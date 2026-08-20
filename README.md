# The Joy of Guix: Or How I Learned to Stop Worrying and Love the Parentheses

A practical, sarcastic, and deeply technical book on **GNU Guix**, functional package management, declarative operating systems, and modern development workflows.

**Author**: Sudheer K. Mohammed  
**Format**: \LaTeX{} Book (`book` document class)  
**Output**: [`main.pdf`](./main.pdf)

---

## 📖 Book Overview

This book demystifies GNU Guix for developers, sysadmins, and curious hackers. It contrasts traditional mutable "Imperative Hellscape" package managers (`apt`, `npm`, `pip`, Docker, systemd) with the mathematical purity and peace of mind of purely functional, reproducible computing in GNU Guile Scheme.

### 📚 Table of Contents

- **Frontmatter**
  - Dedication & Colophon
  - Preface: *The Imperative Hellscape and the Functional Cure*
- **Part I: The Grand Illusion — Package Management Done Right**
  - **Chapter 1**: The Curse of FHS and the Salvation of the Store
  - **Chapter 2**: Daily Life with the Guix CLI (Rollbacks, Generations, GC)
  - **Chapter 3**: Channels, Pins, and Time Travel (Nonguix, Guix Science, `guix time-machine`)
- **Part II: The Development Wonderland — Escaping Dependency Hell**
  - **Chapter 4**: Goodbye Virtualenvs, Hello `guix shell` (`--pure`, `-C`, `--network`)
  - **Chapter 5**: Project Manifests (`manifest.scm`), Transformations & Direnv
- **Part III: The Operating System — Declarative Computing & Shepherd**
  - **Chapter 6**: Guix System: One File to Rule Them All (`config.scm`, bootloader rollbacks)
  - **Chapter 7**: GNU Shepherd: The Lisp-Powered Init System (`herd`)
  - **Chapter 8**: Guix Home: Declarative Dotfiles & Userland
- **Part IV: The Master Craftsman — Packaging with Scheme**
  - **Chapter 9**: The Anatomy of a Package: `(define-public ...)`
  - **Chapter 10**: Build Phases, G-Expressions (`#~`, `#$`), and Shebangs
  - **Chapter 11**: Rolling Your Own Custom Channel
- **Appendices**
  - **Appendix A**: The Ultimate Guix Cheat Sheet
  - **Appendix B**: Troubleshooting & Common Footguns

---

## 🛠 Building the Book

### Prerequisites
- `pdflatex` (TeX Live distribution)
- `make`

### Compilation
```bash
# Compile the PDF (2 passes for TOC and cross-references)
make

# Clean temporary auxiliary files (*.aux, *.log, *.toc)
make clean

# Remove the generated PDF and all auxiliary files
make distclean
```

---

## 📄 License
This work is released under the GNU General Public License v3 or later.
