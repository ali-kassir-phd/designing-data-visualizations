---
name: designing-data-visualizations
description: Principles for designing clear, honest, professional data visualizations. Use this skill whenever you create, choose, critique, or fix any chart, plot, graph, figure, map, or dashboard visual, in any library or language (matplotlib, seaborn, ggplot2, plotly, Altair/Vega-Lite, D3, Observable, Excel-style charts, etc.). That includes picking a chart type for some data, choosing colors or palettes, plotting distributions, proportions, time series, trends, maps, or uncertainty/error bars, preparing figures for papers, reports, slides, or social media, writing figure captions, reviewing someone's figure, or deciding how to tell a story with several figures. Use it even when the user just says "plot this", "visualize this data", "make a graph", or "why does my chart look bad".
license: CC-BY-NC-4.0 (text) and MIT (scripts). See LICENSE and LICENSE-CODE.
---

# Designing Data Visualizations

Core position: a figure must **first convey the data accurately**, never
misleading or distorting, and **then look good**, because good aesthetics
strengthen the message and distracting design weakens it.

The guidance is software-agnostic. Apply it in whatever tool the user is using.

## How to use this skill

This file holds the workflow, the core rules, and the final checklist. The
detail lives in `references/`. Each workflow step below names the file (and
section) to read when you reach that step.

- **Read reference files one at a time, in full, with your file-reading tool**
  (e.g. `Read`). Don't concatenate several files in one shell command
  (`cat a.md b.md c.md`). Long combined output gets truncated, and you'll
  silently miss most of what you asked for.
- If a read does come back truncated or saved to a separate file, open the
  saved file before moving on. Don't proceed on a preview.
- Grep is for finding a section, not a substitute for reading it. Once you find
  the section you need, read the whole section.
- Reading a reference file costs far less than redoing a figure. When a step
  applies to your figure, read its file.

## Three levels of failure

Use this vocabulary when critiquing figures, your own included:
- **wrong**: mathematically incorrect (for example bars not starting at zero, a
  pie whose slices sum to more than 100%, a log axis with bars from 0, an axis
  with no scale).
- **bad**: a perception problem: unclear, confusing, overly complex, or
  deceiving (for example rainbow color scales, stacked histograms, unlabeled
  error bars, inconsistent panel scales).
- **ugly**: an aesthetic problem, though the figure is still informative (for
  example clashing colors, an overbearing grid, mixed fonts, rotated labels).

Always eliminate *wrong*, then *bad*, then work on *ugly*.

## Workflow for every figure

1. **Name the message.** What should the reader conclude, in one sentence? Who
   is the audience (experts, executives, the general public) and what is the
   medium (paper, slide, web, social post, print)? A figure without a point
   should not exist yet. For several figures, a talk, or a report → read
   `references/storytelling.md`.
2. **Classify the variables** (quantitative continuous/discrete, categorical
   ordered/unordered, date/time, text) and decide **which variable goes on
   which aesthetic** (position, color, size, shape, line type). Position is the
   most accurate channel, so put the most important comparison there. → read
   `references/foundations.md` §1–4.
3. **Pick the chart type by the message**, not by the data types (table
   below). → read the topic file for that message (the Reference column of the
   chart chooser). If unsure, read `references/chart-chooser.md` first.
4. **Get the scales right**: zero baselines for bars and areas, log scales for
   ratios and multi-order-of-magnitude data, a 1:1 aspect ratio when both axes
   share units, the same scales across small-multiple panels. → read
   `references/foundations.md` §5–7 and `references/figure-design.md` §1.
5. **Choose color deliberately**: decide whether color is distinguishing,
   representing values, or highlighting. Use a CVD-safe palette and run
   `scripts/check_palette.py` on it. → read `references/color.md` in full.
6. **Design for clarity**: proportional ink, overplotting, sensible ordering,
   light minimal grid, filled shapes, no 3D. → read
   `references/figure-design.md` §1–2 and `references/figure-polish.md` §4–8.
   For small multiples or multi-panel figures, also read
   `references/figure-design.md` §5–6.
7. **Label and annotate**: follow "Labels, legends, and annotations" below.
   One title that states the point (in the caption *or* in the graphic, never
   both), axis titles with units, the data source, and an explanation of error
   bars and any non-obvious choice. → read `references/figure-design.md` §3–4
   and `references/figure-polish.md` §1–2. If the figure shows uncertainty,
   read `references/uncertainty.md`.
8. **Render, then inspect the image yourself** at the real output size (text is
   almost always too small) and at thumbnail size. Look for overlapping text,
   clipped labels, and misplaced leader lines. Re-read every claim in the title
   and annotations against the plotted numbers. **Repeat after every change,
   including the last one**: an unchecked final edit is where new collisions
   slip in. → read `references/figure-polish.md` §6.
9. **Keep it reproducible**: script everything, set seeds for jitter and
   sampling, export vector PDF/SVG or PNG (never JPEG for charts). → read
   `references/workflow-and-formats.md`.

When the user just wants a quick plot, still apply these defaults silently.
Don't lecture. When reviewing a figure, report problems ranked
wrong → bad → ugly, each with a concrete fix.

## Chart chooser (by message)

| Message | Good defaults | Avoid / caution | Reference |
|---|---|---|---|
| **Amounts** per category | sorted bars (horizontal if labels are long); dot plot if zero isn't meaningful; grouped bars or small multiples for two factors; heatmap for many × many | alphabetical order, rotated labels, truncated bars, stacking non-additive values | `amounts.md` |
| **Distribution** (one) | histogram (try several bin widths), density (check tails), ECDF/q-q for precision | default bins unchecked, density spilling into impossible values | `distributions.md` |
| **Distributions** (several) | overlapping densities (few), boxplots/violins/sina (many groups), ridgelines (very many or over time) | stacked or overlapping histograms, mean ± error bars as "distribution" | `distributions.md` |
| **Proportions** | pie (one set, few parts, simple fractions), side-by-side bars (precise comparison), stacked bars (two parts over time), stacked densities, part-vs-whole panels | pies across many conditions, many-segment stacks with floating baselines | `proportions.md` |
| **Nested proportions** | mosaic (orthogonal factors), treemap (hierarchy), parallel sets (3+ factors) | pies summing to more than 100%, overlapping categories shown as separate bars | `proportions.md` |
| **Association** of quantities | scatter (+ color by group), scatterplot matrix, correlogram (sized circles), PCA | bubble size for key comparisons, correlograms without raw data | `associations.md` |
| **Paired** measurements | scatter + x = y line (many cases), slopegraph (few cases, 3+ times) | grid without a diagonal | `associations.md` |
| **Time series / ordered x** | lines with direct end labels; connected scatter for two responses (show direction) | dots-only for several series, legends when labels fit, area fill with nonzero baseline | `time-series-trends.md` |
| **Trends** | LOESS/spline (try settings) or a fitted model; linearize via log axes; detrend; STL decomposition | trusting one smoother's defaults, exponential fits on raw data | `time-series-trends.md` |
| **Geospatial** | equal-area projection, choropleth of densities (4–6 binned classes), cartogram or tile map | Mercator for world comparisons, shrunk insets, non-density choropleths dominated by large empty regions | `geospatial.md` |
| **Uncertainty** | labeled error bars (graded), CIs of differences, quantile dot plots and frequency framing (lay audiences), confidence bands or fitted draws, HOPs (animated) | unlabeled bars, SD/SE confusion, significance judged by overlap | `uncertainty.md` |
| **Many points** | transparency + jitter → 2D/hex bins → contours, panels per group | opaque overplotted clouds, overlaid contour hairballs | `figure-design.md` |

## Non-negotiable rules (the "wrong" and "bad" list)

**Accuracy**
- Bars and filled areas start at **0** on linear axes. Bar length must be
  proportional to the value (*principle of proportional ink*). If zero isn't
  meaningful, use dots, not truncated bars. To show small differences, plot the
  difference itself.
- On **log axes, bars represent ratios and start at 1**. For amounts on a log
  axis, use dots with labels next to them.
- **Ratios on log scales.** Label log axes with the original values
  (1, 10, 100). If you show transformed values, state the base.
- Both axes in the same units → **equal aspect ratio**. Paired data →
  **x = y line**.
- Stack only quantities whose **sum is meaningful** (counts, totals), never
  medians, means, or rates.
- Pie slices and nested proportions must **sum to 100% without double
  counting**.
- **Small multiples share axis scales.** If they truly can't, say so in the
  caption.
- Density estimates must **not extend into impossible values** (negative ages,
  more than 100%).
- Don't rescale map insets (for example shrinking Alaska). Use equal-area
  projections when area matters.

**Perception**
- **No rainbow/jet scales** for continuous data. Use perceptually uniform,
  monotonic-lightness scales (viridis family, single-hue, ColorBrewer
  sequential). Use diverging scales only around a meaningful midpoint, with a
  light center and balanced arms.
- **Qualitative color: about 3–5 categories, 8 at most.** Beyond that, label
  directly or group.
- **Avoid red–green contrasts** and test palettes with a CVD simulator (about
  8% of men have a CVD). Never rely on color alone (see "Labels, legends, and
  annotations").
- **Order matters**: sort unordered categories by value. Keep ordered categories
  in their natural order.
- **Every error bar must say what it shows** (SD, SE, or which CI). Error bars
  show uncertainty of estimates, not spread of data.
- **No gratuitous 3D**, ever. Avoid 3D position scales in static figures.
- **Simplify for the audience** ("a figure for the generals"). Drop dimensions
  that are tangential to the story.

**Aesthetics and polish**
- **Text is almost always too small.** Size text for the final display size and
  check a scaled-down view.
- Prefer **horizontal text** over rotated labels, **filled shapes** over outlines, **solid points** over open symbols, and
  **light, minimal grids** perpendicular to the key variable over heavy frames
  and grids. Don't strip context so far that marks float.
- Avoid **large areas of saturated color** and color used only for decoration.
- **One title**: as the first sentence of the caption (documents) or inside the
  graphic (stand-alone), stating the point. **Axis titles with units.**
- **Consistent visual language** across panels and figures (same colors and order
  for the same groups), **aligned** panels, unobtrusive panel letters. Still,
  **vary chart types between different analyses** so they don't blur together.

## Labels, legends, and annotations

These rules are the ones most often skipped, so they live here rather than only
in the reference files.

**Legends and direct labels**
- **Design figures so they don't need a legend.** Put the name next to the data:
  at the right end of each line, beside or inside each group, on each density
  curve. Moving the legend's content into the caption is not the same thing.
- If you keep a legend, **order its entries to match the visual order of the
  data** (top to bottom at the line ends, for example), not alphabetically.
- One variable mapped to two aesthetics gets **one** legend element. If color
  repeats an axis variable, integrate the color bar into that axis.
- With many items, **label a meaningful subset** (extremes, the cases named in
  the text), not everything.

**Redundant coding**
- **Never let color be the only carrier of key information.** Pair color with
  shape, position, or a direct label, so the figure survives color-vision
  deficiency and grayscale printing.
- Give the **most distinct colors to the groups that overlap in space**.
- Draw labels and outlines in a **darker shade of the fill's hue**. Thin colored
  text looks lighter than a filled area of the same color.

**Collision-free annotation**
- **No text may overlap other text, data marks, lines, or panel edges.**
  Automatic placement often fails, so check the rendered image, not the code.
- Leader lines must point to the exact mark they describe and must not cross
  other labels.
- When space is tight, move the label (offset with a leader line, put it in a
  margin column, or drop it) rather than shrinking text below a legible size.

**Accurate claims**
- Compute every number in a title, subtitle, or annotation from the data you
  plotted, in the script, not from memory.
- **Check that the words match the magnitude.** "Barely changed" for a fall
  from 7.5 to 6.1, or "tripled" for a 2.4× rise, is a wrong claim even if the
  numbers next to it are right.
- Keep causal language out unless the data support it. If an explanation comes
  from outside knowledge, say so or cite it.

## Sensible defaults when nothing else is specified

- **Palette**: Okabe–Ito for categories (`#E69F00 #56B4E9 #009E73 #F0E442
  #0072B2 #D55E00 #CC79A7 #000000`). Viridis (or a single-hue ramp) for
  sequential. ColorBrewer BrBG/PuOr/PiYG or blue–red for diverging. Gray plus
  one or two accent colors for highlighting.
- **Background**: white with a light gray major grid only (or only along the
  value axis), no panel frame needed, no minor grid. A light gray panel
  background is fine for small multiples.
- **Fonts**: one family. Tick labels and axis titles clearly readable at final
  size (for print at column width, roughly 8–12 pt equivalents; for slides,
  much larger).
- **Points**: solid, with slight transparency if there are many. Use **jitter**
  only when values are discretized.
- **Lines**: label directly at the right end. Drop point markers on dense
  series.
- **Export**: vector PDF/SVG for print, PNG for web, fonts embedded, sized at
  final dimensions.

## Before you hand over a figure: checklist

1. Does the title (or caption opening) state the point? Is there exactly one
   title?
2. Is the chart type right for the message? Could a simpler chart say it
   better?
3. Do bars and areas start at 0 (linear) or 1 (log ratios)? Are axes, units,
   and log bases labeled?
4. Are categories ordered meaningfully? Does the legend match the visual
   order, or have you replaced it with direct labels?
5. Is the color purpose clear? Is the palette CVD-safe? Is information also
   carried by shape, position, or labels? No rainbow?
6. Overplotting handled? Distribution parameters (bins, bandwidth, smoother
   settings) sanity-checked?
7. Uncertainty shown where it matters, and are error bars explained?
8. Small multiples on shared scales, panels aligned, consistent colors?
9. Text legible at the actual output size? No frames, heavy grids, outlines,
   or 3D where they're not needed?
10. Have you **looked at the rendered image** (full size and thumbnail)
    **after your final change**, and confirmed that no text overlaps other
    text, marks, or lines, and that every leader line points to the right mark?
11. Is every number and every descriptive word in the title and annotations
    **verified against the plotted data**? Any causal claim supported or
    attributed?
12. Reproducible script, seeds set, appropriate file format?

## Reference files

Read one file at a time, in full, with your file-reading tool (see "How to use
this skill"). Longer files start with a table of contents.

| File | Read when |
|---|---|
| `references/foundations.md` | mapping variables to aesthetics; axes, log/sqrt scales, aspect ratio, polar coordinates |
| `references/color.md` | choosing any palette; CVD; rainbow problems; highlighting |
| `references/chart-chooser.md` | unsure which chart type fits |
| `references/amounts.md` | bars, grouped/stacked bars, dot plots, heatmaps |
| `references/distributions.md` | histograms, densities, ECDF, q-q, boxplots, violins, sina, ridgelines |
| `references/proportions.md` | pies vs. bars, stacked densities, mosaic, treemap, parallel sets |
| `references/associations.md` | scatter, bubble, correlogram, PCA, paired data, slopegraphs |
| `references/time-series-trends.md` | line charts, connected scatter, smoothing, fits, detrending, decomposition |
| `references/geospatial.md` | projections, map layers, choropleths, cartograms |
| `references/uncertainty.md` | error bars, CIs, Bayesian posteriors, confidence bands, quantile dots, HOPs |
| `references/figure-design.md` | proportional ink, overplotting, redundant coding, legends, small multiples, compound figures |
| `references/figure-polish.md` | titles, captions, tables, grids and context, text size, line drawings, 3D |
| `references/workflow-and-formats.md` | scripting/reproducibility, software choice, themes, file formats |
| `references/storytelling.md` | multi-figure narratives, presentations, simplifying for an audience |
| `references/tools-and-reading.md` | library equivalents in R/Python/JS; further reading |

## Script

`scripts/check_palette.py`: standard-library Python. It simulates
deuteranopia, protanopia, and tritanopia (plus grayscale) for a list of hex
colors and checks qualitative distinctness (CIEDE2000), sequential lightness
monotonicity, and diverging balance.

```bash
python scripts/check_palette.py --type qualitative "#E69F00" "#56B4E9" "#009E73"
python scripts/check_palette.py --type sequential  "#440154" "#3b528b" "#21918c" "#5ec962" "#fde725"
python scripts/check_palette.py --type diverging   "#8c510a" "#d8b365" "#f5f5f5" "#5ab4ac" "#01665e" --json
```

A palette that passes still needs a look at the finished figure: thin lines and
small points make colors harder to distinguish.

