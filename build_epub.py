#!/usr/bin/env python3
"""
build_epub.py - Converts LaTeX book sources to clean Markdown and generates
the EPUB edition of 'The Joy of Guix' using Pandoc.
"""

import os
import subprocess
from generate_readme import convert_latex_chapter

def build():
    book_order = [
        ("frontmatter/dedication.tex", None, None),
        ("frontmatter/preface.tex", None, None),
        ("chapters/ch01_curse_of_fhs.tex", 1, None),
        ("chapters/ch02_cli_daily_life.tex", 2, None),
        ("chapters/ch03_channels_time_travel.tex", 3, None),
        ("chapters/ch04_guix_shell.tex", 4, None),
        ("chapters/ch05_manifests.tex", 5, None),
        ("chapters/ch06_guix_system.tex", 6, None),
        ("chapters/ch07_shepherd.tex", 7, None),
        ("chapters/ch08_guix_home.tex", 8, None),
        ("chapters/ch09_anatomy_of_package.tex", 9, None),
        ("chapters/ch10_phases_and_gexp.tex", 10, None),
        ("chapters/ch11_custom_channels.tex", 11, None),
        ("chapters/ch12_guix_pack.tex", 12, None),
        ("chapters/ch13_domain_impact_and_nonguix.tex", 13, None),
        ("backmatter/appendix_cheatsheet.tex", None, "A"),
        ("backmatter/appendix_troubleshooting.tex", None, "B")
    ]

    combined_md = """---
title: "The Joy of Guix: Or How I Learned to Stop Worrying and Love the Parentheses"
subtitle: "A Practical, Sarcastic, and Deeply Technical Guide to Functional Computing"
author: "Sudheer K. Mohammed"
rights: "GNU General Public License v3 or later"
language: "en"
---

"""

    for path, ch_num, app_letter in book_order:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if "dedication.tex" in path:
                md_chunk = """## Dedication

> *Dedicated to everyone who ever ran `sudo apt-get dist-upgrade` at 4:58 PM on a Friday and spent the entire weekend staring at a broken X server and crying into an unbootable kernel.*
>
> *To all the developers whose software "works on my machine" and immediately bursts into flames on anyone else's.*
>
> *And to the humble parenthesis `()`, without which this entire universe would dissolve into an unstructured chaos of arbitrary YAML indents.*

**Colophon**  
This book was typeset with LaTeX using `pdflatex`. The code examples were validated against GNU Guix on GNU/Linux. No global states, mutable `/usr/lib` symlinks, or Python virtualenvs were harmed in the making of this manuscript. All builds are bit-for-bit reproducible, give or take cosmic rays.
"""
            else:
                md_chunk = convert_latex_chapter(content, chapter_num=ch_num, appendix_letter=app_letter)

            combined_md += f"\n\n{md_chunk}\n\n"

    with open("the_joy_of_guix.md", "w", encoding="utf-8") as f:
        f.write(combined_md)
    print("Generated the_joy_of_guix.md successfully.")

    # Call pandoc to create epub
    cmd = [
        "pandoc",
        "the_joy_of_guix.md",
        "-o", "the_joy_of_guix.epub",
        "--epub-cover-image=images/book_cover.jpg",
        "--toc",
        "--toc-depth=2",
        "--highlight-style=breezedark"
    ]
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print("Successfully generated the_joy_of_guix.epub!")
    else:
        print("Pandoc error:", res.stderr)

if __name__ == "__main__":
    build()
