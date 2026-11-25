# paper-pokemon-tcg

A Mechanized Model of the Pokémon TCG: Finite Quotients for Restricted Decks and a
Counter-Machine Embedding.

Draft of a paper on a Lean 4 model of the rules of the Pokémon Trading Card Game: finite quotients
of the reachable states for two restricted classes of decks (tame and store-safe), and an
embedding of two-counter machines in the same model for decks that no printed card supplies.

**Status: a draft, not submitted.** The Lean model, the importer, the surveys and the manuscript
were produced with large language model agents directed by the author, as the paper's
"Provenance and use of AI" paragraph states. The draft has been reviewed only by such agents, not
by human referees. Some bibliography entries are marked unverified in `refs.bib`. The
machine-checked results it describes live in
[sigilante/lean-pokemon](https://github.com/sigilante/lean-pokemon) (audited commit 05a38b3);
where the paper and the Lean source disagree, the Lean source is authoritative.

Build: `latexmk -pdf mss.tex`. A compiled `mss.pdf` is kept in the repository and rebuilt with each change to the source.

Listing check: `python3 tools/listing_check.py PATH/TO/lean-pokemon` (a checkout at the cited commit, 05a38b3) compares every Lean declaration displayed in `mss.tex` with the source, as whole declarations.
It uses the Python standard library only and exits non-zero if any displayed declaration or card term does not match.

Licence: the paper (text, figures and bibliography) is © 2026 N. E. Davis (Sigilante), released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); see `LICENSE`.
The licence covers the author's own text, tables and figures only. Pokémon, card names and quoted
card and rulebook text belong to their owners (Nintendo, Creatures Inc., GAME FREAK inc. and The
Pokémon Company); they are quoted for research and commentary and are not licensed by the author.
This work is not affiliated with, sponsored or endorsed by them. See `NOTICE`.
