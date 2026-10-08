# Figure design II: titles, captions, tables, context, text size, fills, 3D

## Contents
1. Figure titles and captions
2. Axis and legend titles
3. Tables
4. Balance data ink and context ink
5. Background grids and reference lines
6. Text size: use larger axis labels
7. Prefer filled shapes to line drawings
8. Don't go 3D
9. Polish checklist

---

## 1. Figure titles and captions

- **Every figure needs a title** that says what the figure is about and **what
  point it makes**.
- **A figure has exactly one title.** It goes in one of two places:
  - **Caption-block style** (books, papers, reports with a caption under each
    figure): **the title is the first element of the caption**. Do *not* also
    put a title on top of the plot.
  - **Integrated style** (stand-alone infographics, social media, web posts,
    slides with no caption): title, subtitle, and data source go **inside the
    figure display**.
- **Start the caption with a title, not a description.** Write "Commute time and
  income: lower-income districts have longer commutes.", not "This figure shows
  how commute time relates to income…". A title can be a phrase or a short
  assertive sentence ("Lower-income districts have longer commutes").
- After the title, the caption gives context: what is plotted, what marks and
  error bars mean, any non-obvious design choices (different axis scales, "lines
  are a guide to the eye"), and the **data source**.

## 2. Axis and legend titles

- Axes and legends need titles (colloquially "axis labels") that explain what the
  values are. **Quantitative variables should include units**: "body mass (g)",
  "head length (mm)". Categorical variables don't need units.
- **Omit a title only when the labels are self-explanatory**: "female/male" needs
  no "sex" title, country names need no "country", years need no "year".
- **Don't over-omit.** Leaving the y axis untitled and expecting the plot title to
  explain it forces readers to guess, which is **bad**. Even 95% certainty leaves
  a nagging doubt. Don't make readers guess.
- **Don't over-label** either. "company" above four famous company names, or
  "time (years AD)" for recent years, is **ugly** redundancy.
- Sometimes **the entire axis can go** (pie charts, treemaps, mosaic plots, or bar
  charts with value labels on the bars). Removing the axis signals that the
  qualitative pattern matters more than exact values.

## 3. Tables

Most software defaults (including most built-in word-processor table styles)
break basic table rules. Rules:
- **No vertical lines.**
- **No horizontal lines between data rows.** Lines separating the header from
  the body, or framing the whole table, are fine.
- **Text columns left-aligned.**
- **Number columns right-aligned, with the same number of decimal places
  throughout.**
- **Single-character columns centered.**
- **Header fields aligned like their data** (left over text, right over numbers).
- If rows need visual separation (very wide or sparse tables), use **subtle
  alternating row shading**, not rule lines or harsh dark/light stripes. A
  stronger color can set off the header.
- **Caption placement**: **figures get captions below** (people look at the
  graphic first, then read). **Tables get captions above** (tables are read top
  to bottom like text).

## 4. Balance data ink and context ink

- **Data ink**: points, bars, lines, filled areas. **Non-data / context ink**:
  axes, ticks, labels, titles, legends, grids, frames, annotations.
- Tufte's advice is to maximize the data–ink ratio "**within reason**", and the
  "within reason" part is often forgotten. Read it as "remove clutter and aim
  for clean designs", **not** "delete all non-data ink". Both extremes produce
  ugly or bad figures, and a wide range of designs in between is fine.
- **Too much context ink**: frames around the figure, the plot panel, *and* the
  legend, plus a dense, dark major-and-minor grid. Fix: drop unneeded frames,
  drop minor grid lines, **draw major grid lines in light gray** so the data
  stands out.
- **Too little context ink**: faint tick labels and titles, points floating in
  space, legend points that look like data points, no separation between legend
  and plot. Small multiples suffer especially: bars float with no baseline and
  facets blur together. Fix: a **light gray panel background plus thin horizontal
  grid lines** per facet to anchor bars and delimit panels.
- **Open grid (no axis lines or frame)** vs. **framed panel**: both are fine. An
  open grid suggests the data range extends beyond the limits. A frame clearly
  separates the legend from the plot.

## 5. Background grids and reference lines

- There's no single best grid. Choose the **specific guide lines that are
  informative** for this plot and show only those.
- **Gray background with white grid** (the ggplot2 default): it unifies the plot
  as one visual entity (useful for small multiples), but a dense major+minor grid
  can overpower the data, and gray boxes appear in the legend keys. If you use a
  gray background:
  - match its darkness to the surrounding typography and the amount of
    foreground ink, so figures don't appear as dark boxes in light text,
  - use **darker and more saturated** foreground colors than you would on white.
- **No grid at all** (axis lines only): lines float and endpoints are hard to read
  against the axis, which is **bad** for line charts like indexed prices.
- **Minimum**: add **one meaningful reference line**, for example y = 100 for an
  index, y = 0 for changes, y = 1 for ratios.
- **Minimal grid**: **grid lines perpendicular to the direction in which the key
  values vary**. Horizontal lines for y-values over time, vertical lines for
  horizontal bars. Major ticks only. Axis lines can then be omitted or made thin.
- **Full x+y grids** suit scatterplots with no primary axis of interest. With a
  full grid, axis lines are generally unnecessary.
- **White grid lines over bars** (Tufte style) split bars into equal segments.
  Research suggests this can help judge length, but bars can look like they're
  falling apart. Tune bar width, gaps, and line thickness if you use it. **Don't
  put value labels just outside bar ends**, where they visually extend the bars.
- **Paired data**: prefer a **diagonal x = y line over a grid**. The diagonal shows
  immediately which cases are above or below parity. Grid + diagonal gets busy.
- **Branding**: a consistent background and grid style can give a publication a
  recognizable identity. That's a legitimate reason to choose one.
- Recommended default: **minimal light-gray grid on white**.
  White is neutral on paper and supports nearly any foreground color.

## 6. Text size: use larger axis labels

*The single most important rule in this skill:* **axis titles, tick
labels, legend text, and annotations are almost always too small.** Plotting
software defaults are poor. Using the defaults almost guarantees text that is too
small.

- Text that is too small makes the figure illegible and **unbalanced**. Text and
  marks must fit together.
- Text can also be **too big** relative to the marks. If you enlarge text (for
  example because the figure will be shown small), **enlarge the points and lines
  too** so the figure stays balanced.
- Why this keeps happening: we preview figures **large on high-resolution
  monitors**, where small text looks fine and properly sized text looks
  oversized.
- **Always view figures at their real output size.** Zoom out to 3–5 inches
  (8–13 cm) wide on screen, look from across the room, or shrink to an inch or two
  for thumbnails and multi-panel use. Size text for how the figure will actually
  be seen (print column, slide on a projector, phone screen).

## 7. Prefer filled shapes to line drawings

- **Visualize data with solid, filled shapes rather than outlines** whenever
  possible. Filled shapes are seen as coherent objects, cause fewer visual
  artifacts and optical illusions, and convey amount more directly. (This never
  overrides proportional ink.)
- Line drawings come from hand-drawn, black-and-white printing (hatching,
  stippling, dashes). Many tools still default to them.
- **Histograms and bars**: outlined bars, especially with gaps, make it unclear
  what is inside and what is outside a bar. **Fill bars** with a light color, or
  gray if color is unavailable.
- **Density curves**: dashed or dotted outlines look porous and don't separate the
  area under the curve from the area above. Intersecting outlines make the shapes
  hard to segment. Colored solid lines help a bit. **Partially transparent filled
  areas** work best (transparency keeps each distribution fully visible).
- **Scatterplots**: open or line symbols (circles, triangles, crosses) create
  visual noise and groups don't separate. Use **solid, colored, distinct
  shapes**, which also survive grayscale. The argument that open points help
  with overplotting doesn't outweigh their noise. Use the overplotting
  techniques in `figure-design.md` instead.
- **Boxplots**: give boxes a **light shading** so they stand out from the
  background and adjacent boxes don't create inside/outside illusions. (If you
  don't want emphasis on the middle 50%, don't use a boxplot. Use violins,
  jittered points, or sina plots.)
- Use two shades per hue: a light fill plus a darker outline and text (see
  `figure-design.md` §4).

## 8. Don't go 3D

**Gratuitous 3D** (3D pies, 3D columns, ribbon lines) where the third dimension
encodes no data: **always bad**. Remove it from your vocabulary.
- Projecting 3D onto 2D distorts data, and the visual system can only partly
  correct for it. A tilted pie makes front slices look bigger (25% looks like
  much more). 3D columns look shorter than they are because they stand away from
  the back-wall grid lines. Foreground bars dominate.

**3D position scales** (real x, y, z data, such as a 3D scatterplot): usually
avoid on static 2D media.
- They require two transformations, data → 3D space → 2D image, and the second
  **can't be inverted**: each point on the screen corresponds to a whole line in
  3D. Readers can't tell where points really are. Different viewing angles look
  like different datasets, and without depth cues the plot is uninterpretable.
- **Alternatives**: map the third variable to color, size, or shape (x, y + size
  for a secondary variable), or plot the response against each predictor in
  separate panels.
- **3D bars of a two-way table**: replace them with **small multiples / trellis
  panels** (one panel per group with a shared axis). They are much easier to read
  precisely.

**When 3D is appropriate**
- **Interactive** rotation, or VR/AR, where the viewer can inspect from many
  angles.
- **Slowly rotating animation** (web, talks), since the brain reconstructs 3D well
  from a sequence of views.
- Showing **genuinely 3D objects**, possibly with data mapped onto them: terrain
  relief, protein structures, anatomy. Even then, rotation helps where the medium
  allows it.

## 9. Polish checklist

- [ ] Exactly one title: in the caption (document) **or** in the graphic
      (stand-alone). It states the point.
- [ ] Caption starts with the title, then explains the encodings, any unusual
      choices, and the data source.
- [ ] Axes and legends titled, with units for quantitative variables. No
      redundant titles, no guesswork.
- [ ] Tables: no vertical lines or row rules, correct alignment, consistent
      decimals, caption above.
- [ ] No unnecessary frames. Grid light and minimal, perpendicular to the key
      variable. Meaningful reference lines (0, 1, 100, x = y).
- [ ] Nothing floats: bars anchored to a baseline, facets delimited.
- [ ] Text legible **at the actual output size**. Text and marks balanced.
- [ ] Filled shapes rather than outlines, solid points, lightly shaded boxes,
      transparent density fills.
- [ ] No gratuitous 3D. 3D position only if interactive, animated, or the object
      itself is 3D.
