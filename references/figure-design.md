# Figure design I: proportional ink, overplotting, redundant coding, multi-panel figures

Titles, captions, data–context
balance, text size, line drawings, and 3D are in `figure-polish.md`. Color
pitfalls are in `color.md`.

## Contents
1. Proportional ink
2. Overlapping points (overplotting)
3. Redundant coding and legends
4. Designing figures without legends
5. Small multiples
6. Compound figures

---

## 1. Proportional ink

**The principle** (Bergstrom & West): *the size of shaded areas must be
proportional to the data values they represent.* Whenever a mark has visible
extent (bars, rectangles, shaded areas, wedges), its extent must agree with its
value. A dot only encodes position, so it has no such constraint. Violations are
especially common in news media and finance.

**Linear axes**
- **Bars on a linear scale must start at 0.** If bars start at an arbitrary value
  (for example $50,000), bar length shows "excess over $50k". Readers perceive
  length, not endpoint, so small differences look huge.
- **Shaded areas under a curve** (area charts) follow the same rule. Shading
  implies that the height from the axis is the value. A stock chart with y
  starting at $110 and shading underneath makes a modest dip look like a
  collapse. A truncated axis is questionable even without shading. With shading
  it is clearly misleading.
- **Want to show small changes?** Then plot the **change itself** explicitly:
  bars of the difference (2015 minus 2010 income, negative bars pointing down
  from 0), or the shaded loss relative to a reference date. That is honest and
  makes the small differences visible.
- If the bars don't need to start at zero to tell the story, use **dots** (see
  `amounts.md`), not truncated bars.

**Log axes**
- On a log axis, zero is infinitely far away. Bars for **amounts** on a log scale
  have arbitrary lengths that depend on where you put the origin, so they are
  misleading. **Use dots instead**, and **put the labels next to the dots**
  rather than on the axis, so no implied bar length forms between label and dot.
- Bars on a log scale **are appropriate for ratios** (for example GDP relative to
  a reference country). **Log-scale bars must start at 1**, the natural midpoint,
  with ratios above 1 going one way and below 1 the other.
- Rule: *linear bars represent amounts and start at 0; log bars represent ratios
  and start at 1.*

**Direct area encodings (pies, treemaps)**
- Pies and treemaps satisfy proportional ink, but **people judge lengths more
  accurately than areas**. A value encoded as one length (a bar) is perceived
  more accurately than one encoded as an area (two dimensions combined).
  Differences look **smaller** in a pie or treemap than in bars. Keep this in
  mind when choosing between them.

## 2. Overlapping points (overplotting)

Overplotting happens with large datasets, and also with **small datasets that are
rounded or low-precision**, where many observations share identical values.
Hidden points distort perceived density and can completely hide a subgroup
(for example the only two 4WD points sitting exactly under other points).

| Data size | Remedy |
|---|---|
| Moderate n, rounding or ties | **partial transparency** + **small jitter** |
| Large n (thousands to hundreds of thousands) | **2D histogram** (rectangular bins) or **hex bins**, colored by count |
| Smooth density, moderate n | **contour lines** (optionally shaded), with small transparent points on top |
| Several overlapping groups | **separate panels** per group (small multiples), not overlaid colored contours |

- **Transparency** makes stacks look darker. But the reader can't count how many
  points are stacked, and darker points aren't self-explanatory.
- **Jitter** (small random offsets in x, y, or both) makes it obvious that the
  dark areas are stacks of points and reveals hidden ones. **Jitter changes the
  data, so keep it small.** Too much jitter puts points where no data exist and
  misrepresents the dataset.
- **Very large n**: no transparency setting works. Dense regions become solid
  blobs while sparse outliers fade away. Fixing one makes the other worse.
  Switch to **2D binning**: divide the plane into rectangles and color them by
  count (a sequential scale).
  - **Hexagonal bins** (Carr et al. 1987) represent the data slightly more
    accurately than squares, because the average distance from a point to its
    bin center is smaller for hexagons.
  - Be careful interpreting: for example "actual departure time" is not
    "scheduled time". Make sure the axis variables are what you claim.
- **Contour lines** of estimated 2D density work when density changes smoothly.
  Shading the enclosed regions (darker = denser) strengthens the impression.
- **Colored contours per group** work only for **2–3 groups that are clearly
  separated**. With more groups or heavy overlap you get a hairball of crossing
  lines, which is **bad**. Use **one panel per group**, with a shared background
  grid to compare positions across panels.

## 3. Redundant coding and legends

Color alone often fails: too many categories, small marks, CVD, grayscale
printing. **Redundant coding** means encoding the same variable in **more than one
aesthetic** (color + shape, color + position, color + labels), so color *enhances*
the figure without being the only carrier of key information.

**Scatterplots**
- Groups that differ only in color are hard to separate, especially if two similar
  colors (blue and green) sit on intermingled groups. Under tritanomaly or in
  grayscale they can become indistinguishable.
- Fix: **(1) assign the most distinct colors to groups that overlap spatially**,
  and **(2) give each group its own point shape.** Then the figure stays readable
  under CVD and in grayscale.

**Line plots**
- Line type (dashed, dotted) is a weaker option. Dashes look poor unless the line
  is straight or gently curved, they add visual noise, and matching dash patterns
  to a legend takes effort. Prefer direct labeling (below).

**Legend order must match visual order**
- If lines (or stacked areas, or bars) have a clear visual order, for example
  top-to-bottom at the right edge, **order the legend entries the same way.**
  Software usually sorts legends alphabetically, which forces the reader into a
  mental shuffle. Reordering helps everyone and especially CVD and grayscale
  readers, who can then use rank and lightness as cues.

## 4. Designing figures without legends

- Any legend is extra work: look up an item in one place, carry it over to
  another. **Whenever possible, design the figure so it needs no legend.**
  Moving the legend's content into the caption ("yellow dots are species X") is
  *not* eliminating the legend.
- **Direct labeling techniques:**
  - **Lines**: put each series name at the end of its line.
  - **Scatter groups**: draw an **ellipse** (or hull) around each group's main
    cloud and label it. Remove the background grid if the figure gets busy.
  - **Density curves**: write the label next to or inside each curve.
  - **Marginal densities**: put per-group density curves in the scatterplot
    margins and label those, which keeps the main panel uncluttered.
  - **Many items**: label a representative or interesting subset (see `color.md`
    §7).
- **Colored text labels** strengthen the link to the data but can turn out
  hard to read, and thin text looks lighter than a filled area of the same color.
  Use **two shades per hue**: a **light** shade for fills, and a **dark** shade
  for outlines, lines, and text.
- **One variable, several aesthetics → one legend element.** If a variable is
  mapped to both x position and color, don't draw a separate color legend.
  **Integrate the color bar into the x axis.**

## 5. Small multiples

(Also called trellis plots or faceting.) Slice the data by one or more variables,
draw **the same type of plot** for each slice, and arrange the panels in a
**grid** labeled by the slicing variable values. Small multiples can show very
large amounts of data (dozens to 100 panels) and are very intuitive.

- **Use the same axis ranges and scales in all panels.** Readers assume they are
  the same. Independent y scales make every panel fill its range, so small and
  large categories look equally big and changes look equally dramatic. That is
  **bad**.
  - If different scales truly can't be avoided, **say so explicitly in the
    caption** ("Note that y-axis scales differ between panels").
- **Order the panels logically**: natural order (class 1→3, years left-to-right
  and top-to-bottom) or by a summary value (most to least popular). Never in
  arbitrary order.
- Small multiples don't need panel letters (a, b, c), because the facet labels
  identify each panel.

## 6. Compound figures

Different plots (possibly different data) combined into one figure to make one
overall point.

- **Label panels with letters** (a, b, c… or A, B, C…), starting top-left and
  going left-to-right, top-to-bottom, so text can refer to "Figure 5b".
- **Panel labels should be unobtrusive**, like page numbers. They should be in the
  same font as the rest of the figure, not oversized or bold-heavy, placed
  consistently (top-left of each panel), and **consistent across all figures in
  the document** (pick lowercase or uppercase and stick with it). They should not
  look slapped on afterwards.
- **Consistent visual language across panels**: the same thing must look the
  same everywhere. Same color for the same group, same order (for example
  female always left of male), same symbols, same fonts. Inconsistent colors and
  orders confuse readers and can even suggest the opposite conclusion. A
  consistent figure usually needs **only one shared legend**.
- **Align panels**: axes and other elements across panels should line up exactly.
  Misalignment (common when panels are made separately and pasted together)
  looks sloppy. Assemble panels programmatically when you can.
