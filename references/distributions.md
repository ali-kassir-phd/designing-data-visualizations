# Visualizing distributions

## Contents
1. Histograms
2. Density plots (KDE)
3. Histogram vs. density
4. Two or a few distributions
5. ECDFs: parameter-free distributions
6. Highly skewed and heavy-tailed data
7. Q-Q plots
8. Many distributions: response vs. grouping variable
9. Mean ± error bars for distributions (avoid)
10. Boxplots, violins, strip charts, sina plots
11. Ridgeline plots
12. Decision guide

---

## 1. Histograms

- Bin the data and draw rectangles. Height is the count, width is the bin width.
  **All bins must have equal width** for a valid histogram.
- Appearance **depends heavily on bin width**, and software defaults are rarely
  ideal. **Always try several bin widths.** If bins are too narrow, the plot is
  peaky and noisy and hides the main trend. If too wide, real features (dips,
  secondary peaks) vanish. Example: for ages 0–75, 1-year bins are too narrow,
  15-year bins too wide, and 3–5-year bins work.

## 2. Density plots (KDE)

- A smooth curve that estimates the underlying probability distribution, most
  often by kernel density estimation. A small kernel (usually Gaussian) is placed
  on every data point and the kernels are summed.
- **Bandwidth** acts like bin width: too small is noisy, too large over-smooths.
  The **kernel** shape matters too. Gaussian kernels make everything look smooth
  and bell-like, and rectangular kernels create artificial steps. Kernel choice
  matters less with more data, so densities are **reliable for large datasets
  and can mislead with few points**.
- The area under the curve is usually 1, so **y-axis values depend on x units**
  (for x spanning 0–75, the average height is about 1/75 ≈ 0.013). This can
  confuse readers. Consider whether the y axis needs numbers at all.
- **Pitfall: density estimates invent data in the tails**, including impossible
  values (negative ages, percentages above 100). **Always check that the density
  doesn't extend into impossible ranges.** Restrict or bound the estimate if
  needed.

## 3. Histogram vs. density

The choice is largely a matter of taste. Both are interpretations of the data
that depend on parameters. Pick whichever shows the features of interest more
faithfully. Densities have a clear advantage **as soon as more than one
distribution is shown**. ECDFs and q-q plots are the parameter-free
alternative.

## 4. Two or a few distributions

- **Avoid stacked histograms.** Readers can't tell whether a stacked segment
  starts at zero or at the color change, and upper segments can't be compared
  because they sit on different baselines. Group differences (for example, men
  older than women) become invisible.
- **Avoid overlapping semi-transparent histograms.** The overlap looks like a
  third group with its own color, and bar boundaries remain unclear.
- **Overlapping density lines** work better because the continuous outlines keep
  the groups apart. They work best when the distributions are reasonably distinct.
  To also convey group size, scale each curve so its area equals the group's
  count instead of 1.
- **Each group as a proportion of the total**: draw the overall distribution in
  gray and each subgroup's density (scaled to its share) in color, one panel per
  group. This clearly shows where in the range each group is over- or
  under-represented.
- **Exactly two distributions**: an **age pyramid**, two histograms rotated 90°
  and pointing in opposite directions. This does **not** extend to three or more.
- **More than two**: histograms get very confusing. Density plots work as long
  as the distributions are reasonably distinct and contiguous.

## 5. ECDFs: parameter-free distributions

- Histograms and densities are *interpretations* that depend on parameters. The
  **empirical cumulative distribution function** needs **no parameters and shows
  every data point**. The cost is that it's less intuitive, so it is common in
  technical and statistical work and rare elsewhere.
- Construction: rank the observations in ascending order and plot rank vs. value,
  as a step function. Usually you normalize the rank to the 0–1 cumulative
  fraction and omit the individual points.
- Read it directly: the y value at x is the fraction of observations ≤ x. The
  median is where y = 0.5. Quartiles and other percentiles can be read the same
  way.
- **Flat stretches** mark gaps in the data and **steep jumps** mark ties or
  clusters. This makes ECDFs good for setting cutoffs (such as grade boundaries)
  that fall inside natural gaps.
- A **descending ECDF** (fraction with value ≥ x) flips the curve. It is the
  key tool for heavy-tailed distributions.

## 6. Highly skewed and heavy-tailed data

- Many real distributions have **long right tails**: city and county
  populations, social network contacts, word frequencies, papers per author, net
  worth, protein interaction partners. Very large values are not rare.
  **Power laws** (scale-free distributions) are an important case.
- On linear axes, both the density plot and the ECDF of such data are useless: a
  spike at zero and nothing else.
- **Log-transform** the values. If the data are **log-normal** (for example US
  county populations), the log values give a clean bell-shaped density and a
  sigmoidal ECDF.
- To test for a **power law**, plot a **descending ECDF on log–log axes**. A power
  law appears as a **straight line**. Near-straight but curving means "heavy
  tail but not a pure power law".

## 7. Q-Q plots

- Use these to judge **how well data follow a reference distribution** (usually
  normal). Each observation's rank gives the theoretical quantile it *should*
  have. Plot observed values against theoretical values.
- Draw the **x = y line**. It is not a regression line. Points on it mean the
  data follow the reference distribution. Systematic departures at the ends show
  heavy or light tails, skew, or floor and ceiling effects (for example, scores
  capped at 100).
- To check log-normality, make a normal q-q plot of the log values.

## 8. Many distributions: response vs. grouping variable

Think in terms of a **response variable** (whose distribution you show) and one
or more **grouping variables** (which define the subsets). Response goes on one
axis and grouping on the other. Every layout below can be flipped.

## 9. Mean ± error bars for distributions (avoid)

Showing each group as a point with error bars is **bad** for describing
distributions:
1. It throws away most of the information.
2. It isn't obvious whether the point is a mean or a median.
3. It isn't obvious what the bars mean: SD, SE, 95% CI? There is no standard,
   and readers easily confuse SD (spread of the data) with SE (precision of the
   mean). A dataset can have a tiny SE and a huge SD.
4. **Symmetric bars misrepresent skewed data**, and real data are almost always
   somewhat skewed.

Error bars are conventionally used for **uncertainty of an estimate**, not
**variability in a population**. Use one of the methods below to show
variability.

## 10. Boxplots, violins, strip charts, sina plots

**Boxplot** (Tukey). The line is the median and the box is the middle 50% (the
interquartile range, IQR). Whiskers extend to the most extreme data point within
1.5 × IQR of the box (the "fences"), or to the min/max if those are closer.
Points beyond the fences are drawn individually as outliers. Simple,
standardized, good side by side, and it shows skew. **But it hides
bimodality.**

**Violin plot**: a density estimate rotated 90° and mirrored. Width is the point
density at each y. It spans the data min to max. It can replace a boxplot
anywhere and **reveals bimodality** that boxplots hide.
- **Check that each group has enough data points** to justify a smooth density.
- It inherits density pitfalls: it can suggest data where none exist, or make
  sparse data look dense.

**Strip chart**: every observation drawn as a dot along the response axis. This
is fine if the points don't pile on top of each other. Fix overplotting by
**jittering**, adding small random offsets along the grouping axis. When data
are too sparse for violins, plot the raw points.

**Sina plot**: points jittered in proportion to the local density, which gives
a violin outline made of the actual points. It shows each observation *and*
the distribution shape. It can also be layered on top of violins.

## 11. Ridgeline plots

- Densities along the horizontal axis, staggered vertically by group, like
  overlapping mountain ridges. Often **more intuitive than violins**: bimodality
  and shifts jump out.
- There is no explicit density axis. As with violins, the point is comparing
  shapes and relative heights, not reading density values.
- **Use densities, not histograms.** Ridgeline histograms line up their bar edges
  confusingly and look busy.
- **Scales to very many distributions** (around 100 is fine), and is excellent
  for **distributions changing over time** (for example movie lengths by year).
- Can compare two groups over time by drawing two colored densities per row (for
  example two parties' voting scores per Congress).

## 12. Decision guide

| Situation | Recommended |
|---|---|
| One distribution, general audience | histogram (several bin widths tried) or density (sensible bandwidth, bounded tails) |
| One distribution, need exact percentiles or no arbitrary parameters | ECDF |
| Heavy-tailed or skewed | log-scale density or ECDF, descending log–log ECDF for power laws |
| Does the data follow distribution X? | q-q plot with an x = y line |
| Two distributions | overlapping densities, proportions-of-total panels, or an age pyramid |
| 3–5 distinct distributions | overlapping densities |
| Many groups, interest in shifts | boxplots, or violins if n is large enough |
| Many groups, small n | jittered strip chart or sina plot |
| Many groups or a time series of distributions | ridgeline plot |
| Avoid | stacked or overlapping histograms, mean ± SD bars, ridgeline histograms |
