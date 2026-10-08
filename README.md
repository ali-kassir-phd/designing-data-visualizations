# designing-data-visualizations: an Agent Skill for data visualization

An [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
that teaches AI agents (Claude Code, Claude.ai, and other skill-compatible
agents) to make clear, honest, professional charts. It distills the principles
of Claus O. Wilke's open-access book
**[Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)**
(O'Reilly, 2019) into a chart-selection workflow, rules, checklists, and a
palette checker.

> **Not affiliated with or endorsed by Claus O. Wilke or O'Reilly Media.**
> If you work with data visualization, read the book itself. It's free online,
> and its many before/after figures are the best way to learn this material.

## What's inside

```
designing-data-visualizations/
├── SKILL.md                         # entry point: workflow, chart chooser, core rules, checklist
├── references/
│   ├── foundations.md               # Ch. 1–3: aesthetics, scales, axes, log/sqrt, polar
│   ├── color.md                     # Ch. 4, 19, 20: color scales, pitfalls, CVD
│   ├── chart-chooser.md             # Ch. 5: directory of visualizations
│   ├── amounts.md                   # Ch. 6
│   ├── distributions.md             # Ch. 7–9
│   ├── proportions.md               # Ch. 10–11
│   ├── associations.md              # Ch. 12
│   ├── time-series-trends.md        # Ch. 13–14
│   ├── geospatial.md                # Ch. 15
│   ├── uncertainty.md               # Ch. 16
│   ├── figure-design.md             # Ch. 17, 18, 20, 21
│   ├── figure-polish.md             # Ch. 22–26
│   ├── workflow-and-formats.md      # Preface, Ch. 27–28
│   ├── storytelling.md              # Ch. 29
│   └── tools-and-reading.md         # Ch. 30 + library equivalents (R / Python / JS)
└── scripts/
    └── check_palette.py             # CVD + grayscale palette checker (stdlib only)
```

SKILL.md stays short and always-loaded. The reference files are loaded only
when the task calls for them (progressive disclosure).

## Install

**Claude Code** (available in all your projects):
```bash
git clone https://github.com/ali-kassir-phd/designing-data-visualizations.git ~/.claude/skills/designing-data-visualizations
```
For a single project, clone it into that project's `.claude/skills/` folder instead.

**Claude.ai**: download the repository as a ZIP and upload it under
Settings → Capabilities → Skills.

## Usage

There is nothing to invoke. Once installed, the skill loads automatically
whenever you ask the agent to make, choose, fix, or critique a chart, e.g.:

- "Plot monthly sales by region from `sales.csv` for the board deck."
- "Which chart should I use to compare these five distributions?"
- "Review this figure before I submit the paper."

## Palette checker

```bash
python scripts/check_palette.py --type qualitative "#E69F00" "#56B4E9" "#009E73"
python scripts/check_palette.py --type sequential "#440154" "#3b528b" "#21918c" "#5ec962" "#fde725"
python scripts/check_palette.py --type diverging "#d7191c" "#fdae61" "#ffffbf" "#a6d96a" "#1a9641"   # flags red–green
```

The checker simulates deuteranopia, protanopia, and tritanopia (Machado et al.
2009) plus grayscale. It measures CIEDE2000 color differences and checks
lightness monotonicity and balance.

## License and attribution

### This project
- **Text** (SKILL.md, `references/`, README): **Creative Commons
  Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**. See
  [`LICENSE`](LICENSE).
- **Code** (`scripts/`): **MIT**. See [`LICENSE-CODE`](LICENSE-CODE).

### Source material
*Fundamentals of Data Visualization* © Claus O. Wilke is licensed under
**[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)**. The
book's source repository (https://github.com/clauswilke/dataviz) is under CC
BY-NC-ND 3.0 US.

### How this project relates to the book's license
The book's **NoDerivatives (ND)** term forbids sharing *adapted* versions of
the book's text and figures. The book's **NonCommercial (NC)** term forbids
commercial use. This project is designed to stay clear of both:

1. **Ideas, not expression.** Copyright protects how something is expressed,
   not the underlying ideas, methods, or facts. This skill restates the book's
   *principles* (e.g. "bars should start at zero", "avoid rainbow color scales")
   in **original wording**, reorganized as agent instructions and checklists. It
   does **not** reproduce the book's prose, figures, captions, or datasets. A
   word-overlap check against the full book text was used during writing to
   catch and rewrite accidental verbatim passages. The only remaining overlaps
   are book titles, citations, and short attributed phrases such as the
   "principle of proportional ink" (Bergstrom & West).
2. **Attribution.** The book, its author, its URL, and its license are credited
   here. The skill files themselves contain only the guidance.
3. **NonCommercial preserved.** Even though the text is original, it is licensed
   **NC** out of respect for the author's choice to keep the book
   non-commercial. ND was **not** carried over because it would stop the
   community from improving the skill, which defeats the purpose of open-sourcing
   it.
4. **Factual data reused**: published color values (Okabe–Ito hex codes,
   ColorBrewer names) and the list of image formats are facts, not
   copyrightable expression.

*This is not legal advice.* If you plan to use this skill commercially or
redistribute it in a commercial product, consult a lawyer, and consider asking
Prof. Wilke for permission. Any contributions must also follow the rules
above: no copying of the book's text or figures.

### Contributing
Issues and pull requests are welcome. Please:
- write in your own words, and don't paste text or figures from the book,
- mention in the PR description which part of the book a new rule comes from,
- keep SKILL.md concise and put detail in `references/`.
