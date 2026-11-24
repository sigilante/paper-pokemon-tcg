#!/usr/bin/env python3
"""Check every Lean listing of mss.tex against a lean-pokemon checkout.

Usage:  python3 tools/listing_check.py PATH/TO/lean-pokemon [--tex mss.tex]

Every declaration displayed in an lstlisting environment of the manuscript (a line that starts,
in column 0, with theorem, def, inductive, structure, abbrev, instance or class) must match a
declaration of the same name in the .lean files of the checkout (Pokemon/, PokemonCards/ and the
two root files).  Both sides are compared as whole declarations, after removing comments and
docstrings, leading attributes, the modifiers private/protected/noncomputable/nonrec, trailing
`deriving` clauses, and collapsing whitespace.  A listing matches if it equals the source
declaration, or, for a theorem, equals its statement (the source declaration up to the `:=`).
A listing may qualify a name that the source declares inside a namespace.  Card terms
(definitions in PokemonCards/) are counted separately.  The checkout's commit is printed, not
checked: run it on a checkout of the commit the paper cites.

Exits 0 if every displayed declaration matches, 1 otherwise (each failure is printed), 2 on a
usage error.
Standard library only; reads files, writes nothing.
"""
import os
import re
import subprocess
import sys

KW = r'(?:theorem|def|inductive|structure|abbrev|instance|class)'
MODS = r'(?:(?:private|protected|noncomputable|nonrec|partial)\s+)*'
HEAD = re.compile(r'^(?:@\[[^\]]*\]\s*)*' + MODS + KW + r'\b')
NAME = re.compile(r'^(?:@\[[^\]]*\]\s*)*' + MODS + KW + r'\s+([^\s(:{\[]+)')
# Column-0 lines that end a declaration in a source file.
STOP = re.compile(r'^(?:@\[|end\b|namespace\b|section\b|open\b|variable\b|set_option\b|'
                  r'attribute\b|#|example\b|universe\b|noncomputable section\b|private\b|'
                  r'protected\b|theorem\b|def\b|inductive\b|structure\b|abbrev\b|instance\b|'
                  r'class\b|mutual\b|macro\b|syntax\b|elab\b|lemma\b|opaque\b|axiom\b)')


def strip_comments(text):
    """Remove `--` line comments and nested `/- ... -/` block comments (docstrings included),
    leaving string literals intact."""
    out = []
    i, n, depth = 0, len(text), 0
    while i < n:
        if depth:
            if text.startswith('/-', i):
                depth += 1
                i += 2
            elif text.startswith('-/', i):
                depth -= 1
                i += 2
            else:
                if text[i] == '\n':
                    out.append('\n')
                i += 1
            continue
        c = text[i]
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(text[i:j + 1])
            i = j + 1
        elif text.startswith('/-', i):
            depth = 1
            i += 2
        elif text.startswith('--', i):
            while i < n and text[i] != '\n':
                i += 1
        else:
            out.append(c)
            i += 1
    return ''.join(out)


def normalise(decl):
    s = ' '.join(decl.split())
    s = re.sub(r'^(?:@\[[^\]]*\]\s*)*', '', s)
    s = re.sub(r'^' + MODS, '', s)
    s = re.sub(r'\s+deriving\s+[\w.,\s]+$', '', s)
    return s.strip()


def split_decls(lines):
    """Split column-0 code into declarations: (name, text)."""
    decls, cur = [], None
    for line in lines:
        if line and not line[0].isspace() and STOP.match(line):
            if cur is not None:
                decls.append(cur)
                cur = None
            if HEAD.match(line):
                cur = [line]
            elif line.startswith('@['):
                cur = [line]  # attribute line: the declaration follows
            continue
        if cur is not None:
            cur.append(line)
    if cur is not None:
        decls.append(cur)
    out = []
    for d in decls:
        text = '\n'.join(d)
        flat = ' '.join(text.split())
        m = NAME.match(flat)
        if m:
            out.append((m.group(1), text))
    return out


def source_decls(root):
    table = {}
    files = []
    for top in ('Pokemon', 'PokemonCards'):
        base = os.path.join(root, top)
        if not os.path.isdir(base):
            sys.exit(f'listing_check: {base} is not a directory; is {root} a lean-pokemon checkout?')
        for dp, _, fs in os.walk(base):
            files += [os.path.join(dp, f) for f in fs if f.endswith('.lean')]
        rootfile = base + '.lean'
        if os.path.isfile(rootfile):
            files.append(rootfile)
    for p in sorted(files):
        with open(p, encoding='utf-8') as fh:
            code = strip_comments(fh.read())
        rel = os.path.relpath(p, root)
        for name, text in split_decls(code.splitlines()):
            table.setdefault(name, []).append((rel, normalise(text)))
    return table


def listing_decls(tex):
    with open(tex, encoding='utf-8') as fh:
        src = fh.read()
    blocks = re.findall(r'\\begin\{lstlisting\}(?:\[[^\]]*\])?\n(.*?)\\end\{lstlisting\}', src, re.S)
    out = []
    for b in blocks:
        cur = None
        for line in b.splitlines():
            if line and not line[0].isspace() and HEAD.match(line):
                if cur:
                    out.append(cur)
                cur = [line]
            elif cur is not None:
                cur.append(line)
        if cur:
            out.append(cur)
    res = []
    for d in out:
        text = '\n'.join(d)
        m = NAME.match(' '.join(text.split()))
        res.append((m.group(1), normalise(text)))
    return len(blocks), res


def matches(listing, source):
    if listing == source:
        return True
    # Only a theorem may be shown by its statement alone.
    return (listing.startswith('theorem ') and source.startswith(listing)
            and source[len(listing):].startswith(' :='))


def main(argv):
    args = list(argv[1:])
    tex = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mss.tex')
    if '--tex' in args:
        i = args.index('--tex')
        tex = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    try:
        head = subprocess.run(['git', '-C', args[0], 'rev-parse', '--short', 'HEAD'],
                              capture_output=True, text=True).stdout.strip()
    except OSError:
        head = ''
    print(f'listing_check: checkout {args[0]} at commit {head or "unknown"}')
    table = source_decls(args[0])
    nblocks, decls = listing_decls(tex)
    bad, cards = 0, 0
    for name, text in decls:
        # A listing may qualify a name that the source declares inside a namespace
        # (`Lingering.reduce_breaks_clamp` for `reduce_breaks_clamp` in `namespace Lingering`).
        parts = name.split('.')
        cands, hit = [], []
        for i in range(len(parts)):
            short = '.'.join(parts[i:])
            for f, s in table.get(short, []):
                cands.append((f, s))
                if matches(text.replace(name, short, 1), s):
                    hit.append(f)
            if hit:
                break
        if not hit:
            bad += 1
            where = ', '.join(f for f, _ in cands) or 'no declaration of that name'
            print(f'MISMATCH {name}  (candidates: {where})')
            print(f'  listing: {text[:300]}')
            for f, s in cands:
                print(f'  {f}: {s[:300]}')
        elif any(f.startswith('PokemonCards') for f in hit) and text.startswith('def '):
            cards += 1
    print(f'listing_check: {nblocks} listings, {len(decls)} declarations '
          f'({len(decls) - cards} model declarations, {cards} card terms); {bad} mismatches')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
