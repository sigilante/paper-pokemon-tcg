# Build the paper: A Mechanized Model of the Pokemon TCG (amsart; venue undecided).
#   make          build mss.pdf (latexmk runs pdflatex and bibtex as needed)
#   make check    build, then report errors, undefined refs/cites, and overfull boxes
#   make watch    rebuild on every save
#   make dist     source tarball: mss.tex, mss.bbl, refs.bib, the class files
#   make clean    remove build byproducts, keep mss.pdf
#   make distclean  remove mss.pdf and the tarball too

MAIN    := mss
BIBS    := refs.bib
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
SOURCES := $(MAIN).tex $(BIBS) $(wildcard *.cls)
DIST    := paper-pokemon-tcg

.PHONY: all check watch dist clean distclean

all: $(MAIN).pdf

$(MAIN).pdf: $(SOURCES)
	$(LATEXMK) $(MAIN).tex

check: $(MAIN).pdf
	@echo '--- errors'; grep -n '^!' $(MAIN).log || echo none
	@echo '--- undefined references and citations'; grep -n -i 'undefined' $(MAIN).log || echo none
	@echo '--- overfull hboxes'; grep -n 'Overfull .hbox' $(MAIN).log || echo none
	@grep -o 'Output written on .*' $(MAIN).log

watch:
	$(LATEXMK) -pvc -view=none $(MAIN).tex

dist: $(MAIN).pdf
	rm -rf $(DIST) && mkdir $(DIST)
	cp $(MAIN).tex $(MAIN).bbl $(BIBS) $(wildcard *.cls) $(DIST)/
	tar czf $(DIST).tar.gz $(DIST) && rm -rf $(DIST)
	@echo wrote $(DIST).tar.gz

clean:
	latexmk -c $(MAIN).tex
	rm -f $(MAIN).bbl $(MAIN).run.xml build.log build.out

distclean: clean
	rm -f $(MAIN).pdf $(DIST).tar.gz
