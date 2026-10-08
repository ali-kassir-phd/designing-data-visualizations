# Visualizing associations among quantitative variables

For handling overplotting in large scatterplots, see
`figure-design.md` § Overlapping points. For trend lines through scatter, see
`time-series-trends.md` § Smoothing.

## Contents
1. Scatterplots
2. Adding a third or fourth variable: color, bubble size
3. Scatterplot matrices
4. Correlograms
5. Dimension reduction (PCA)
6. Paired data: x = y line and slopegraphs
7. Decision guide

---

## 1. Scatterplots

- The standard chart for **two quantitative variables**. One dot per observation.
  Terminology: you plot *y against x*.
- Look for trend direction and strength, clusters, and outliers.
- **Color points by a grouping variable** (such as sex or species) to check
  whether an overall trend holds within groups or is driven by group
  differences. Groups can sit at different average levels or have different
  relationships. This is a quick guard against Simpson's-paradox-style
  misreadings.

## 2. Adding a third or fourth variable: color, bubble size

- **Bubble chart**: map a third quantitative variable to point size.
- Drawbacks:
  - The *same kind* of variable (quantitative) is shown with *two different kinds*
    of scale (position and size), so it's hard to compare the strength of the
    associations.
  - **Size differences are much harder to perceive than position differences.**
    The largest bubble must still be small relative to the figure, so the
    available size range is narrow and moderate data differences become nearly
    invisible.
- Use bubble charts sparingly. For three or four quantitative variables, a
  scatterplot matrix is usually clearer.

## 3. Scatterplot matrices

- All-against-all grid of pairwise scatterplots (color can still mark groups).
- Because position is judged more accurately than size, relationships that were
  hidden in a bubble chart become visible.
- Becomes unwieldy beyond about **3–4 variables**.

## 4. Correlograms

- For many variables, show the **correlation coefficient r** for each pair instead
  of the raw data. r ranges from −1 to 1. Its sign gives direction
  (correlated vs. anticorrelated) and its magnitude gives strength (0 = no
  linear association). r is symmetric in x and y and unchanged by shifting or
  rescaling either variable.
- Display it as a matrix of **tiles colored on a diverging scale centered at 0**.
  With k variables there are k(k−1)/2 unique pairs (7 variables → 21).
- **Improvement:** draw **circles whose size scales with |r|** in addition to
  color. Near-zero correlations then visually recede and strong ones stand out.
  Plain tiles give weak correlations too much visual weight.
- **Drawback:** correlograms are abstract and **hide the raw data**. Correlation
  only measures linear association, so nonlinear patterns, clusters, and outliers
  can produce misleading r values. In general, **prefer showing raw data over
  derived summary statistics** whenever feasible.

## 5. Dimension reduction (PCA)

- A middle ground between abstract summaries and raw data. High-dimensional data
  usually have **correlated variables carrying overlapping information** (for
  example many body measurements mostly reflect overall size, then sex).
- **PCA**: standardize variables (mean 0, variance 1), then define new
  uncorrelated axes (**principal components**) ordered by how much variance they
  capture. Geometrically this is a rotation. The first 2–3 PCs usually show the
  key structure.
- Show two things:
  1. **Component composition (loadings)**: arrows for the original variables in
     PC1–PC2 space. Arrow direction shows which PCs a variable contributes to.
     Short arrows mean the variable contributes mostly to higher PCs that aren't
     shown.
  2. **Scores**: the observations projected into PC1–PC2 space, colored by known
     groups to reveal clustering. Interpret the clusters by comparing with the
     loadings ("windows sit at high PC1, which is driven by low Ba/Al/Na").
- Label axes with the component (and ideally the % of variance explained).

## 6. Paired data: x = y line and slopegraphs

Paired data are **repeated measurements of one quantity** taken under
closely related conditions: left and right arm, the same subject at two times, twins,
the same country in two years. Members of a pair are more alike than random
observations, so the visualization should **highlight within-pair differences**.

- **Scatterplot + diagonal x = y line.**
  - Pure noise means points scatter symmetrically around the diagonal. A
    systematic difference means points shift above or below it.
  - Both axes have the same units, so **use equal scaling (1:1 aspect ratio)**.
    Use log axes on *both* if values span orders of magnitude.
  - Best for **many observations** and **overall systematic shifts**.
- **Slopegraph**: two (or more) columns of dots, one per condition, with lines
  connecting each pair. Slope shows the direction and size of change.
  - Best for **few observations** where **individual identity matters**. Label
    each line directly.
  - **Extends to three or more time points**, which reveals cases whose trend
    reverses between intervals.

## 7. Decision guide

| Situation | Recommended |
|---|---|
| Two quantitative variables | scatterplot |
| Plus a categorical grouping | scatterplot colored (and/or shaped) by group |
| Plus a third quantitative variable | scatterplot matrix (preferred) or bubble chart |
| Many quantitative variables | correlogram (color + size by \|r\|), then PCA |
| High-dimensional data, want structure plus raw observations | PCA loadings plot + scores plot |
| Paired data, many cases, overall shift | scatter + x = y line, equal axes |
| Paired data, few cases, identity matters, or 3+ time points | slopegraph with direct labels |
| Very many points | see overplotting fixes in `figure-design.md` |
| Time on x / ordered x | see `time-series-trends.md` |
