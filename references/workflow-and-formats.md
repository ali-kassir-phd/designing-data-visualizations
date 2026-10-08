# Workflow, reproducibility, software, and file formats

Use this when writing plotting code, setting up a figure pipeline, or exporting
figures.

## Contents
1. Automate: figures should come out of the pipeline finished
2. Reproducible vs. repeatable figures
3. Exploration vs. presentation
4. Separate content from design (themes)
5. Choosing software
6. Bitmap vs. vector formats
7. Lossless vs. lossy compression
8. Converting formats and archiving originals
9. Export checklist

---

## 1. Automate: figures should come out of the pipeline finished

- Generate figures **programmatically as part of an automated analysis
  pipeline**, so they come out **ready to print**, with **no manual
  post-processing**.
- Why manual touch-ups (exporting a draft and fixing it in Illustrator or
  Photoshop) cause trouble:
  1. The figure becomes **irreproducible**. Others can't regenerate it or verify
     changes such as relabeling.
  2. Manual steps make you **reluctant to redo** figures, so reasonable change
     requests get ignored, or stale figures are reused after the data changed.
  3. You **forget** what you did, and future figures won't match.
- **Interactive point-and-click plotting programs** (including spreadsheet
  charting such as Excel) build manual steps into the process and are not
  recommended for figure preparation.
- Hand-drawn or hand-finished figures can still be beautiful and distinctive, and
  are fine as one-off art. Avoid them in **routine analysis and scientific
  publication**, where figures get regenerated many times (new data, a changed
  analysis, late-stage revisions).
- If you must work interactively, **keep careful notes** of every transformation
  and tweak.

## 2. Reproducible vs. repeatable figures

- **Reproducible**: given the plotted data and exactly specified transformations,
  someone else can make a figure that conveys the same message (fonts and colors
  may differ).
- **Repeatable**: the exact same figure, down to the pixel, can be regenerated
  from the raw data. **Random elements (jitter, sampled draws, HOP frames) need
  a fixed, recorded random seed** (and a specified RNG).
- Scripted figures are repeatable for anyone with the scripts, language, and
  library versions. **When writing plotting code, set seeds for jitter or random
  sampling, and keep the data loading → transformation → plot chain in code.**

## 3. Exploration vs. presentation

- **Exploration**: speed matters most. Quickly try many chart types,
  transformations, and subsets (scatter → densities → boxplots → heatmap). Looks
  don't matter (missing labels are fine). Good tools let you **swap which
  variables map to which aesthetics** within one consistent framework (a grammar
  of graphics). Tools organized as a separate API per chart type slow
  exploration.
- **Presentation**: once you know the message, produce a polished,
  publication-quality figure. Options: finish in the same tool, switch to a tool
  with finer control, post-process manually (discouraged for routine work), or
  redraw by hand (for special, artistic pieces).

## 4. Separate content from design (themes)

- **Content** = data, transformations, aesthetic mappings, scales, axis ranges,
  chart type. **Design** = colors, fonts, symbol shapes and sizes, legend,
  tick and title placement, grid and background.
- Settle content first through exploration, then **apply a predefined theme or
  style** for a consistent look across a body of work (paper, report, brand).
  Examples: ggplot2 themes, matplotlib style sheets / rcParams, Vega-Lite config,
  Plotly templates.
- This lets data scientists focus on data and designers on visual language, as
  in publishing, where writers supply content and designers supply layout.

## 5. Choosing software

- **The best visualization software is the one that lets you make the figures
  you need** without excessive effort. Switching has a real learning cost.
- Evaluate tools on:
  1. **Reproducibility/repeatability**: are all steps captured in code?
  2. **Speed of exploration**: can you rapidly change mappings and chart types?
  3. **Separation of content and design**: themes or styles you can swap.
- Different tools for exploration and final presentation is a legitimate choice.
- These principles are software-agnostic: everything here can be made with
  ggplot2 (R), and equally with matplotlib/seaborn/plotnine (Python),
  Vega-Lite/Altair, Plotly, D3, Observable Plot, and others.

## 6. Bitmap vs. vector formats

| Format | Type | Use |
|---|---|---|
| **PDF** | vector | general purpose, high-quality publication files (preferred whenever possible) |
| EPS | vector | outdated, use PDF |
| **SVG** | vector | online / web use |
| **PNG** | bitmap (lossless) | line drawings, charts, text, screenshots; online documents |
| **JPEG** | bitmap (lossy) | photographs only; last resort for charts if PNG is too large |
| TIFF | bitmap | print production, accurate color reproduction |
| RAW | bitmap | digital photography, needs post-processing |
| GIF | bitmap | outdated for static figures; OK for animations |

- **Vector** formats store geometric instructions ("a line from here to there")
  that are re-rendered on display. They are **resolution-independent**: they
  zoom without pixelation.
  - Downside 1: **rendering can differ between programs and machines**,
    especially **font substitution** when a font is missing. Embed or outline
    fonts in PDFs.
  - Downside 2: **huge, slow files for complex figures** (millions of points, each
    stored and drawn even when hidden). For very large scatterplots, rasterize
    the point layer or use a bitmap. Simple figures are often *smaller* as
    vectors.
- **Bitmap (raster)** formats store a pixel grid. They always look the same but
  pixelate when enlarged. Export at sufficient resolution for the output (for
  example ≥ 300 dpi at final print size, or 2× pixel density for high-DPI
  screens).
- Recommended default: **PDF** for publication-quality files whenever
  possible, **PNG** where bitmaps are required (online), **JPEG** only as a last
  resort if PNGs are too large.

## 7. Lossless vs. lossy compression

- **Lossless** (PNG, TIFF): pixel-identical to the original. It compresses
  **large uniform-color areas** very efficiently, which is exactly what charts,
  line art, and text contain.
- **Lossy** (JPEG): discards detail the eye barely notices. Excellent for
  **photographs** (gradients), but creates **visible artifacts around sharp edges
  and text**, which is exactly what charts contain. Even subtle artifacts can
  cause trouble in print production.
- **Never use JPEG for data visualizations, line drawings, text, or
  screenshots.** Use PNG or TIFF, even for mixed photo + text images. Worst case
  with PNG is a large file. Worst case with JPEG is an ugly result.

## 8. Converting formats and archiving originals

- Converting can only **lose** information, never recover it. Vector → bitmap
  loses resolution independence. Putting a JPEG inside a PDF doesn't make it
  vector. JPEG → PNG doesn't remove JPEG artifacts.
- **Store the master in the highest-fidelity format** (vector PDF/SVG, or a
  high-resolution PNG) and **derive** downscaled or bitmap versions as needed.
  For photos, keep originals uncompressed or minimally compressed at full
  resolution.

## 9. Export checklist

- [ ] Figure generated entirely by script, with a seed set for any randomness?
- [ ] Theme or style applied consistently across all figures in the document?
- [ ] Vector (PDF/SVG) for print and publication, with fonts embedded? PNG for
      web/bitmap needs? No JPEG for charts?
- [ ] Huge point clouds rasterized or binned so files stay manageable?
- [ ] Exported at the final physical size (so text sizes are right) and at
      sufficient resolution?
- [ ] Master file archived in its highest-fidelity form?
