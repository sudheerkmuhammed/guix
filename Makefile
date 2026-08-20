# Makefile for building "The Joy of Guix" LaTeX book

LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error
MAIN = main
TARGET = $(MAIN).pdf

CHAPTERS = $(wildcard chapters/*.tex)
FRONTMATTER = $(wildcard frontmatter/*.tex)
BACKMATTER = $(wildcard backmatter/*.tex)

.PHONY: all pdf clean distclean view

all: pdf

pdf: $(TARGET)

$(TARGET): $(MAIN).tex preamble.tex $(CHAPTERS) $(FRONTMATTER) $(BACKMATTER)
	@echo "==> Compiling LaTeX document (Pass 1)..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	@echo "==> Compiling LaTeX document (Pass 2 for Table of Contents & References)..."
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	@echo "==> Compilation complete! Output generated at $(TARGET)"

clean:
	@echo "==> Cleaning intermediate LaTeX auxiliary files..."
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb *.bbl *.blg *.fls *.fdb_latexmk frontmatter/*.aux chapters/*.aux backmatter/*.aux

distclean: clean
	@echo "==> Removing generated PDF..."
	rm -f $(TARGET)
