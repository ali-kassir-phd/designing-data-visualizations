# Color: scales, pitfalls, and accessibility

## Contents
1. The three jobs of color
2. Qualitative scales (distinguish)
3. Sequential scales (represent values)
4. Diverging scales (deviation from a midpoint)
5. Accent scales (highlight)
6. Ready-to-use palettes
7. Pitfall: encoding too much or irrelevant information
8. Pitfall: nonmonotonic (rainbow) scales for data values
9. Pitfall: not designing for color-vision deficiency
10. Color checklist

---

## 1. The three jobs of color

Color does one of three things in a figure, and each job needs a different kind
of scale:

| Job | Data | Scale type |
|---|---|---|
| **Distinguish** groups | unordered categories | qualitative |
| **Represent** values | numbers, ordered levels | sequential, or diverging if there is a meaningful midpoint |
| **Highlight** | a few elements that carry the story | accent (muted base + strong accent) |

Decide which job color is doing *before* picking colors. A lot of bad color use
comes from mixing up these jobs, for example using a rainbow (a distinguishing
palette) to represent values.

## 2. Qualitative scales (distinguish)

Use these for categories with no inherent order (countries, manufacturers,
species). A good qualitative scale has colors that:
- are **clearly distinct** from each other,
- are **equivalent**, so no single color jumps out, and
- **do not imply an order**. Colors that get steadily lighter or darker suggest
  a ranking that isn't there.

Example use: color bars (states sorted by growth) by region, so readers can see
that regions cluster.

## 3. Sequential scales (represent values)

Use these for quantitative values such as income, temperature, or speed. A good
sequential scale shows clearly:
1. which values are larger and which are smaller, and
2. **how far apart** two values are. So the scale must be perceived as changing
   **uniformly** across its whole range (perceptually uniform).

- **Single-hue**: for example dark blue → light blue.
- **Multi-hue**: follow gradients that occur in nature. Dark red → light yellow,
  dark blue → green → light yellow (viridis), dark purple → light green. Avoid
  unnatural ones such as dark yellow → light blue.
- A classic use is the **choropleth map**, where regions are colored by value.
  Show **missing data in a neutral gray** and say so in the caption.

## 4. Diverging scales (deviation from a midpoint)

Use these when values deviate in two directions from a meaningful neutral point:
positive vs. negative, or above vs. below 50%. A diverging scale is essentially a pair
of sequential ramps that meet at a shared **light midpoint color**.

- The midpoint must have **real meaning**: zero, 50% (majority threshold), 1 for
  ratios, a target value. A variable that is always positive can still justify a
  diverging scale if a meaningful midpoint exists.
- The scale must be **balanced**: light-to-dark progressions of equal length on
  both sides. Otherwise values on one side look bigger than equal deviations on
  the other.
- Common hue pairs: brown ↔ blue-green, pink ↔ yellow-green, blue ↔ red.

## 5. Accent scales (highlight)

Use these to make a few story-critical elements pop: highlight two states among
fifty, or one group of athletes among many.

- Accent scales pair **subdued base colors** with **stronger, darker, or more
  saturated** matching accents. You can build one by lightening or desaturating
  some colors of a qualitative palette and darkening others, by pairing grays
  with colors, or by using a ready-made accent palette (ColorBrewer "Accent").
- **The base colors must not compete with the accents.** A common mistake is a
  base palette that is too colorful. The simplest fix is to make **everything
  gray except the highlighted elements**.
- The same data can support different stories depending on what you highlight.
  Choose the highlight to match the message, and say it in the title.

## 6. Ready-to-use palettes

These are reasonable defaults. Their published color values are facts and can
be used freely.

- **Okabe–Ito** (qualitative, colorblind-safe, 8 colors). A strong
  default:
  `#E69F00` orange, `#56B4E9` sky blue, `#009E73` bluish green, `#F0E442` yellow,
  `#0072B2` blue, `#D55E00` vermillion, `#CC79A7` reddish purple, `#000000` black
  (`#999999` gray is often swapped in for black).
- **ColorBrewer** (colorbrewer2.org): qualitative (Dark2, Set2, Paired, Accent),
  sequential (Blues, Greens, YlOrRd, …), and diverging (BrBG, PiYG, RdBu, …).
  The site flags colorblind-safe options.
- **Viridis family** (viridis, magma, inferno, plasma, cividis): perceptually
  uniform sequential scales that remain readable for common color-vision
  deficiencies and in grayscale.
- Software default hue palettes (for example ggplot2's evenly spaced hues) are
  valid qualitative scales but are not colorblind-safe.

---

## 7. Pitfall: encoding too much or irrelevant information

Color has to serve a purpose, be clear, and not distract.

- **Too many categories.** Qualitative scales work best for **3–5 categories**.
  At **8–10 or more**, matching colors to legend entries becomes a burdensome
  puzzle, even if the colors are technically distinguishable. Coloring 50 states
  individually defeats the purpose of color.
  - **Use direct labeling instead of color when distinguishing more than about
    eight items.** Put text labels next to the points or lines.
  - Use color only for a **coarser grouping** (for example region instead of
    state), and label individual items directly.
  - You **don't have to label every point.** Label a representative subset or the
    items discussed in the text, and provide the full data as a table if readers
    need it.
- **Coloring for the sake of coloring.** A rainbow of colors on bars that are
  already identified by axis labels adds no insight and distracts.
- **Overly saturated colors.** Large areas of intense, saturated color are
  tiring to look at. They pull the eye away from labels and make it hard to
  compare bar ends against grid lines. **Keep big filled regions away from
  intense, fully saturated hues.** Prefer softer, partially desaturated fills for large areas.

## 8. Pitfall: nonmonotonic (rainbow) scales for data values

The popular rainbow (spectral or "jet") scale breaks both
requirements of a sequential scale (clear order and uniform differences):
- It is **effectively circular**. Both ends are similar dark reds, so the extremes
  don't look maximally different.
- It is **non-monotonic in lightness**. Converted to grayscale, it goes medium
  dark → light → very dark → medium dark. Changes are **non-uniform**: the
  yellow–light green–cyan stretch takes up about a third of the scale with little
  change, while dark blue is squeezed into a narrow band.
- In real data it **hides real features and highlights arbitrary ones** (for
  example a random threshold such as ~75% shows up as a sharp color boundary).
- Its colors are oversaturated, so it's uncomfortable to look at for long.

**Fix:** use a monotonic, perceptually uniform sequential scale (viridis family,
single-hue or ColorBrewer sequential, Heat), or a balanced diverging scale when
there's a meaningful midpoint. **Check any continuous scale in grayscale.**
Lightness should change steadily from one end to the other.

## 9. Pitfall: not designing for color-vision deficiency

- About **8% of men and 0.5% of women** have a color-vision deficiency (CVD).
  People with CVD see colors but can't tell certain ones apart:
  - **red–green**: deuteranomaly/deuteranopia (green perception impaired, the
    most common form) and protanomaly/protanopia (red impaired),
  - **blue–yellow**: tritanomaly/tritanopia (blue impaired, rare).
  - "-anomaly" means reduced perception and "-anopia" means absent perception.
- **Sequential scales** that run steadily dark → light are generally safe. Under
  any CVD the colors change but the lightness gradient still conveys magnitude.
- **Diverging scales** are risky. **Red vs. green**, the strongest contrast for
  normal vision, nearly vanishes for deutans and protans. **Blue vs. green**
  vanishes for tritans. Small tweaks often fix this. ColorBrewer **PiYG**
  (pink ↔ yellow-green) still reads as "red vs. green" to most people but works
  for all CVD types, because the pink carries blue (visible to deutans and
  protans) and the green carries yellow and red (visible to tritans). Blue ↔
  orange/red diverging scales are another common CVD-safe option.
- **Qualitative scales** are hardest, because many colors must stay distinct under
  every CVD type. **Okabe–Ito** (8 colors, listed above) was designed for this,
  and eight is about the most items you should color-code anyway.
- **Safe palettes are not magic bullets.** **Element size matters**: colors are far
  easier to tell apart on large areas than on thin lines or small points, and
  CVD makes this worse. A CVD-safe palette on hairlines can still fail.
- **Test the actual figure in a CVD simulator**, not just the palette. Check
  deuteranomaly, protanomaly, and tritanomaly, plus grayscale. Tools: Coblis or
  other online simulators, R `colorblindr`/`colorspace`, Python
  `colorspacious`/`daltonlens`, or this skill's `scripts/check_palette.py` for
  palette-level checks.
- Also use **redundant coding** (shapes, line types, direct labels, position) so
  that color is never the only carrier of information. See `figure-design.md` §
  Redundant coding.

## 10. Color checklist

- [ ] What is color doing here: distinguish, represent, or highlight? Is the
      scale type right for that job?
- [ ] Qualitative: about 3–5 categories (8 max), or else direct labels or grouping?
      Equivalent, unordered-looking colors?
- [ ] Sequential: monotonic in lightness and perceptually uniform? No rainbow?
- [ ] Diverging: meaningful midpoint, light center, balanced arms, not
      red-vs-green?
- [ ] Accent: are the base colors drab enough not to compete?
- [ ] Missing data shown in neutral gray and explained?
- [ ] Checked under CVD simulation and grayscale? Is information also carried
      redundantly?
- [ ] Is any color purely decorative? Remove it. Any large areas of oversaturated color? Soften them.
- [ ] Are colored elements large enough (not hairlines or tiny points) for colors to be told apart?
