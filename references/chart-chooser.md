# Chart chooser: a directory of visualizations by message

Charts are grouped by the **message** they convey (how large, how distributed, what share, how
related, how it changes, where, how certain), not by data type. Start here when
picking a chart type, then read the detailed reference file.

| Message | Go-to options | Details |
|---|---|---|
| **Amounts**: values for a set of categories | bars (vertical or horizontal), dot plot, grouped or stacked bars, heatmap | `amounts.md` |
| **Distributions**: how values are spread | histogram, density, ECDF, q-q plot, boxplot, violin, strip chart, sina, ridgeline | `distributions.md` |
| **Proportions**: parts of a whole | pie, side-by-side bars, stacked bars, stacked density, mosaic, treemap, parallel sets | `proportions.md` |
| **x–y relationships**: association between quantities | scatter, bubble chart, slopegraph, correlogram, 2D bins/hex/contours, PCA | `associations.md` |
| **Change over time / trends** | line graph, connected scatter, smoothed trend, detrended / seasonal decomposition | `time-series-trends.md` |
| **Geospatial** | map, choropleth, cartogram, cartogram heatmap | `geospatial.md` |
| **Uncertainty** | error bars, graded error bars, confidence strips, eye / half-eye, quantile dot plot, confidence bands, fitted draws, HOPs | `uncertainty.md` |

## Amounts
- **Bars** (vertical or horizontal) are the default for showing a numerical value
  per category.
- **Dots** at the position where a bar would end. Use these when the axis
  shouldn't start at zero.
- Two or more categorical variables: **grouped bars**, **stacked bars**, or a
  **heatmap** (categories on x and y, amount as color).

## Distributions
- **Histograms and density plots** are the most intuitive, but both depend on
  arbitrary parameters (bin width, bandwidth) and can mislead.
- **Cumulative distributions (ECDF) and q-q plots** always represent the data
  faithfully but are harder to read.
- Many distributions at once, or interest in overall shifts: **boxplots, violins,
  strip charts, sina plots**.
- A few distributions in depth: **overlapping densities**. Stacked histograms are
  hard to interpret and best avoided.
- Very many distributions, or distributions changing over time: **ridgeline
  plots**.

## Proportions
- **Pie charts** emphasize that parts make a whole and make simple fractions
  (½, ¼) easy to read.
- **Side-by-side bars** make it easiest to compare individual parts.
- **Stacked bars** are clumsy for one lone set of proportions, but they become
  useful when several sets are compared.
- Several sets, or change across conditions: pies waste space and hide
  relationships. **Grouped bars** work for a moderate number of conditions,
  **stacked bars** for many, and **stacked densities** when proportions change
  along a continuous variable.
- Proportions defined by several grouping variables: a **mosaic plot** (every
  level of one variable crosses every level of the other), a **treemap** (no
  such assumption; subdivisions can differ between groups), or **parallel sets**
  (best for more than two grouping variables).

## x–y relationships
- **Scatterplot** is the standard for one quantitative variable against another.
- A third quantitative variable mapped to point size gives a **bubble chart**.
- **Paired data** (both axes in the same units): add an **x = y line**, or use a
  **slopegraph** (paired points joined by lines).
- Many points (overplotting): **contour lines, 2D bins, hex bins**.
- More than two or three variables: a **correlogram** of correlation
  coefficients, or dimension reduction (PCA).
- x is time or another strictly increasing quantity (such as dose): a **line
  graph**.
- Two response variables over time: a **connected scatterplot**.
- Trends in larger or noisy datasets: **smoothed lines**.

## Geospatial
- **Map**: projects globe coordinates onto a plane with approximately faithful
  shapes and distances.
- **Choropleth**: regions colored by a data value.
- **Cartogram**: regions distorted by another quantity (such as population).
  **Cartogram heatmap**: each region simplified to an equal square.

## Uncertainty
- **Error bars** show the range of likely values around a point estimate, drawn
  from a dot or a bar.
- **Graded error bars** show several confidence levels as nested bars of
  different thickness.
- To show the full confidence or posterior distribution:
  - **Confidence strips** give an intuitive sense of uncertainty but are hard to
    read precisely.
  - **Eyes** (violin + error bars) and **half-eyes** (ridgeline + error bars)
    show both precise intervals and the overall distribution.
  - **Quantile dot plots** show the distribution as discrete units. They are
    less precise but easier to understand as probabilities.
- For smooth lines, the equivalent of error bars is a **confidence band**, or
  **graded bands**, or **individual fitted draws** drawn instead of or in
  addition to the bands.
