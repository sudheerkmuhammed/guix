# Makefile for building "The Joy of Guix" (PDF & EPUB)

LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error
MAIN = main
TARGET_PDF = $(MAIN).pdf
TARGET_EPUB = the_joy_of_guix.epub
TARGET_README = README.md

CHAPTERS = $(wildcard chapters/*.tex)
FRONTMATTER = $(wildcard frontmatter/*.tex)
BACKMATTER = $(wildcard backmatter/*.tex)
IMAGES = $(wildcard images/*.jpg)

.PHONY: all pdf epub readme clean distclean

all: pdf epub readme

pdf: $(TARGET_PDF)

epub: $(TARGET_EPUB)

readme: $(TARGET_README)

$(TARGET_PDF): $(MAIN).tex preamble.tex $(CHAPTERS) $(FRONTMATTER) $(BACKMATTER) $(IMAGES)
	@echo "==> Compiling LaTeX document (Pass 1)..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	@echo "==> Compiling LaTeX document (Pass 2 for Table of Contents & References)..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	@echo "==> PDF compilation complete! Output: $(TARGET_PDF)"

$(TARGET_EPUB): build_epub.py generate_readme.py $(CHAPTERS) $(FRONTMATTER) $(BACKMATTER) $(IMAGES)
	@echo "==> Generating EPUB edition..."
	python3 build_epub.py
	@echo "==> EPUB generation complete! Output: $(TARGET_EPUB)"

$(TARGET_README): generate_readme.py $(CHAPTERS) $(FRONTMATTER) $(BACKMATTER) $(IMAGES)
	@echo "==> Generating extensive GitHub README..."
	python3 generate_readme.py
	@echo "==> README generation complete! Output: $(TARGET_README)"

clean:
	@echo "==> Cleaning intermediate auxiliary files..."
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.bbl *.blg *.fls *.fdb_latexmk frontmatter/*.aux chapters/*.aux backmatter/*.aux the_joy_of_guix.md

distclean: clean
	@echo "==> Removing generated PDF and EPUB..."
	rm -f $(TARGET_PDF) $(TARGET_EPUB)
