# Visualizing geospatial data

Maps are intuitive for
readers but hard to design well. Key decisions: the **projection** (preserve
angles or areas?), which **layers** to show, whether a **choropleth** is honest
for the variable, and whether a **cartogram** would serve better.

## Contents
1. Geographic coordinates basics
2. Projections
3. Insets and relocated regions (e.g. Alaska and Hawaii)
4. Layers, scale bar, north arrow
5. Mapping data onto aesthetics on maps
6. Choropleth maps
7. Cartograms
8. Map checklist

---

## 1. Geographic coordinates basics

- Positions on Earth are **longitude** (east–west angle; meridians run pole to
  pole, 0° at Greenwich, ±180° near the date line), **latitude** (north–south
  angle; parallels, 0° at the equator, ±90° at the poles), and **altitude**.
- These are defined relative to a **datum**. **WGS 84** is the one GPS uses.
  Unprojected lon/lat in WGS 84 is **EPSG:4326**.
- Registries (EPSG, ESRI) catalog projections by code. See epsg.io or
  spatialreference.org.

## 2. Projections

Flattening a sphere always distorts something. A projection can preserve
**angles (conformal)** or **areas (equal-area)**, never both. Some preserve
distances from a reference point or line. **Compromise** projections accept
some of both kinds of distortion for a balanced look.

| Projection | Property | Use / caveat |
|---|---|---|
| Lon/lat drawn as Cartesian x/y (equirectangular) | neither | distorts areas and angles; avoid for real maps |
| **Mercator** | conformal | navigation; **huge area distortion near the poles** (Greenland looks as big as Africa, which is about 14× larger). Avoid for world thematic maps |
| Transverse Mercator | conformal | detailed maps of small areas (a few degrees of longitude) |
| Web Mercator | ~conformal | online tile maps (Google Maps etc.); same area issues |
| **Interrupted Goode homolosine** | equal-area (angles approximately kept) | accurate global areas; cuts oceans, Greenland, Antarctica |
| **Robinson**, **Winkel tripel** | compromise | attractive whole-world maps |
| **Albers equal-area conic** | equal-area | countries and continents in mid-latitudes (for example the contiguous US, ESRI:102003) |

**Rule:** if the map's message involves comparing **areas** or anything colored
by region (choropleths), use an **equal-area** projection. Use conformal
projections when local shape and direction matter (navigation, small regions).

## 3. Insets and relocated regions (e.g. Alaska and Hawaii)

- Mapping distant parts of a country at true positions wastes space on empty
  ocean and distorts the far-off parts.
- Common practice is to project the remote parts separately and **move** them
  near the main map. That's fine.
- **Rescaling them is misleading**, which is **bad**. A common US map shrinks
  Alaska to about 35% of its linear size (about 12% of its area) so it looks like
  a typical state. **Move but don't shrink**, or state the scale change clearly
  with its own scale bar.

## 4. Layers, scale bar, north arrow

- Maps are built from **layers**, bottom to top, for example: terrain or water →
  roads → data (points, highlight boxes) → place labels, scale bar, and north
  arrow.
- **Include only layers that support the message.** Terrain distracts on a
  voting-district map. Satellite imagery may be essential for a rooftop solar
  map.
- **Generally add a scale bar** (feature size) and a **north arrow**
  (orientation).
- When background tiles or map data come from third parties (for example
  OpenStreetMap, ODbL), **credit them as their licenses require**.

## 5. Mapping data onto aesthetics on maps

Everything in `foundations.md` applies. Points get their geographic position,
and other variables can go on color, shape, and so on. Example: turbines
colored by construction year and shaped by project gives an at-a-glance history
of development. Use an overview map with highlight rectangles plus zoomed-in
detail maps.

## 6. Choropleth maps

Regions colored by a data value.

**Color scale direction and background**
- On a **light background** (print on white paper), **darker = higher** is
  intuitive.
- On a **dark background** (screen), **lighter = higher** works if the light end
  is in the **red–yellow "glowing"** range.
- Use sequential scales, or diverging scales for meaningful midpoints (see
  `color.md`). Show missing data in neutral gray and say so.

**What to color by**
- Choropleths work best for **densities**: quantity ÷ area (people per km²).
  Readers perceive bigger areas as more of something (see proportional ink), and
  densities correct for that.
- **Non-density values** (median income, percentages) can be OK **only if**
  either:
  1. all regions are of **roughly similar size and shape**, or
  2. regions are **small relative to the map** and the variable changes over
     scales **larger than individual regions**.
- When neither holds, large sparse regions dominate the visual impression. For
  example a state-level income map makes high income look common because one
  huge, nearly empty state is high-income. That is **bad**. Use counties (finer
  units), a cartogram, or a non-map chart.

**Continuous vs. binned colors**
- Continuous scales look nice but specific colors are **hard to match back** to
  values.
- **Binning into about 4–6 classes** makes each color uniquely recognizable at
  the cost of some detail. This is often the better choice for reading values.

## 7. Cartograms

- **Area cartogram**: regions are deformed so their area ∝ another quantity
  (usually population). Regions stay recognizable while the visual weight is
  corrected. Dense coastal states grow and sparse western states shrink.
- **Cartogram heatmap** (tile grid map): each region is an **equal square**
  placed roughly where it lies geographically. It doesn't correct for population,
  but it gives **every region equal weight**, unaffected by its area or shape.
- **Geofacet / small-multiple map**: put **a small chart per region** (for example
  an unemployment time series per state) in a grid laid out by geography. Readers
  who know the geography find panels faster than in alphabetical order, and
  regional similarity between neighbors becomes visible.

## 8. Map checklist

- [ ] Projection suitable: equal-area for thematic or area-based messages, no
      Mercator for world-scale comparisons?
- [ ] Remote regions moved but **not rescaled** (or rescaling clearly marked)?
- [ ] Only layers that support the message? Scale bar and north arrow where
      relevant?
- [ ] Choropleth variable is a density, or are regions similar or small enough?
- [ ] Would large sparse regions dominate? Consider a cartogram or tile map.
- [ ] Binned (4–6 classes) or continuous color chosen on purpose? Light/dark
      direction suits the background?
- [ ] Missing regions in neutral gray, explained?
- [ ] Data and tile sources credited?
