# Time series, ordered x, and trends

Uncertainty around trend lines
(confidence bands) is in `uncertainty.md`.

## Contents
1. Single time series: dots, lines, filled area
2. Multiple time series: lines and direct labels
3. Line graphs beyond time: dose–response
4. Two response variables over time: stacked panels vs. connected scatter
5. High-dimensional time series: connected scatter in PCA space
6. Smoothing: moving averages, LOESS, splines/GAMs
7. Fitting a defined functional form
8. Transform axes to make relationships linear
9. Detrending
10. Time-series decomposition (trend, seasonal, remainder)
11. Decision guide

---

## 1. Single time series: dots, lines, filled area

Time gives the data a **natural order**: each point has one predecessor and one
successor. Show that order.
- **Dots only** treat the data like an ordinary scatter.
- **Dots joined by lines** emphasize order. The lines aren't data, and some
  object that they imply values between observations. When observations are
  sparse or unevenly spaced, the lines still help perception, but **say so in
  the caption** (for example "lines are a guide to the eye").
- **Line only (no dots)** is standard practice. It emphasizes the overall trend,
  de-emphasizes individual observations, and looks less busy. **The denser the
  series, the less you need the dots.**
- **Filled area under the line** emphasizes the overall trend even more. **Do this
  only with a y axis anchored at zero**, because the shaded height must
  represent the value (see proportional ink in `figure-design.md`).

## 2. Multiple time series: lines and direct labels

- Several series drawn as dots alone interfere with each other, which is **bad**.
  **Connect them with lines** so each series can be followed.
- **Label lines directly** (the name at the right end of each line) instead of
  using a legend. This removes the color-matching effort, removes the need for
  different point shapes, and lets you drop the dots for a much cleaner figure.

## 3. Line graphs beyond time: dose–response

Line graphs fit **any x that imposes an order**, such as an experimental dose
or treatment level set to a range of values. Example: crop yield vs. fertilizer
amount, one line per variety. The lines reveal both the shared curve shape and
differences in baseline.

## 4. Two response variables over time: stacked panels vs. connected scatter

Example: house-price change and unemployment rate over the same years.
- **Separate line graphs stacked vertically** (shared time axis): straightforward
  and easier for most readers. But spotting when the two move together or
  opposite means flicking between panels and comparing slopes.
- **Connected scatterplot** (also called a phase portrait): plot variable A vs.
  variable B and connect consecutive time points into a path.
  - Movement toward the upper right means **correlated** change. Movement toward
    the upper left or lower right means **anticorrelated** change. **Loops or
    spirals** reveal cyclical relationships that are hard to see in separate
    line graphs.
  - **You must show direction and timing**: for example a color gradient that
    gets darker over time, arrows along the path, and date labels at key
    points. Without them the plot is a meaningless scribble, which is **bad**.
  - Research note (Haroz, Kosara & Franconeri 2016): readers **misread order and
    direction more often** and report correlation less often than with line
    graphs, but connected scatterplots are **more engaging**. That can help draw
    readers into a story.

## 5. High-dimensional time series: connected scatter in PCA space

- With dozens or hundreds of series (for example 100+ macroeconomic indicators),
  run **PCA** first (see `associations.md`), then draw the connected scatter in
  PC space (PC2 vs. PC1, PC2 vs. PC3).
- PC1 often measures overall **system size** (for example the size of the
  economy), so PC1-vs-PC2 often looks like an ordinary time series. Color
  phases (such as recession vs. recovery) and label key endpoints to reveal
  cycles.

---

## 6. Smoothing: moving averages, LOESS, splines/GAMs

Use smoothing to show the **long-term trend** without short-term noise, drawn on
top of or instead of the raw data.

**Moving average** (mean over a sliding window)
- **Window length sets which fluctuations survive.** A short window (20 days)
  only removes spikes. A long one (100 days) can erase even major multi-week
  drops. Make sure the smoothing doesn't hide something important.
- Where you plot each average matters:
  - at the **window end** (finance convention): the curve **lags** the data, and
    the lag grows with window size.
  - at the **window center** (statistics convention): the curve lines up with
    the data.
- Limitations: the smoothed curve is **shorter** than the data, because the ends
  are lost and more so with bigger windows. It can still be **wiggly**, because
  points entering and leaving the equal-weight window cause bumps.

**LOESS** (locally estimated scatterplot smoothing)
- Fits low-degree polynomials to local subsets, weighting central points more.
  It is **much smoother than a moving average**, covers the **full data range**,
  and works on **any scatterplot**, not only time series.
- Smoothness is a tunable parameter. Similarity to a given moving average is
  coincidental.
- Usually "looks right" but is **slow on large datasets**.

**Splines**
- Piecewise polynomials joined at **knots** (k segments need k + 1 knots). Fast
  and always smooth.
- There are many types (cubic, B-spline, thin-plate, Gaussian process…), and the
  **type and knot count can change the curve dramatically**, especially **near
  the data boundaries**.

**GAMs** (generalized additive models): the general family that covers these
smoothers and is often what software uses by default.

**Caution:** a smoother's output depends heavily on the method and its defaults.
**Try several settings** before trusting or publishing a smooth. The same data
can be smoothed in many different ways.

## 7. Fitting a defined functional form

- General smoothers can behave unpredictably and their parameters have **no
  interpretable meaning**. **When possible, fit a curve with an appropriate
  functional form and meaningful parameters.**
  - Rises linearly, then levels off: for example y = A − B·exp(−m·x).
  - **Straight line** y = A + m·x. Approximately linear relationships are
    surprisingly common. Draw per-group linear fits over scatterplots to help
    readers see the trends.
  - Constant percentage growth gives an **exponential** y = A·exp(m·x).

## 8. Transform axes to make relationships linear

- To test a guessed nonlinear form, **transform the axes so it should become a
  straight line**:
  - **log–linear** (log y, linear x): exponential growth becomes a line.
  - **log–log**: power laws y ~ x^α become lines.
  - **linear–log** (linear y, log x): logarithmic relationships y ~ log(x)
    become lines.
- **Prefer fitting a straight line to transformed data over fitting a nonlinear
  curve to raw data.** A direct exponential fit by least squares is dominated by
  the largest values and systematically misses the small ones. A linear fit on
  log(y) treats all magnitudes fairly.

## 9. Detrending

- When a series has a strong long-term trend (for example house prices growing
  exponentially, which looks straight on a log axis), **remove the trend** to
  expose unusual deviations such as bubbles and crashes.
- For multiplicative or exponential trends, **divide** the actual value by the
  trend value. On a log scale this is the same as subtracting. Example: a
  "modest" price dip can be a 25% shortfall relative to the expected rise.
- Show the raw series with the trend line (log y), and the detrended ratio as a
  separate panel or figure.

## 10. Time-series decomposition (trend, seasonal, remainder)

- A series = **long-term trend** + **cyclical/seasonal** components (daily,
  annual…) + **remainder**. The remainder holds random noise *and* unique
  external events (a volcanic eruption would show up as a spike).
- Methods such as **STL** (Seasonal-Trend decomposition using LOESS) split the
  series. Show **stacked panels**: observed, trend, seasonal, remainder.
  - Compare the **magnitudes** across panels (for example trend +50 ppm vs.
    seasonal swing < 8 ppm vs. remainder < 1.6 ppm). Panels may need
    independent y scales. Say so and make the ranges clear.
  - Zooming into a recent window helps show the shape of the seasonal component.

## 11. Decision guide

| Situation | Recommended |
|---|---|
| One dense time series | line, no dots |
| One sparse or irregular series | dots + lines ("guide to the eye" in caption) |
| Emphasize the magnitude trend, y from 0 | filled area chart |
| Several series | lines + direct end labels, no legend |
| Ordered experimental x (dose) | line graph per group |
| Two responses over time, general audience | stacked line panels with a shared x |
| Two responses, cyclical relation, engaged readers | connected scatter with color/arrows for direction and date labels |
| Many responses over time | PCA, then connected scatter in PC space |
| Noisy series or scatter, show trend | LOESS or spline (try several settings) over the raw data |
| Known or plausible functional form | fit the model, ideally linearized via axis transform |
| Exponential growth | log y axis, linear fit to log data |
| Long-term trend hides events | detrend (ratio to trend) |
| Seasonal data | STL-style decomposition panels |
