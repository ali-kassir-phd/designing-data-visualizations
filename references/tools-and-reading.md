# Implementation tools and further reading

Use the library table to turn the guidance in this skill into code. Use the
reading list when the user asks where to learn more.

## Library mapping for techniques in this skill

| Technique | R | Python | JavaScript / web |
|---|---|---|---|
| Grammar-of-graphics base | ggplot2 | plotnine, Altair; matplotlib/seaborn | Vega-Lite, Observable Plot, D3 |
| Direct labels without overlap | ggrepel, directlabels | adjustText; manual `ax.annotate` | D3 label placement; Plot `text` mark |
| Ridgeline plots | ggridges | joypy; seaborn FacetGrid with overlap | D3 custom; Vega-Lite with offset |
| Sina plots | ggforce `geom_sina` | seaborn `swarmplot`/`stripplot` (approximation) | custom |
| Ellipses around groups, parallel sets | ggforce | matplotlib `Ellipse`; plotly `parcats` | D3 / plotly |
| Treemaps | treemapify | squarify; plotly treemap | d3-hierarchy treemap |
| Mosaic plots | ggmosaic, base `mosaicplot` | statsmodels `mosaic` | custom |
| Hex bins / 2D bins | hexbin, `geom_hex`, `geom_bin2d` | matplotlib `hexbin`, `hist2d` | d3-hexbin |
| Contours of 2D density | `geom_density_2d` | seaborn `kdeplot` (2D) | d3-contour |
| LOESS / GAM smoothing | `geom_smooth`, mgcv | statsmodels `lowess`, pygam | — (precompute) |
| STL decomposition | `stl()` | statsmodels `STL` | — |
| Uncertainty: half-eyes, intervals, quantile dots | tidybayes, ggdist | arviz; custom | custom |
| Fitted draws, HOPs | ungeviz, gganimate | matplotlib animation; plotly frames | D3 transitions (prefer hard cuts) |
| Multiple comparisons CIs (Dunnett) | emmeans | statsmodels / scipy `dunnett` | — |
| Maps, projections | sf, ggspatial | geopandas, cartopy | d3-geo, Vega-Lite projections |
| Tile grid maps / geofacets | statebins, geofacet | custom grid layout | custom |
| Compound figure alignment | cowplot, patchwork, egg | matplotlib `subplot_mosaic`, `constrained_layout` | CSS grid / Vega concat |
| Color: CVD simulation, palettes | colorspace, colorblindr, viridis, RColorBrewer | colorspacious, daltonlens, matplotlib viridis, palettable | d3-scale-chromatic |
| Themes (content vs. design) | `theme_*()`, cowplot themes, ggthemes | matplotlib style sheets / rcParams, seaborn themes | Vega config, CSS |

## Further reading

**Thinking about data and visualization**
- Alberto Cairo, *The Truthful Art* (2016): broad introduction aimed at
  journalists. Covers distributions, trends, uncertainty, maps, and basic
  statistics.
- Stephen Few, *Show Me the Numbers* (2012): business-oriented, more material
  and depth than Knaflic.
- Cole Nussbaumer Knaflic, *Storytelling with Data* (2015): polished business
  graphics guide. Light on distributions, trends, and uncertainty.

**Programming**
- Kieran Healy, *Data Visualization: A Practical Introduction* (2018):
  ggplot2.
- Scott Murray, *Interactive Data Visualization for the Web*, 2nd ed. (2017):
  D3.
- Jake VanderPlas, *Python Data Science Handbook* (2016): matplotlib, Seaborn.
- Hadley Wickham & Garrett Grolemund, *R for Data Science* (2017).

**Statistics**
- Diez, Barr & Çetinkaya-Rundel, *OpenIntro Statistics* (open textbook).
- Susan Holmes & Wolfgang Huber, *Modern Statistics for Modern Biology*
  (2018, freely available).

**Historical**
- William S. Cleveland, *Visualizing Data* (1993) and *The Elements of Graphing
  Data* (2nd ed., 1994). The second popularized the Cleveland dot plot.
- Edward R. Tufte, *Envisioning Information* (1990): popularized small
  multiples.
- Edward R. Tufte, *The Visual Display of Quantitative Information* (2nd ed.,
  2001): chart junk, data–ink ratio, sparklines, the first slopegraph. Some of
  its advice (excessive minimalism) hasn't aged well.

**Related topics**
- Joshua Schimel, *Writing Science* (2011): storytelling in technical writing.
- Jonathan Schwabish, *Better Presentations* (2016): slides and talks.
- Maureen C. Stone, *A Field Guide to Digital Color* (2003).
- Colin Ware, *Information Visualization*, 3rd ed. (2012): perception.

**Research cited in this skill**
- Bergstrom & West (2016), "The Principle of Proportional Ink".
- Okabe & Ito (2008), Color Universal Design.
- Brewer, ColorBrewer 2.0 (colorbrewer2.org).
- Stone, Albers Szafir & Setlur (2014): color difference depends on mark size.
- Haroz, Kosara & Franconeri (2015, ISOTYPE; 2016, connected scatterplots).
- Kay et al. (2016): quantile dot plots.
- Hullman, Resnick & Adar (2015); Kale et al. (2018): hypothetical outcome
  plots.
- Cleveland (1979): LOESS. Cleveland et al. (1990): STL.
- Carr et al. (1987): hexagon binning.
- Sidiropoulos et al. (2018): sina plots.
- Bateman et al. (2010); Borgo et al. (2012): embellishment and memorability.
