# Foundations: aesthetics, scales, coordinate systems, axes

For color scales, see `color.md`.

## Contents
1. Every chart is a mapping from data to aesthetics
2. Variable types and the scales they need
3. Scales must be one-to-one
4. Choosing which variable goes on which aesthetic
5. Cartesian coordinates, units, and aspect ratio
6. Nonlinear axes: log and square-root
7. Curved axes: polar coordinates and map projections

---

## 1. Every chart is a mapping from data to aesthetics

Scatter plots, pie charts, and heatmaps look different, but they all work the same
way. Each data value is turned into a measurable property of a graphical element.
These properties are called **aesthetics**:

| Aesthetic | Continuous data? | Discrete data? |
|---|---|---|
| Position (x, y) | yes | yes |
| Size | yes | yes |
| Color | yes | yes |
| Line width | yes | yes |
| Shape | no | yes |
| Line type (solid, dashed, dotted…) | no | yes |

Other aesthetics include font family, face, and size (for text) and transparency
(for overlapping objects). Every element needs a color to be visible at all, even
in a black-and-white figure.

**Practical rule:** shape and line type can only encode categories. Don't try to
encode a continuous quantity with them.

## 2. Variable types and the scales they need

Before choosing a chart, classify each variable:

| Variable type | Example | Scale |
|---|---|---|
| Quantitative continuous | 1.3, 5.7, 83, 0.015 | continuous |
| Quantitative discrete | 1, 2, 3 (counts, or any values with no possible intermediates) | discrete |
| Qualitative unordered (factor) | dog, cat, fish | discrete |
| Qualitative ordered (ordered factor) | good, fair, poor | discrete, in the natural order |
| Date/time | Jan 5 2018, 8:03am; or generic dates like Dec 25 | continuous or discrete |
| Free text | sentences | none, or treat as categorical |

Terms: numerical data is *quantitative*, categorical data is *qualitative*.
A categorical variable is a *factor*, and its categories are its *levels*.

## 3. Scales must be one-to-one

A **scale** maps data values to aesthetic values: positions on an axis, specific
colors, specific shapes. Each data value must correspond to exactly one aesthetic
value, and each aesthetic value to exactly one data value. If two categories share
a color, or one category gets two colors, the figure is ambiguous.

## 4. Choosing which variable goes on which aesthetic

- Any variable can go on any compatible aesthetic. The usual choice, such as
  putting the key quantity on y, is not the only valid one.
- If the key quantitative variable is shown as **color**, the colored areas have
  to be fairly large, because small marks make color differences hard to judge.
  Use tiles or squares (a heatmap-style layout), not thin lines or tiny points.
- **Discrete position scales:** levels are placed at equal spacing. Ordered
  factors must appear in their natural order. Unordered factors can go in any
  order, so pick one that helps the reader, for example sorting locations from
  coldest to hottest so the colors form a smooth progression.
- A basic chart typically uses about three scales (x, y, plus one of color, shape,
  or size). You can use more. Five scales (x, y, color, size, shape) can work when
  each encodes a distinct variable, but every extra scale costs the reader effort.

## 5. Cartesian coordinates, units, and aspect ratio

- A **coordinate system** is a set of position scales plus their geometric
  arrangement. The default is 2D Cartesian: orthogonal x and y axes with even
  spacing. Axis limits decide which data are shown, and values outside the limits
  are dropped. Watch for silently clipped data.
- Changing units (°F → °C, miles → km) is a linear transformation. Cartesian
  plots are unchanged by it: the picture stays the same and only the tick labels
  change.
- **Axes in different units** (for example temperature vs. date): the aspect
  ratio is a free choice and every version is valid. Tall and narrow emphasizes
  change in y, and short and wide de-emphasizes it. Pick an aspect ratio that
  makes the important differences in position visible.
- **Both axes in the same units** (for example temperature in city A vs. city B,
  predicted vs. observed): use a **fixed 1:1 aspect ratio** so one data unit is
  the same length on both axes and the grid cells are squares.

## 6. Nonlinear axes: log and square-root

**Log scales**
- On a log scale, each equal step means multiplying by a fixed factor
  (1 → 10 → 100). The midpoint between 1 and 10 is √10 ≈ 3.16.
- Plotting log-transformed data on a linear axis and plotting raw data on a log
  axis give the same geometry. The difference is the labels. **Prefer a log axis
  labeled with the original values** (1, 10, 100). It is easier to read and
  avoids confusion about the base. The axis title should name the variable itself
  (for example "population"), not "log(population)".
- If you do show log-transformed values, **always state the base** (log10, ln,
  log2). A bare "log(x)" is ambiguous.
- Use log scales for:
  - **Ratios and fold changes. Ratios should practically always be on a log
    scale.** On a linear axis, ratios above 1 are stretched and ratios below 1
    are squashed into a sliver near zero. On a log scale, 2× and ½× sit at the
    same distance from 1.
  - Anything that arises from multiplication or division.
  - Data spanning several orders of magnitude.
- On a log scale, 1 is the natural midpoint, the way 0 is on a linear scale. Mark
  it with a reference line when values are ratios.
- **Zero cannot appear on a log scale**, because it lies infinitely far away.
  Decide explicitly how to handle zeros.

**Square-root scales**
- These compress large values like a log scale does, but they allow zero.
- Drawbacks: a unit step has no constant meaning (it is neither additive nor
  multiplicative), and tick placement is awkward. Ticks at squares
  (0, 4, 25, 49…) look odd. Evenly spaced ticks crowd at one end. A pragmatic
  choice is a hand-picked set such as 0, 1, 5, 10, 20, 30, 40, 50.
- A sensible use: quantities that are naturally squared, such as **areas**. On a
  square-root scale, area values reflect linear extent (for example, how long it
  takes to drive across a region).

## 7. Curved axes: polar coordinates and map projections

- **Polar coordinates** map one variable to an angle and another to a radius.
  Use them for **cyclical data**, where the end of the scale joins the beginning
  (day of year, hour of day, compass direction, month). They make the
  December–January transition continuous, where a Cartesian plot would split it
  across opposite edges.
- **Geographic data:** longitude and latitude plotted directly as Cartesian x and
  y (equirectangular) distort both areas and angles, so avoid this for world maps.
  Use a proper projection. Some preserve area (for example, interrupted Goode
  homolosine, which cuts land masses into lobes). Others compromise between area
  and angle distortion and are common for world maps (Robinson, Winkel tripel).
  See `geospatial.md` for more.
