#!/usr/bin/env python3
import re
import os
import subprocess

def latex_to_md(tex_content):
    # Remove comments
    lines = []
    in_listing = False
    listing_lang = "scheme"
    
    tex_content = re.sub(r'\\begin\{titlepage\}.*?\\end\{titlepage\}', '', tex_content, flags=re.DOTALL)
    tex_content = re.sub(r'\\cleardoublepage', '', tex_content)
    tex_content = re.sub(r'\\clearpage', '', tex_content)
    
    # Replace epigraph
    def replace_epigraph(m):
        quote = m.group(1).replace('\\"', '"').replace("\\'", "'")
        author = m.group(2).replace('\\---', '—').replace('---', '—')
        return f"\n> *\"{quote}\"*\n> \n> — **{author}**\n\n"
    tex_content = re.sub(r'\\epigraph\{([^}]+)\}\{([^}]+)\}', replace_epigraph, tex_content)

    # Chapters and sections
    tex_content = re.sub(r'\\chapter\*?\{([^}]+)\}', r'# \1', tex_content)
    tex_content = re.sub(r'\\section\*?\{([^}]+)\}', r'## \1', tex_content)
    tex_content = re.sub(r'\\subsection\*?\{([^}]+)\}', r'### \1', tex_content)
    tex_content = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'#### \1', tex_content)
    tex_content = re.sub(r'\\label\{[^}]+\}', '', tex_content)
    tex_content = re.sub(r'\\addcontentsline\{[^}]+\}\{[^}]+\}\{[^}]+\}', '', tex_content)

    # Replace custom callout boxes
    def replace_callout(box_type, emoji, title_prefix):
        pattern = r'\\begin\{' + box_type + r'\}(?:\[([^\]]*)\])?(.*?)\\end\{' + box_type + r'\}'
        def repl(m):
            title = m.group(1) or ""
            body = m.group(2).strip()
            header = f"> ### {emoji} {title_prefix}: {title}\n" if title else f"> ### {emoji} {title_prefix}\n"
            body_quoted = "\n".join([f"> {line}" for line in body.split("\n")])
            return f"\n{header}>\n{body_quoted}\n\n"
        return pattern, repl

    for box, emoji, name in [
        ('tearsbox', '😭', 'Tears of the Imperative Developer'),
        ('alchemybox', '✨', 'Functional Alchemy & Arcana'),
        ('footgunbox', '⚠️', 'Caution: Footgun Detected'),
        ('protipbox', '💡', 'Guix Wizard Pro-Tip'),
        ('tcolorbox', '📦', 'Note')
    ]:
        pat, repl = replace_callout(box, emoji, name)
        tex_content = re.sub(pat, repl, tex_content, flags=re.DOTALL)

    # Listings / Code blocks
    def replace_listing(m):
        opts = m.group(1) or ""
        code = m.group(2)
        lang = "scheme"
        if "guixcli" in opts or "bash" in opts or "sh" in opts:
            lang = "bash"
        elif "scheme" in opts:
            lang = "scheme"
        return f"\n```{lang}\n{code.strip()}\n```\n"
    tex_content = re.sub(r'\\begin\{lstlisting\}(?:\[([^\]]*)\])?(.*?)\\end\{lstlisting\}', replace_listing, tex_content, flags=re.DOTALL)

    # Figures and images
    def replace_figure(m):
        content = m.group(1)
        img_match = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', content)
        cap_match = re.search(r'\\caption\*?\{([^}]+)\}', content)
        if img_match:
            img_path = img_match.group(1)
            caption = cap_match.group(1) if cap_match else ""
            caption = re.sub(r'\\textit\{([^}]+)\}', r'\1', caption)
            caption = re.sub(r'\\texttt\{([^}]+)\}', r'`\1`', caption)
            caption = re.sub(r'\\guixcmd\{([^}]+)\}', r'`\1`', caption)
            return f"\n\n![{caption}]({img_path})\n\n*{caption}*\n\n"
        return ""
    tex_content = re.sub(r'\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}', replace_figure, tex_content, flags=re.DOTALL)

    # Inline formatting
    tex_content = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', tex_content)
    tex_content = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', tex_content)
    tex_content = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', tex_content)
    tex_content = re.sub(r'\\texttt\{([^}]+)\}', r'`\1`', tex_content)
    tex_content = re.sub(r'\\guixcmd\{([^}]+)\}', r'`\1`', tex_content)
    tex_content = re.sub(r'\\storepath\{([^}]+)\}', r'`\1`', tex_content)
    tex_content = re.sub(r'\\code\{([^}]+)\}', r'`\1`', tex_content)
    tex_content = re.sub(r'\\url\{([^}]+)\}', r'<\1>', tex_content)

    # Lists
    tex_content = re.sub(r'\\begin\{itemize\}', '', tex_content)
    tex_content = re.sub(r'\\end\{itemize\}', '', tex_content)
    tex_content = re.sub(r'\\begin\{enumerate\}', '', tex_content)
    tex_content = re.sub(r'\\end\{enumerate\}', '', tex_content)
    tex_content = re.sub(r'\\item\s*', r'- ', tex_content)

    # Clean remaining LaTeX commands & special chars
    tex_content = tex_content.replace(r'\%', '%')
    tex_content = tex_content.replace(r'\&', '&')
    tex_content = tex_content.replace(r'\_', '_')
    tex_content = tex_content.replace(r'\#', '#')
    tex_content = tex_content.replace(r'\$', '$')
    tex_content = tex_content.replace(r'\textasciitilde', '~')
    tex_content = tex_content.replace(r'\textasciicircum', '^')
    tex_content = tex_content.replace(r'---', '—')
    tex_content = tex_content.replace(r'--', '–')
    tex_content = tex_content.replace('``', '"')
    tex_content = tex_content.replace("''", '"')
    tex_content = re.sub(r'\\noindent', '', tex_content)
    tex_content = re.sub(r'\\vspace\*?\{[^}]+\}', '', tex_content)
    tex_content = re.sub(r'\\rule\{[^}]+\}\{[^}]+\}', '---', tex_content)

    return tex_content

def build():
    book_order = [
        "frontmatter/dedication.tex",
        "frontmatter/preface.tex",
        "chapters/ch01_curse_of_fhs.tex",
        "chapters/ch02_cli_daily_life.tex",
        "chapters/ch03_channels_time_travel.tex",
        "chapters/ch04_guix_shell.tex",
        "chapters/ch05_manifests.tex",
        "chapters/ch06_guix_system.tex",
        "chapters/ch07_shepherd.tex",
        "chapters/ch08_guix_home.tex",
        "chapters/ch09_anatomy_of_package.tex",
        "chapters/ch10_phases_and_gexp.tex",
        "chapters/ch11_custom_channels.tex",
        "chapters/ch12_domain_impact_and_nonguix.tex",
        "backmatter/appendix_cheatsheet.tex",
        "backmatter/appendix_troubleshooting.tex"
    ]

    combined_md = """---
title: "The Joy of Guix: Or How I Learned to Stop Worrying and Love the Parentheses"
subtitle: "A Practical, Sarcastic, and Deeply Technical Guide to Functional Computing"
author: "Sudheer K. Mohammed"
rights: "GNU General Public License v3 or later"
language: "en"
---

"""

    for path in book_order:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                md = latex_to_md(content)
                combined_md += f"\n\n{md}\n\n"

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
