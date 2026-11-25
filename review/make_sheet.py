"""Draw a stratified sample of imported cards and write a reading sheet:
printed text beside the generated Lean term.  Run:  python3 -I make_sheet.py
Card JSON is untrusted data: it is only parsed, never executed."""
import csv, glob, json, os, random, re, sys
ROOT = "/Users/neal/Code/ski/pokemon"
REPO = ROOT + "/lean-pokemon"
DATA = ROOT + "/data/pokemon-tcg-data/cards/en"
SEED = 20261126
sys.path.insert(0, REPO + "/tools/importer")
import translate as TR  # the repo's own importer, for caveat texts and directions

rows = list(csv.DictReader(open(REPO + "/tools/importer/out/imported.tsv"), delimiter="\t"))
commit = os.popen("git -C %s rev-parse --short HEAD" % REPO).read().strip()

# Lean terms by definition name
terms = {}
for f in sorted(glob.glob(REPO + "/PokemonCards/Standard/Part*.lean")):
    src = open(f).read()
    for m in re.finditer(r"(/-- [^\n]*-/\n)?def (\w+) : Card :=.*?(?=\n\n|\Z)", src, re.S):
        terms[m.group(2)] = (os.path.basename(f), src[:m.start()].count("\n") + 1, m.group(0))

cards = {}
def card(cid):
    s = cid.split("-")[0]
    if s not in cards:
        cards[s] = {c["id"]: c for c in json.load(open("%s/%s.json" % (DATA, s)))}
    return cards[s][cid]

def has_text(r):
    t = terms[r["lean_name"]][2]
    effs = re.findall(r"effect := (.*?),\n", t)
    return "abilities := []" not in t or any(e.strip() != ".skip" for e in effs)

TRAINER = {"Item", "Supporter", "Pokémon Tool", "Stadium"}
ex = lambda r: r["status"] == "imported exactly"
strata = [
    ("Pokémon, exact, with effect text", 6, lambda r: r["kind"] == "Pokémon" and ex(r) and has_text(r)),
    ("Pokémon, exact, no effect text",   1, lambda r: r["kind"] == "Pokémon" and ex(r) and not has_text(r)),
    ("Pokémon, with caveats",            5, lambda r: r["kind"] == "Pokémon" and not ex(r)),
    ("Trainer, exact",                   4, lambda r: r["kind"] in TRAINER and ex(r)),
    ("Trainer, with caveats",            3, lambda r: r["kind"] in TRAINER and not ex(r)),
    ("Special Energy",                   1, lambda r: r["kind"] == "Special Energy"),
]
rng = random.Random(SEED)
out, n = [], 0
head = ["# Card translation reading sheet", "",
  "Sample of 20 imported cards, drawn at random within strata (seed %d) from the %d cards imported at lean-pokemon `%s`." % (SEED, len(rows), commit),
  "For each card: read the printed text, read the Lean term, and mark a verdict.", "",
  "- **Right**: the term does what the card says, apart from the listed caveats and the global departures and readings (Known gaps, top of `Pokemon/Rules.lean`).",
  "- **Wrong**: the term does something the card does not, or omits something, and no listed caveat covers it.",
  "- **Mislabelled**: the term is defensible but a caveat is missing, needless, or has the wrong direction.", "",
  "Units: the model counts damage and HP in tens (HP 110 is `hp := 11`; 50 damage is `damage := 5`).", "",
  "| Stratum | In pool | Sampled |", "|---|---|---|"]
for name, k, pred in strata:
    pool = sorted((r for r in rows if pred(r)), key=lambda r: r["id"])
    pick = rng.sample(pool, k)
    head.append("| %s | %d | %d |" % (name, len(pool), k))
    for r in pick:
        n += 1
        c = card(r["id"]); fn, ln, term = terms[r["lean_name"]]
        o = ["", "---", "", "## %d. %s (%s)" % (n, r["name"], r["id"]), "",
             "Stratum: %s. Status: **%s**. Term: `PokemonCards/Standard/%s:%d`." % (name, r["status"], fn, ln), "", "### Printed", ""]
        bits = [c.get("supertype", "")] + (c.get("subtypes") or [])
        o.append("- **Kind:** " + ", ".join(b for b in bits if b))
        if c.get("hp"):
            o.append("- **HP:** %s. **Type:** %s. **Evolves from:** %s." % (c["hp"], ", ".join(c.get("types") or []), c.get("evolvesFrom") or "none"))
            w = ", ".join("%s %s" % (x["type"], x["value"]) for x in c.get("weaknesses") or []) or "none"
            rs = ", ".join("%s %s" % (x["type"], x["value"]) for x in c.get("resistances") or []) or "none"
            o.append("- **Weakness:** %s. **Resistance:** %s. **Retreat Cost:** %d." % (w, rs, len(c.get("retreatCost") or [])))
        for a in c.get("abilities") or []:
            o.append("- **%s: %s.** %s" % (a.get("type", "Ability"), a["name"], a.get("text", "")))
        for a in c.get("attacks") or []:
            o.append("- **Attack: %s** [%s] %s. %s" % (a["name"], ", ".join(a.get("cost") or []) or "no cost", a.get("damage") or "no damage", a.get("text") or ""))
        for t in c.get("rules") or []:
            o.append("- **Rule text:** " + t)
        o += ["", "### Lean", "", "```lean", term, "```", "", "### Caveats", ""]
        cv = [x for x in re.split(r"[,;\s]+", r["caveats"]) if x]
        if not cv: o.append("None (exact).")
        for x in cv:
            d = getattr(TR, "CAVEAT_DIRECTION", {}).get(x) or getattr(TR, "DIRECTION", {}).get(x, "?")
            o.append("- `%s` (%s): %s" % (x, d, " ".join(str(TR.CAVEATS.get(x, "?")).split())))
        o += ["", "### Verdict", "", "- [ ] Right   - [ ] Wrong   - [ ] Mislabelled", "", "Notes:", ""]
        out += o
head += ["", "With no error found in 20 cards, the 95% upper bound on the error rate of the sampled strata is about 14% (1 − 0.05^(1/20)); the sample is stratified, not proportional, so this is indicative only."]
open("sheet.md", "w").write("\n".join(head + out) + "\n")
print(n, "cards;", len("\n".join(out).splitlines()), "lines")
