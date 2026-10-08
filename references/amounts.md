# Visualizing amounts

"Amounts" means a set of categories, each with one
quantitative value: sales by brand, population by city, median age by sport.
The emphasis is on **magnitude**. Standard tools are bars (simple, grouped,
stacked). Alternatives are dot plots and heatmaps.

## Bar plots

- Each bar **starts at zero** and extends to the value. Bar length must be
  proportional to the value (see `figure-design.md` § Proportional ink).
- **Long category labels → horizontal bars.** Rotated tick labels on vertical
  bars are awkward to read and waste space, and labels too long to fit
  horizontally don't look good rotated either. Swap the axes so all text is
  horizontal.
- **Order matters:**
  - **Unordered categories**: sort bars by value, ascending or descending.
    Alphabetical order (a common software default) or other arbitrary orders
    make the chart confusing.
  - **Ordered categories** (age groups, income brackets, months, Likert levels):
    **keep the natural order**. Sorting age groups by height scrambles the
    meaning.

## Grouped bars (two categorical variables)

- One variable sets the position of each group along the axis, and the other
  sets the bars within the group, distinguished by color.
- Grouped bars pack in a lot and can be **hard to read**. Comparisons *within* a
  group (adjacent bars) are easy. Comparisons of the same color-coded category
  *across* groups are hard.
- **Put the variable you most want compared on the within-group (adjacent)
  position.** Swapping which variable sets the groups and which sets the bars
  changes the story the chart tells.
- Matching bar colors against a legend takes mental effort. Often a better
  option is **small multiples**: one simple bar chart per level of the second
  variable, which needs no color coding at all.

## Stacked bars

- Stack **only when the sum of the stacked pieces is itself meaningful.** Counts
  (men + women = all passengers) and totals (gross of film A + film B) can be
  stacked. Medians, means, and rates **cannot**, because the sum of two median
  incomes means nothing.
- When there are only a few values, **write the numbers directly on or next to
  the bars**. That adds a lot of information with little visual noise, and you
  can then **omit the y axis**.

## Dot plots (Cleveland dot plots)

- Bars must start at zero. When all values are large and close together (for
  example life expectancies of 60–81 years), long bars of almost the same length
  draw the eye to their middles and hide the differences.
- **Dots at the value, with the axis limited to the data range**, put the
  differences up front. Dots don't need a zero baseline because their position
  is read against the axis, not their length.
- Ordering still matters. Sort by value. Alphabetical order turns a dot plot into
  a disordered cloud and should be considered **bad**.

## Heatmaps

- For large tables (many categories × many conditions, for example 20 countries
  × 23 years), position-based charts get too busy. **Map the value to color**
  instead.
- The tradeoff: exact values are hard to read, but **broad patterns and trends
  stand out**.
- **Row and column order sets the story.** Order rows by the final value to tell
  a "who leads now" story, or by when they crossed a threshold to tell an "early
  vs. late adopters" story. Both are valid. Choose based on the message.
- Use a sequential scale (or diverging, if there's a meaningful midpoint) as
  described in `color.md`.

## Quick decision guide

| Situation | Use |
|---|---|
| One categorical + one value, values comparable to zero | bar chart, sorted (or natural order) |
| Long category names | horizontal bars |
| Values far from zero, small differences matter | dot plot with a restricted axis |
| Two categorical variables, few levels | grouped bars, or better, small multiples |
| Parts that sum to a meaningful total | stacked bars |
| Many × many categories | heatmap, with deliberately chosen ordering |
| Very few values | label bars with numbers, consider dropping the axis |
