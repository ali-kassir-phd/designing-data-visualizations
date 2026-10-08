# Visualizing proportions and nested proportions

## Contents
1. No single best chart
2. Pie vs. stacked bars vs. side-by-side bars
3. When pies win
4. When side-by-side bars win
5. When stacked bars and stacked densities win
6. Parts shown separately against the whole
7. Nested proportions: what goes wrong
8. Mosaic plots
9. Treemaps
10. Nested pies
11. Parallel sets
12. Decision guide

---

## 1. No single best chart

Proportions (vote shares, market shares, gender composition) are hard to show
well, especially when there are **many pieces** or when proportions **change
over time or across conditions**. No visualization is always best. Choose by
the data and the specific point you want to make. Reflexively rejecting pie
charts is as wrong as using them for everything.

## 2. Pie vs. stacked bars vs. side-by-side bars

| Property | Pie | Stacked bars | Side-by-side bars |
|---|:-:|:-:|:-:|
| Clearly shows data as parts of a whole | ✔ | ✔ | ✖ |
| Easy visual comparison of relative proportions | ✖ | ✖ | ✔ |
| Emphasizes simple fractions (½, ⅓, ¼) | ✔ | ✖ | ✖ |
| Looks good even for very small datasets | ✔ | ✖ | ✔ |
| Works when the whole is split into many pieces | ✖ | ✖ | ✔ |
| Works for many sets or a time series of proportions | ✖ | ✔ | ✖ |

## 3. When pies win

- A **single** set of proportions with **few** parts, where the point involves
  **simple fractions** or **combinations of parts vs. the rest**. Example:
  parliament seats where a two-party coalition holds a slim majority over a third
  party. The pie makes "together they're just over half" obvious. Stacked or
  side-by-side bars don't.
- A single stacked bar column looks awkward. A single pie looks fine.

## 4. When side-by-side bars win

- Parts of **similar size** that need to be compared precisely, and/or
  **comparisons across several conditions or years**. Example: five companies,
  each near 20% market share, over three years.
  - A row of pies makes within-year comparison nearly impossible and hides
    changes between years.
  - Stacked bars show the trend of the outermost segments but **middle segments
    float on shifting baselines**, so they can't be compared across years. This
    is the main general drawback of stacked bars.
  - Side-by-side (grouped) bars show who is gaining and losing and the ranking
    within each year.

## 5. When stacked bars and stacked densities win

- **Stacked bars over time work well when each stack has only two parts.** No
  internal segment floats, so the shifting-baseline problem disappears. Example:
  share of women vs. men in a parliament per election year.
  - Add a **reference line at a meaningful threshold** (such as 50%) so readers
    can tell when the majority flips. Don't add lines at every quartile, which
    clutters the chart.
- **Stacked densities** handle proportions that change along a **continuous**
  variable (such as health status by age). You can think of them as infinitely
  many thin stacked bars. They inherit KDE caveats (see `distributions.md`).
  - Acceptable with a few categories if the pattern is clear.
  - **Limitation:** percent-of-total hides how the **absolute** counts change.
    If there are far fewer old people than young, a constant percentage hides a
    falling count.
  - **Bad** when one category's share changes drastically along the axis (for
    example "never married" and "widowed" by age). The other bands get distorted
    and become uninterpretable.

## 6. Parts shown separately against the whole

This fixes both the "side-by-side bars lose the whole" and the "stacked bars lose
the baseline" problems.
- Make **one panel per part**. Shade the **overall distribution in gray** and
  draw the part (density or bars) in color on top. Readers see each part's
  absolute size *and* its relation to the total.
- Variant: put the **percentage** on the y axis (the part in color vs. all
  others in gray) when the question is "at what age is X the majority?".
  Absolute counts answer "where is X concentrated".

## 7. Nested proportions: what goes wrong

Nested proportions are breakdowns by **several categorical variables** at once
(seats by party *and* gender, bridges by material *and* era).
- **Combined pie with overlapping categories → wrong.** If slices for material
  (100% on their own) and era (overlapping with material) share one pie, the
  slices sum to more than 100% because cases are counted twice.
- **Bars of overlapping categories in one chart → bad.** Not technically wrong,
  since bars don't have to sum to 100%, but readers will assume the categories
  are mutually exclusive (for example that "modern" bridges are neither steel
  nor wood).
- Whenever categories overlap, **show explicitly how they relate.**

## 8. Mosaic plots

- Split the x axis by the proportions of variable A. Within each A column, split
  the y axis by the proportions of variable B. Rectangle **area** is proportional
  to the count for each A × B combination. Both widths and heights vary.
- **Requirement:** each variable must **cover all observations**. The variables
  are orthogonal, and every combination is possible in principle (some may be
  empty).
- Emphasis: how the composition by B **changes across** A (for example how
  material use evolved by era).

## 9. Treemaps

- Recursively **nest rectangles**: split the whole by variable A, then split each
  piece by B, and so on. Area is proportional to amount. More than 2–3 levels
  gets unwieldy.
- **No orthogonality requirement.** Treemaps fit **hierarchies** where
  sub-categories differ between parents (states within regions). Fill color can
  encode another variable (for example population as a sequential color).
- Emphasis: **totals** of the top-level groups.
- Space-efficient (no wasted white space), so **labels fit inside the
  rectangles**. Labels placed inside shapes bind more tightly to the
  data than labels outside, so prefer them.

**Mosaic and treemap caveat:** rectangles don't share baselines and their
**shapes differ**, so equal counts can look very different (a tall thin rectangle
vs. a short wide one). There may be no perfect fix. **Print the counts or
percentages on the rectangles** so readers can check their visual reading.

## 10. Nested pies

- **Two concentric rings** (inner = A, outer = B within A): "ugly". Each case is
  still effectively counted twice across the rings, and the fact that every case
  has both attributes is obscured.
- **One pie sliced by A, then sub-sliced by B, with a nested color scale**: hue
  for A (green = wood, orange = iron, blue = steel), lightness for B (darker =
  more recent). This is reasonable.
- **Still, prefer the treemap.** It uses the rectangle with no wasted space, fits
  inside labels, and avoids hairline slices.

## 11. Parallel sets

- For **more than two categorical variables**, where mosaics, treemaps, and pies
  break down. Each variable is a vertical axis split into its categories.
  **Bands** connect the categories and show how subgroups flow between
  variables.
- Color the bands by **one** variable to trace it through the others.
- **Put the coloring variable on the far left.** People read left to right, so
  color should originate at the left edge.
- **Reorder the axes to minimize crossing bands.** The same data with a better
  axis order goes from "ugly" to readable.

## 12. Decision guide

| Situation | Recommended |
|---|---|
| One set, few parts, simple fractions or coalition-style sums | pie |
| One set, many parts, or precise comparison of parts | side-by-side bars |
| Several sets or time points, parts of similar size | side-by-side (grouped) bars |
| Time series of a two-part split | stacked bars + a 50% reference line |
| Many conditions, few parts | stacked bars |
| Proportions along a continuous variable | stacked densities, or per-part panels vs. a gray total |
| Need both shares and absolute sizes | per-part panels against the gray whole |
| Two orthogonal categorical variables | mosaic plot (with counts labeled) |
| Hierarchy or non-orthogonal grouping | treemap (labels inside) |
| Three or more categorical variables | parallel sets (coloring variable left, minimal crossings) |
| Avoid | combined pies with overlapping categories (wrong), overlapping categories as plain bars, concentric two-ring pies |
