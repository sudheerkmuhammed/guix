#!/usr/bin/env python3
"""
generate_readme.py - Generates an extensive, publication-quality README.md
for reading the complete book directly on GitHub.
"""

import os
import re

LABEL_MAP = {
    "chap:curse-of-fhs": ("[Chapter 1](#chapter-1-the-curse-of-fhs-and-the-salvation-of-the-store)", "Chapter 1"),
    "chap:cli-daily-life": ("[Chapter 2](#chapter-2-daily-life-with-the-guix-cli)", "Chapter 2"),
    "chap:channels-and-time-travel": ("[Chapter 3](#chapter-3-channels-pins-and-time-travel)", "Chapter 3"),
    "chap:guix-shell": ("[Chapter 4](#chapter-4-goodbye-virtualenvs-hello-guix-shell)", "Chapter 4"),
    "chap:manifests": ("[Chapter 5](#chapter-5-project-manifests-and-package-transformations)", "Chapter 5"),
    "chap:guix-system": ("[Chapter 6](#chapter-6-guix-system-one-file-to-rule-them-all)", "Chapter 6"),
    "chap:shepherd": ("[Chapter 7](#chapter-7-gnu-shepherd-the-lisp-powered-init-system)", "Chapter 7"),
    "chap:guix-home": ("[Chapter 8](#chapter-8-guix-home-declarative-dotfiles-and-userland)", "Chapter 8"),
    "chap:anatomy-of-package": ("[Chapter 9](#chapter-9-the-anatomy-of-a-package)", "Chapter 9"),
    "chap:phases-and-gexp": ("[Chapter 10](#chapter-10-build-phases-g-expressions-and-shebangs)", "Chapter 10"),
    "chap:custom-channels": ("[Chapter 11](#chapter-11-rolling-your-own-custom-channel)", "Chapter 11"),
    "chap:domain-impact-and-nonguix": ("[Chapter 12](#chapter-12-guix-in-the-wild-domain-impact-and-taming-real-hardware-with-nonguix)", "Chapter 12"),
    "appendix:cheatsheet": ("[Appendix A](#appendix-a-the-ultimate-guix-cheat-sheet)", "Appendix A"),
    "appendix:troubleshooting": ("[Appendix B](#appendix-b-troubleshooting-and-common-footguns)", "Appendix B"),
}

def parse_latex_arg(text, start_idx):
    """Extract content of balanced { ... } starting at start_idx."""
    if start_idx >= len(text) or text[start_idx] != '{':
        return None, start_idx
    depth = 0
    i = start_idx
    while i < len(text):
        if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
            depth += 1
        elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
            depth -= 1
            if depth == 0:
                return text[start_idx+1:i], i + 1
        i += 1
    return None, start_idx

def replace_command_recursive(text, cmd_name, handler):
    """Replace occurrences of \\cmd{...} supporting nested braces."""
    pattern = re.compile(re.escape(cmd_name) + r'(\s*\{)')
    while True:
        m = pattern.search(text)
        if not m:
            break
        brace_pos = m.end() - 1
        arg, end_pos = parse_latex_arg(text, brace_pos)
        if arg is None:
            # If unmatched, break to avoid infinite loop
            break
        replacement = handler(arg)
        text = text[:m.start()] + replacement + text[end_pos:]
    return text

def clean_inline_latex(text):
    if not text:
        return ""

    # Remove multi-arg commands first
    text = re.sub(r'\\addcontentsline\s*\{[^}]*\}\s*\{[^}]*\}\s*\{[^}]*\}', '', text)

    # Commands with arguments that need nested handling
    text = replace_command_recursive(text, r'\color', lambda arg: '')
    text = replace_command_recursive(text, r'\caption', lambda arg: f"\n\n*{clean_inline_latex(arg)}*\n\n")
    text = replace_command_recursive(text, r'\texttt', lambda arg: f"`{arg}`")
    text = replace_command_recursive(text, r'\guixcmd', lambda arg: f"`{arg}`")
    text = replace_command_recursive(text, r'\storepath', lambda arg: f"`{arg}`")
    text = replace_command_recursive(text, r'\code', lambda arg: f"`{arg}`")
    text = replace_command_recursive(text, r'\textbf', lambda arg: f"**{arg}**")
    text = replace_command_recursive(text, r'\textit', lambda arg: f"*{arg}*")
    text = replace_command_recursive(text, r'\emph', lambda arg: f"*{arg}*")
    text = replace_command_recursive(text, r'\url', lambda arg: f"<{arg}>")

    # Replace chapter references with Markdown links
    def handle_ref(label):
        if label in LABEL_MAP:
            return LABEL_MAP[label][0]
        return f"`{label}`"
    
    # Handle "Chapter~\ref{...}" or "Chapter \ref{...}" or "\ref{...}"
    def replace_chap_ref(m):
        prefix = m.group(1) # e.g. "Chapter~" or "Chapter "
        label = m.group(2)
        if label in LABEL_MAP:
            return LABEL_MAP[label][0]
        return f"{prefix}`{label}`"
    text = re.sub(r'(Chapter[~\s]+)\\ref\{([^}]+)\}', replace_chap_ref, text)
    text = replace_command_recursive(text, r'\ref', handle_ref)

    text = replace_command_recursive(text, r'\label', lambda arg: "")
    text = replace_command_recursive(text, r'\cite', lambda arg: "")
    text = replace_command_recursive(text, r'\vspace', lambda arg: "")
    text = replace_command_recursive(text, r'\rule', lambda arg: "---")

    # Math / arrows
    text = text.replace(r'$\longrightarrow$', '→')
    text = text.replace(r'\longrightarrow', '→')
    text = text.replace(r'\LaTeX{}', 'LaTeX')
    text = text.replace(r'\LaTeX', 'LaTeX')

    # Special characters
    text = text.replace(r'\%', '%')
    text = text.replace(r'\&', '&')
    text = text.replace(r'\_', '_')
    text = text.replace(r'\#', '#')
    text = text.replace(r'\$', '$')
    text = text.replace(r'\textasciitilde', '~')
    text = text.replace(r'\textasciicircum', '^')
    text = text.replace('---', '—')
    text = text.replace('--', '–')
    text = text.replace('``', '"').replace("''", '"')

    # Strip standalone commands
    text = re.sub(r'\\small\b', '', text)
    text = re.sub(r'\\itshape\b', '', text)
    text = re.sub(r'\\bfseries\b', '', text)
    text = re.sub(r'\\noindent\b', '', text)
    text = re.sub(r'\\cleardoublepage\b', '', text)
    text = re.sub(r'\\clearpage\b', '', text)
    text = re.sub(r'\\vfill\b', '', text)
    text = re.sub(r'\\centering\b', '', text)
    text = re.sub(r'\\Large\b', '', text)
    text = re.sub(r'\\Huge\b', '', text)
    text = re.sub(r'\\begin\{center\}', '', text)
    text = re.sub(r'\\end\{center\}', '', text)
    text = re.sub(r'\\begin\{titlepage\}.*?\\end\{titlepage\}', '', text, flags=re.DOTALL)

    return text

def convert_table(table_tex):
    lines = [l.strip() for l in table_tex.split('\n') if l.strip()]
    rows = []
    for line in lines:
        if any(cmd in line for cmd in ['\\toprule', '\\midrule', '\\bottomrule', '\\addlinespace', '\\begin{tabular', '\\end{tabular']):
            continue
        if '&' in line:
            line = re.sub(r'\\\\.*$', '', line)
            cells = [clean_inline_latex(c.strip()) for c in line.split('&')]
            rows.append(cells)

    if not rows:
        return ""

    num_cols = max(len(r) for r in rows)
    padded_rows = []
    for r in rows:
        r_padded = r + [''] * (num_cols - len(r))
        padded_rows.append(r_padded)

    header = padded_rows[0]
    separator = [' :--- ' for _ in range(num_cols)]

    md_lines = []
    md_lines.append('| ' + ' | '.join(header) + ' |')
    md_lines.append('|' + '|'.join(separator) + '|')
    for row in padded_rows[1:]:
        md_lines.append('| ' + ' | '.join(row) + ' |')

    return '\n' + '\n'.join(md_lines) + '\n'

def convert_latex_chapter(tex_content, chapter_num=None, appendix_letter=None):
    code_blocks = []
    tables = []

    # 1. Protect listings
    def save_listing(m):
        opts = m.group(1) or ""
        code = m.group(2)
        lang = "scheme"
        if "guixcli" in opts or "bash" in opts or "sh" in opts:
            lang = "bash"
        elif "scheme" in opts:
            lang = "scheme"
        idx = len(code_blocks)
        code_blocks.append(f"```{lang}\n{code.strip()}\n```")
        return f"@@@CODE_BLOCK_{idx}@@@"
    tex_content = re.sub(r'\\begin\{lstlisting\}(?:\[([^\]]*)\])?(.*?)\\end\{lstlisting\}', save_listing, tex_content, flags=re.DOTALL)

    # 2. Protect tables
    def save_table(m):
        full_table = m.group(0)
        idx = len(tables)
        converted = convert_table(full_table)
        tables.append(converted)
        return f"\n@@@TABLE_BLOCK_{idx}@@@\n"
    tex_content = re.sub(r'\\begin\{tabular[x]?\}.*?\\end\{tabular[x]?\}', save_table, tex_content, flags=re.DOTALL)
    tex_content = re.sub(r'\\begin\{table\}(?:\[[^\]]*\])?\s*(.*?)\s*\\end\{table\}', r'\1', tex_content, flags=re.DOTALL)

    # 3. Epigraph
    def replace_epigraph(m):
        quote = m.group(1)
        author = m.group(2).replace(r'\---', '—').replace('---', '—')
        quote = clean_inline_latex(quote).strip()
        author = clean_inline_latex(author).strip()
        # Clean double dash in author
        author = re.sub(r'^[—\s-]+', '', author).strip()
        return f"\n> *\"{quote}\"*\n> \n> — **{author}**\n\n"
    tex_content = re.sub(r'\\epigraph\{([^}]+)\}\{([^}]+)\}', replace_epigraph, tex_content)

    # 4. Chapters & Sections
    if chapter_num:
        tex_content = replace_command_recursive(tex_content, r'\chapter', lambda arg: f"\n\n## Chapter {chapter_num}: {clean_inline_latex(arg)}\n\n")
    elif appendix_letter:
        tex_content = replace_command_recursive(tex_content, r'\chapter', lambda arg: f"\n\n## Appendix {appendix_letter}: {clean_inline_latex(arg)}\n\n")
    else:
        tex_content = replace_command_recursive(tex_content, r'\chapter*', lambda arg: f"\n\n## {clean_inline_latex(arg)}\n\n")
        tex_content = replace_command_recursive(tex_content, r'\chapter', lambda arg: f"\n\n## {clean_inline_latex(arg)}\n\n")

    tex_content = replace_command_recursive(tex_content, r'\section*', lambda arg: f"\n\n### {clean_inline_latex(arg)}\n\n")
    tex_content = replace_command_recursive(tex_content, r'\section', lambda arg: f"\n\n### {clean_inline_latex(arg)}\n\n")
    tex_content = replace_command_recursive(tex_content, r'\subsection*', lambda arg: f"\n\n#### {clean_inline_latex(arg)}\n\n")
    tex_content = replace_command_recursive(tex_content, r'\subsection', lambda arg: f"\n\n#### {clean_inline_latex(arg)}\n\n")
    tex_content = replace_command_recursive(tex_content, r'\subsubsection*', lambda arg: f"\n\n##### {clean_inline_latex(arg)}\n\n")
    tex_content = replace_command_recursive(tex_content, r'\subsubsection', lambda arg: f"\n\n##### {clean_inline_latex(arg)}\n\n")

    # 5. Figures and images (extract with nested braces support for caption)
    def replace_figure(m):
        content = m.group(1)
        img_match = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', content)
        cap_match = re.search(r'\\caption\*?\s*\{', content)
        caption = ""
        if cap_match:
            brace_pos = cap_match.end() - 1
            raw_cap, _ = parse_latex_arg(content, brace_pos)
            if raw_cap:
                caption = clean_inline_latex(raw_cap).strip()
                caption = re.sub(r'^\*+|\*+$', '', caption).strip()
        if img_match:
            img_path = img_match.group(1)
            return f"\n\n<div align=\"center\">\n  <img src=\"{img_path}\" width=\"720\" alt=\"{caption}\"/>\n  <br/>\n  <em>{caption}</em>\n</div>\n\n"
        return ""
    tex_content = re.sub(r'\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}', replace_figure, tex_content, flags=re.DOTALL)

    # 6. Callout boxes using GitHub Native Alerts:
    # protipbox -> [!TIP]
    # footgunbox -> [!WARNING]
    # alchemybox -> [!IMPORTANT]
    # tearsbox -> [!CAUTION]
    # tcolorbox -> [!NOTE]
    def replace_callout_box(box_type, alert_tag, emoji, default_name):
        pattern = r'\\begin\{' + box_type + r'\}(?:\[([^\]]*)\])?(.*?)\\end\{' + box_type + r'\}'
        def repl(m):
            raw_title = m.group(1) or ""
            body = m.group(2).strip()
            if 'title=' in raw_title:
                m_title = re.search(r'title=([^,\]]+)', raw_title)
                title = m_title.group(1) if m_title else ""
            else:
                title = raw_title
            clean_t = clean_inline_latex(title).strip()
            header_str = f"{emoji} {default_name}: {clean_t}" if clean_t else f"{emoji} {default_name}"

            # Clean body
            body_clean = clean_inline_latex(body)

            # We format lines with >
            lines = body_clean.split('\n')
            quoted_lines = []
            for l in lines:
                quoted_lines.append(f"> {l}" if l.strip() else ">")
            content_quoted = '\n'.join(quoted_lines)

            return f"\n> [!{alert_tag}]\n> **{header_str}**\n>\n{content_quoted}\n\n"
        return pattern, repl

    for box, alert, emoji, name in [
        ('protipbox', 'TIP', '💡', 'Guix Wizard Pro-Tip'),
        ('footgunbox', 'WARNING', '⚠️', 'Caution: Footgun Detected!'),
        ('alchemybox', 'IMPORTANT', '✨', 'Functional Alchemy & Arcana'),
        ('tearsbox', 'CAUTION', '😭', 'Tears of the Imperative Developer'),
        ('tcolorbox', 'NOTE', 'ℹ️', 'Diagnostic Information')
    ]:
        pat, repl = replace_callout_box(box, alert, emoji, name)
        tex_content = re.sub(pat, repl, tex_content, flags=re.DOTALL)

    # 7. Lists
    tex_content = re.sub(r'\\begin\{itemize\}', '', tex_content)
    tex_content = re.sub(r'\\end\{itemize\}', '', tex_content)
    tex_content = re.sub(r'\\begin\{enumerate\}', '', tex_content)
    tex_content = re.sub(r'\\end\{enumerate\}', '', tex_content)
    tex_content = re.sub(r'\\item\s*', r'- ', tex_content)

    # 8. Clean remaining inline LaTeX
    tex_content = clean_inline_latex(tex_content)

    # 9. Restore Tables
    for i, tbl in enumerate(tables):
        def restore_tbl(m):
            prefix = m.group(1)
            if prefix.strip().startswith('>'):
                lines = tbl.strip().split('\n')
                return '\n' + '\n'.join([f"> {l}" for l in lines]) + '\n>'
            return '\n' + tbl + '\n'
        tex_content = re.sub(rf'(>*\s*)@@@TABLE_BLOCK_{i}@@@', restore_tbl, tex_content)

    # 10. Restore Code blocks
    for i, cb in enumerate(code_blocks):
        def restore_code(m):
            prefix = m.group(1)
            if prefix.strip().startswith('>'):
                lines = cb.strip().split('\n')
                return '\n' + '\n'.join([f"> {l}" for l in lines]) + '\n>'
            return '\n' + cb + '\n'
        tex_content = re.sub(rf'(>*\s*)@@@CODE_BLOCK_{i}@@@', restore_code, tex_content)

    # Remove trailing line breaks `\\`
    tex_content = re.sub(r'\\\\\s*$', '', tex_content, flags=re.MULTILINE)
    tex_content = re.sub(r'\\\\\n', '\n', tex_content)

    # Collapse excess newlines
    tex_content = re.sub(r'\n{3,}', '\n\n', tex_content)

    return tex_content.strip()

def build_full_readme():
    chapters_info = [
        ("frontmatter/dedication.tex", None, None, None),
        ("frontmatter/preface.tex", None, None, "Preface: The Imperative Hellscape and the Functional Cure"),
        ("chapters/ch01_curse_of_fhs.tex", "Part I: The Grand Illusion — Package Management Done Right", 1, "The Curse of FHS and the Salvation of the Store"),
        ("chapters/ch02_cli_daily_life.tex", None, 2, "Daily Life with the Guix CLI"),
        ("chapters/ch03_channels_time_travel.tex", None, 3, "Channels, Pins, and Time Travel"),
        ("chapters/ch04_guix_shell.tex", "Part II: The Development Wonderland — Escaping Dependency Hell", 4, "Goodbye Virtualenvs, Hello guix shell"),
        ("chapters/ch05_manifests.tex", None, 5, "Project Manifests and Package Transformations"),
        ("chapters/ch06_guix_system.tex", "Part III: The Operating System — Declarative Computing & Shepherd", 6, "Guix System: One File to Rule Them All"),
        ("chapters/ch07_shepherd.tex", None, 7, "GNU Shepherd: The Lisp-Powered Init System"),
        ("chapters/ch08_guix_home.tex", None, 8, "Guix Home: Declarative Dotfiles and Userland"),
        ("chapters/ch09_anatomy_of_package.tex", "Part IV: The Master Craftsman — Packaging with Scheme", 9, "The Anatomy of a Package"),
        ("chapters/ch10_phases_and_gexp.tex", None, 10, "Build Phases, G-Expressions, and Shebangs"),
        ("chapters/ch11_custom_channels.tex", None, 11, "Rolling Your Own Custom Channel"),
        ("chapters/ch12_domain_impact_and_nonguix.tex", "Part V: The Real-World Frontier — Domains & Pragmatic Hardware", 12, "Guix in the Wild: Domain Impact and Taming Real Hardware with Nonguix"),
        ("backmatter/appendix_cheatsheet.tex", "Appendices", None, "The Ultimate Guix Cheat Sheet", "A"),
        ("backmatter/appendix_troubleshooting.tex", None, None, "Troubleshooting and Common Footguns", "B"),
    ]

    header = """# The Joy of Guix: Or How I Learned to Stop Worrying and Love the Parentheses

<div align="center">
  <img src="images/book_cover.jpg" width="480" alt="The Joy of Guix Book Cover"/>
  <br/><br/>
  <h3>A Practical, Sarcastic, and Deeply Technical Guide to Functional Computing</h3>
  <p>
    <strong>Author:</strong> Sudheer K. Mohammed &nbsp;|&nbsp;
    <strong>License:</strong> GNU General Public License v3 or later
  </p>
  <p>
    <a href="main.pdf"><strong>📥 Download PDF Edition</strong></a> &nbsp;•&nbsp;
    <a href="the_joy_of_guix.epub"><strong>📱 Download EPUB Edition</strong></a> &nbsp;•&nbsp;
    <a href="#-table-of-contents"><strong>📖 Read Online Below</strong></a>
  </p>
</div>

---

## 🧭 About This Book

Welcome to **The Joy of Guix**! This book is written for developers, systems engineers, DevOps practitioners, scientific researchers, and curious tinkerers who are exhausted by the fragility of traditional mutable operating systems and package managers.

Whether you run Guix as an unprivileged, transactional package manager on top of an existing distribution (**Ubuntu, Debian, Fedora, Arch, openSUSE**), or deploy it as a fully unified declarative operating system (**Guix System**), this book provides a complete, hands-on path from first principles to advanced mastery.

---

## 📑 Table of Contents

- [**Dedication & Colophon**](#dedication)
- [**Preface: The Imperative Hellscape and the Functional Cure**](#preface-the-imperative-hellscape-and-the-functional-cure)
- [**Part I: The Grand Illusion — Package Management Done Right**](#part-i-the-grand-illusion--package-management-done-right)
  - [Chapter 1: The Curse of FHS and the Salvation of the Store](#chapter-1-the-curse-of-fhs-and-the-salvation-of-the-store)
  - [Chapter 2: Daily Life with the Guix CLI](#chapter-2-daily-life-with-the-guix-cli)
  - [Chapter 3: Channels, Pins, and Time Travel](#chapter-3-channels-pins-and-time-travel)
- [**Part II: The Development Wonderland — Escaping Dependency Hell**](#part-ii-the-development-wonderland--escaping-dependency-hell)
  - [Chapter 4: Goodbye Virtualenvs, Hello `guix shell`](#chapter-4-goodbye-virtualenvs-hello-guix-shell)
  - [Chapter 5: Project Manifests and Package Transformations](#chapter-5-project-manifests-and-package-transformations)
- [**Part III: The Operating System — Declarative Computing & Shepherd**](#part-iii-the-operating-system--declarative-computing--shepherd)
  - [Chapter 6: Guix System: One File to Rule Them All](#chapter-6-guix-system-one-file-to-rule-them-all)
  - [Chapter 7: GNU Shepherd: The Lisp-Powered Init System](#chapter-7-gnu-shepherd-the-lisp-powered-init-system)
  - [Chapter 8: Guix Home: Declarative Dotfiles and Userland](#chapter-8-guix-home-declarative-dotfiles-and-userland)
- [**Part IV: The Master Craftsman — Packaging with Scheme**](#part-iv-the-master-craftsman--packaging-with-scheme)
  - [Chapter 9: The Anatomy of a Package](#chapter-9-the-anatomy-of-a-package)
  - [Chapter 10: Build Phases, G-Expressions, and Shebangs](#chapter-10-build-phases-g-expressions-and-shebangs)
  - [Chapter 11: Rolling Your Own Custom Channel](#chapter-11-rolling-your-own-custom-channel)
- [**Part V: The Real-World Frontier — Domains & Pragmatic Hardware**](#part-v-the-real-world-frontier--domains--pragmatic-hardware)
  - [Chapter 12: Guix in the Wild: Domain Impact and Taming Real Hardware with Nonguix](#chapter-12-guix-in-the-wild-domain-impact-and-taming-real-hardware-with-nonguix)
- [**Appendices**](#appendices)
  - [Appendix A: The Ultimate Guix Cheat Sheet](#appendix-a-the-ultimate-guix-cheat-sheet)
  - [Appendix B: Troubleshooting and Common Footguns](#appendix-b-troubleshooting-and-common-footguns)
- [**Building Offline Editions (PDF & EPUB)**](#building-offline-editions)
- [**License & Acknowledgments**](#license)

---

"""

    body = ""

    for item in chapters_info:
        path = item[0]
        part_heading = item[1]
        ch_num = item[2]
        ch_title = item[3]
        app_letter = item[4] if len(item) > 4 else None

        if part_heading:
            body += f"\n\n---\n\n# {part_heading}\n\n"

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            ch_md = convert_latex_chapter(content, chapter_num=ch_num, appendix_letter=app_letter)

            # Special case for dedication
            if "dedication.tex" in path:
                body += """<a id="dedication"></a>

## Dedication

> *Dedicated to everyone who ever ran `sudo apt-get dist-upgrade` at 4:58 PM on a Friday and spent the entire weekend staring at a broken X server and crying into an unbootable kernel.*
>
> *To all the developers whose software "works on my machine" and immediately bursts into flames on anyone else's.*
>
> *And to the humble parenthesis `()`, without which this entire universe would dissolve into an unstructured chaos of arbitrary YAML indents.*

<br/>

**Colophon**  
This book was typeset with LaTeX using `pdflatex`. The code examples were validated against GNU Guix on GNU/Linux. No global states, mutable `/usr/lib` symlinks, or Python virtualenvs were harmed in the making of this manuscript. All builds are bit-for-bit reproducible, give or take cosmic rays.

[⬆ Back to Table of Contents](#-table-of-contents)

"""
                continue

            body += f"\n\n{ch_md}\n\n"
            body += "[⬆ Back to Table of Contents](#-table-of-contents)\n\n"

    footer = """---

# Building Offline Editions

If you prefer to read offline or print a physical copy, you can compile both the high-resolution vector PDF and EPUB editions locally using the included `Makefile`.

### System Requirements
- **LaTeX Distribution:** `pdflatex` (TeX Live with standard collections)
- **EPUB Builder:** `pandoc` (v2.19+) and `python3` (v3.8+)
- **Build Automation:** GNU `make`

### Compilation Commands

```bash
# 1. Clone the repository
git clone https://github.com/sudheerkmuhammed/guix.git
cd guix

# 2. Build both PDF and EPUB editions
make all

# 3. Build only the PDF (performs 2 passes for cross-references & TOC)
make pdf

# 4. Build only the EPUB edition
make epub

# 5. Clean auxiliary build files (.aux, .log, .toc)
make clean

# 6. Re-generate this extensive README.md from LaTeX sources
python3 generate_readme.py
```

---

# License

Copyright © 2026 Sudheer K. Mohammed.

This book and its accompanying source code are free documentation: you can redistribute them and/or modify them under the terms of the **GNU General Public License** as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

All package definitions, Scheme manifests, and configurations presented herein are released into the public domain under the **Creative Commons CC0 1.0 Universal Public Domain Dedication**.

[⬆ Back to Table of Contents](#-table-of-contents)
"""

    full_readme = header + body + footer
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(full_readme)

    print(f"Generated README.md successfully: {len(full_readme)} bytes, {len(full_readme.splitlines())} lines.")

if __name__ == "__main__":
    build_full_readme()
