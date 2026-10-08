# Visualizing uncertainty

Readers tend to take any drawn point as exact. Almost
all data carry uncertainty, and how (or whether) you show it changes what the
audience concludes.

**Audience split:**
- **Experts or scientific readers**: error bars and confidence bands are
  precise and space-efficient, and they can show many estimates at once.
- **Lay audiences**: prefer **intuitive** displays (frequency framing, quantile
  dot plots, animated hypothetical outcomes), even at some cost in precision or
  data density. *A mathematically correct chart that people misperceive is not
  useful.*

## Contents
1. Probability as frequency (discrete outcome visualizations)
2. Probability distributions and quantile dot plots
3. Statistical vocabulary you must get right
4. Error bars: always say what they show
5. Graded error bars and deterministic construal error
6. Comparing estimates: show the CI of the difference
7. Error bar styling: caps, grading, strips, distributions
8. Error bars on other charts
9. Bayesian posteriors and credible intervals
10. Uncertainty of curve fits: bands and draws
11. Hypothetical outcome plots (HOPs)
12. Decision guide

---

## 1. Probability as frequency (discrete outcome visualizations)

- A single probability shown as a bar or a dot on a line gives little feel for
  the odds.
- **Frequency framing**: show e.g. a grid of 100 squares with *p*% dark,
  **randomly placed**. Readers imagine picking blindly. 1% feels unlikely, 10%
  still unlikely, 40% quite possible. The random placement conveys
  unpredictability.
- People judge **counts of discrete objects** (when there aren't too many) much
  better than **relative areas**.

## 2. Probability distributions and quantile dot plots

- For numeric outcomes (for example a predicted election margin with a margin of
  error), show the **probability distribution**. Shade the area for each outcome
  (such as "blue wins" 87% vs. "yellow wins" 13%) and mark the best estimate
  and the margin of error.
- Note that "+1 point, margin of error 1.76" sounds like a sure win, while the
  distribution shows a 13% chance of losing. Visualize it.
- **Quantile dot plot** (Kay et al. 2016): split the distribution into *n*
  equal-probability units, each drawn as a dot, and stack the dots to follow
  the curve. It combines discrete counting with the distribution's shape.
  - **Use few dots (about 10–50, often 10–20).** With too many, dots blur into a
    continuum and lose the counting advantage. 10 dots (10% each) can beat 50
    dots for lay readers despite the rounding error. *Trading a little
    mathematical precision for accurate perception is often worth it.*

## 3. Statistical vocabulary you must get right

- **Population** = the full, true state of the world. **Sample** = the subset you
  observe. **Sample size** n = the number of observations.
- **Parameters** (population mean, population SD) are unknowable. **Estimates**
  (sample mean, sample SD) are computed from the sample. A **point estimate** is
  a single estimated value.
- **Sampling distribution** = the distribution of an estimate over hypothetical
  repeated samples. Its width is the **standard error (SE)**.
- **SD vs. SE: never confuse them.**
  - **Standard deviation** describes the **spread of individual observations**.
    It is a property of the population.
  - **Standard error** describes the **precision of an estimate** (such as the
    mean). SE ≈ SD/√n, so it shrinks with sample size.
- **Confidence intervals** are multiples of the SE. A 95% CI ≈ mean ± 2 SE.
  Larger samples mean narrower CIs even with the same SD.

## 4. Error bars: always say what they show

The same data can give five visually different error bars: ±SD, ±SE, 80%,
95%, and 99% CI. They mean different things. **Every figure with error bars must
state what the bars represent** (SD, SE, or which CI level) in the caption or
legend. Ideally also say what the central point is (mean or median). Don't use
error bars to show population variability. Show the distribution instead (see
`distributions.md`).

## 5. Graded error bars and deterministic construal error

- **Deterministic construal error**: reading uncertainty displays as hard facts,
  for example assuming error bars mark the data's min and max, or that the
  estimate can't lie outside them. Good uncertainty visualization minimizes
  this.
- **Graded error bars** draw several confidence levels at once (for example 80%,
  95%, 99%) as overlaid bars. Lower confidence levels are **thicker and
  darker**. This makes it clear there is a *range* of plausibility rather than a
  hard edge.
- Tradeoff: grading adds visual noise. In a dense figure with many estimates,
  simple single-level bars may be better.

## 6. Comparing estimates: show the CI of the difference

- Whether two means differ "significantly" **cannot be reliably judged from
  overlapping or non-overlapping error bars**. Avoid those rules of thumb.
- To compare groups against a reference, **compute and plot confidence intervals
  for the differences** (for example each country's mean minus the US mean,
  adjusted for multiple comparisons such as Dunnett's). If the CI of a
  difference excludes zero, the difference is significant at that level. Draw a
  reference line at zero.

## 7. Error bar styling: caps, grading, strips, distributions

| Option | Pros | Cons |
|---|---|---|
| Graded error bars | show several confidence levels at once, reduce deterministic reading | more visual noise |
| Simple error bars | clean, good for many estimates | invite deterministic reading |
| **With caps** | mark exactly where the interval ends | add clutter with many bars |
| **Without caps** | equal emphasis on the whole interval, less clutter | ends less precise |
| Confidence strips (fading gradient) | convey that some values are more probable | very hard to read exact levels; can mislead about significance |
| Full confidence/posterior distributions | most complete | hard to integrate areas by eye; mitigate with quantile dots or shaded intervals |

Caps vs. no caps is largely taste. Leaning toward no caps when there are many
bars is reasonable.

## 8. Error bars on other charts

- Error bars combine with almost any 2D chart: points, bars, and both x and y
  directions on scatterplots (for example 90% CIs on both variables).
- **Bars ± SE** (the "dynamite plot") are common in science and technically
  correct. But they show **neither** the within-group variation **nor** the
  uncertainty of the mean especially well. Prefer showing the distribution
  (points, violins) plus a mean and CI.

## 9. Bayesian posteriors and credible intervals

- Frequentists report **confidence intervals**, and Bayesians report **posterior
  distributions** and **credible intervals**. The visualization strategies are
  largely the same.
- **Credible interval** (Bayesian): "where do we expect the true parameter to
  lie?" A 95% credible interval contains the true value with 95% probability,
  given the prior and the data.
- **Confidence interval** (frequentist): a statement about the **null
  hypothesis**: "how sure are we the parameter isn't zero?" Under repeated
  sampling, 95% of such intervals would contain the true value. A single CI
  either contains it or not. Illustrate with many CIs from repeated samples.
- In practice the two are often numerically similar. Bayesian estimates show
  **shrinkage** (extreme estimates pulled toward the overall mean). Bayesian
  thinking puts the emphasis on **effect magnitude**. Frequentist thinking
  invites a binary "effect or no effect" view.
- Since the posterior *is* the result, **show the whole posterior** with any
  distribution technique (histogram, density, boxplot, violin, ridgeline).
  Helpful additions:
  - shading under the curve for central 80/95/99% regions, and a point at the
    median,
  - **half-eye** = ridgeline (one-sided density) + graded interval bar
    underneath,
  - **eye** = violin + interval bar,
  - quantile dot plots.

## 10. Uncertainty of curve fits: bands and draws

- **Confidence band** around a fitted line: the range of fit lines compatible
  with the data at a given confidence level (state the level, for example 95%).
- Bands around straight lines are **curved** (narrowest near the data center)
  because both the intercept and the slope are uncertain. Show this by drawing
  **a set of alternative fits** sampled from the parameter posterior (around 15
  lines).
- **Graded confidence bands** (several levels) strengthen the sense of
  uncertainty and push readers to consider alternative trends.
- For **nonlinear fits** (splines etc.), the band hides the fact that plausible
  alternative curves are **wigglier** than the best fit, not just shifted. Drawing
  individual fitted draws shows this.

## 11. Hypothetical outcome plots (HOPs)

- **Animate** through a series of equally likely outcomes (Hullman, Resnick &
  Adar 2015). This avoids deterministic construal error because every frame is
  clearly only one possibility.
- Media: online (GIF, MP4, interactive) and live presentations. **Not print.**
  For print, show a few frames side by side as a schematic.
- Good for intuitive questions such as "if I pick one bar from A and one from B,
  which tastes better?" (53% vs. 47%) and for showing **individual alternative
  trend lines** one at a time instead of overlaid.
- **Transitions**: evidence suggests **smooth morphing between outcomes makes
  probability judgments harder** (Kale et al. 2018). Prefer **hard cuts**, very
  fast transitions, or fade in/out.
- **The frames must be representative.** A small unlucky sample of draws can
  reverse the apparent result. Show many draws, or check that the frame
  frequencies match the true probabilities.

## 12. Decision guide

| Goal or audience | Recommended |
|---|---|
| Single probability, lay audience | frequency grid (random icons or squares) |
| Distribution of outcomes, lay audience | quantile dot plot (about 10–20 dots), shaded outcome regions |
| Many estimates, expert audience | point + error bars (state what they are), graded if not too dense |
| Is A different from B / reference? | CI of the difference with a zero reference line |
| Bayesian results | posterior distributions: half-eye / eye / ridgeline with shaded intervals |
| Trend line uncertainty | confidence band (graded optional) or fitted draws |
| Nonlinear fit uncertainty | fitted draws (or HOP) to show the wiggliness |
| Online or talk, intuitive feel | hypothetical outcome plot (hard cuts, representative frames) |
| Avoid | unlabeled error bars, SD/SE confusion, judging significance by bar overlap, error bars as data spread |
