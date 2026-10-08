# Telling a story and making a point

Use this when a figure, a set of figures, a report, a
paper, a dashboard narrative, or a slide deck has to *communicate* an insight
to an audience.

## Contents
1. Why a story
2. Story arcs and how figures fit in
3. Make a figure for the generals
4. Build up toward complex figures
5. Make figures memorable without hurting clarity
6. Be consistent, but don't be repetitive
7. Go from raw data to derived quantities
8. How many figures
9. Story checklist

---

## 1. Why a story

- Most visualization exists to **communicate an insight to an audience**. That
  takes a clear, engaging story built from **facts and logical reasoning**. A
  story here is not spin and not fabrication.
- **Every communication creates a story in the audience's mind.** If you don't
  provide one, they'll invent one, and their version may be unflattering
  (dull, mistaken, or incompetent).

## 2. Story arcs and how figures fit in

- A story is a sequence of observations or events, ordered to build **tension**
  and then **resolve** it. That flow is the **story arc**.
- Common formats:
  - **Opening – Challenge – Action – Resolution**,
  - **Lead – Development – Resolution** (or just Lead – Development): newspaper
    style, with the main point given up front,
  - **Action – Background – Development – Climax – Ending**: pulls the audience
    in fast without revealing the resolution.
  (For writing guidance aimed at scientists and analysts, see Schimel,
  *Writing Science*.)
- **A single static figure rarely tells a whole story.** Usually one figure
  illustrates one part (opening, challenge, or resolution), and **a sequence of
  figures carries the arc**. Example: figure 1 shows exponential growth that
  suddenly stalls (challenge: *why?*), and figure 2 adds a competing series whose
  launch coincides with the stall (resolution).
- **One-figure stories** must contain both the challenge and the resolution. They
  work like a "lead" and suit short-attention media (social posts). In talks,
  splitting the story into challenge and resolution figures often has more
  impact, even if the second figure contains the first.

## 3. Make a figure for the generals

Two misconceptions to avoid: (1) that the audience can see your figure and
immediately infer your point, and (2) that the audience can rapidly process
complex displays. **Neither is true.**

- **"Make a figure for the generals":** busy, smart decision-makers (reviewers,
  editors, managers, funders) should grasp each figure's point **at a glance**.
  The issue is time, not intelligence.
- **Simplify relentlessly.** Remove everything tangential to the story. Only the
  important points should remain. **Don't expect any audience to decode an
  intricate display quickly.**
- Resist piling on dimensions just because modern tools make it easy. An
  impressive multi-encoding chart (position + size + color + trend lines) often
  conveys nothing. **If the story is "airlines A and B have the shortest delays",
  a simple sorted bar chart is the right figure.** A second simple chart can
  answer the obvious follow-up question ("are they major carriers?").
- It's fine to **discard data dimensions** that are tangential to the story, even
  ones you have and could show. *When you try to show too much at once, you may
  end up showing nothing.*
- Use plain-language labels, not internal jargon or variable codes.

## 4. Build up toward complex figures

- When a complex figure is truly needed, **first show a simplified subset**, then
  the full version. **Never jump straight to a highly complex figure**,
  especially in presentations.
- For **small multiples**, show **one panel alone first** (for example one
  airline at one airport by weekday), then the full grid. Once one panel is
  understood, the grid is easy.

## 5. Make figures memorable without hurting clarity

- Very clean, simple charts can be **generic and forgettable**. Ten similar bar
  charts blur together.
- Research (Bateman et al. 2010; Borgo et al. 2012): figures with more visual
  complexity and uniqueness are **remembered better**. Too much complexity hurts quick
  overview and fine comparisons. A memorable but confusing figure is art, not
  good visualization. **Balance memorable and clear.** Technical venues need less
  memorability than newspapers and blogs.
- **Isotype plots**: show the values as **repeated pictograms** (for example
  one dog icon = 5 million households). The figure still works as a bar chart
  but is more memorable and immediately signals the topic.
- **Use images to *represent* data, not to *decorate*.** Pictures as mere
  adornment or as axis labels tend to distract (Haroz, Kosara & Franconeri 2015).

## 6. Be consistent, but don't be repetitive

- Figures in one story should share a **consistent visual language** (the same
  colors and order for the same groups, consistent fonts and theme). See
  `figure-design.md` §6.
- But **different analyses should look visibly different**, so readers notice
  where one result ends and the next begins. **Aim for a different visualization
  type for each distinct analysis**: bar chart, then scatter, then boxplot, then
  line. All-bar-chart reports blur together.
- Watch out when every part of a story uses the same raw data type (for example
  stock prices over time). Show the raw time series once, then switch to a
  different form (such as a bar chart of % increase) for the comparison, instead
  of another near-identical line chart.

## 7. Go from raw data to derived quantities

- **Start with the figure closest to the raw data, then move to increasingly
  derived quantities** (percent changes, averages, model coefficients).
- Derived quantities summarize well but are less intuitive. Shown before the
  raw data, they are hard to follow. Showing *only* raw data makes the figure
  count explode and gets repetitive.

## 8. How many figures

| Venue | Figures |
|---|---|
| Short blog post, social post | 1 |
| Scientific paper | 3–6 (move the rest to supplementary material) |
| Hour-long talk | about 3 distinct stories, each with ≤ 3–6 figures |
| Book, thesis, long report | one story per chapter or section, each with ≤ 3–6 figures |

Document all the evidence, but don't wear the audience out with many
similar-looking figures.

## 9. Story checklist

- [ ] What is the one-sentence point of each figure? Is it in the title?
- [ ] Is there a story arc (challenge → resolution) across the figure sequence?
- [ ] Could a busy "general" get each figure's point in seconds?
- [ ] Have tangential dimensions been removed?
- [ ] Are complex figures preceded by a simpler build-up?
- [ ] Consistent visual language, but different chart types for different
      analyses?
- [ ] Raw data first, derived summaries later?
- [ ] Figure count suited to the venue?
- [ ] Any pictograms represent data rather than decorate?
