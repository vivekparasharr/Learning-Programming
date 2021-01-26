
# seaborn builds on top of matplotlib and integrates closely with pandas data structures

# seaborn namespace is flat; all of the functionality is accessible at the top level
# But the code itself is hierarchically structured, with modules for 
# “relational”, “distributional”, and “categorical” data
# https://seaborn.pydata.org/api.html

import seaborn as sns
sns.set_theme() # more on https://seaborn.pydata.org/tutorial/aesthetics.html

# There’s nothing special about these datasets: they are just pandas dataframes, and we could have loaded them with pandas.read_csv() or built them by hand 


# Seaborn example datasets
import seaborn as sns
sns.get_dataset_names()
tips = sns.load_dataset("tips")
tips.plot(x='total_bill', y='tip', kind='scatter')



### Relational plots

# relplot function used to plot scatter plot 
# relplot - Figure-level interface for drawing relational plots onto a FacetGrid
tips = sns.load_dataset("tips")
sns.relplot(
    data=tips, # if we dont specify kind then we get a scatter plot
    x="total_bill", y="tip", col="time", # col - separate charts for different "time" column wise
    hue="smoker", style="smoker", size="size",
) # hue - different colors, style - different marker style, size - different marker size

# scatterplot funciton used to plot scatter plot
# scatterplot - Draw a scatter plot with possibility of several semantic groupings.
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", style="day", size="size",)

# relplot function used to plot line plot
dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line", # line plot for relationships where one variable represents a measure of time
    x="time", y="firing_rate", col="align",
    hue="choice", style="choice", size="coherence",
    facet_kws=dict(sharex=False),
)

# lineplot function used to plot line plot
# lineplot - Draw a line plot with possibility of several semantic groupings.
sns.lineplot(data=dots, x="time", y="firing_rate", hue="choice", style="choice", )





# statistical analysis
# distplot
import seaborn as sns, numpy as np
sns.set(); np.random.seed(0)
x = np.random.randn(100)
ax = sns.distplot(x)

# displot() supports several approaches to visualizing distributions
# include classic techniques like histograms and computationally-intensive approaches like kernel density estimation
sns.displot(data=tips, x="total_bill", col="time", kde=True)

# calculating and plotting the empirical cumulative distribution function of the data
sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)

# Statistical estimation and error bars
fmri = sns.load_dataset("fmri")
sns.relplot(data=fmri, kind="line",
            x="timepoint", y="signal", col="region", 
            hue="event", style="event")




### Distribution plots
penguins = sns.load_dataset("penguins")

# displot - Figure-level interface for drawing distribution plots onto a FacetGrid.
# displot([data, x, y, hue, row, col, …])
# univariate
sns.displot(data=penguins, x="flipper_length_mm")
sns.displot(data=penguins, x="flipper_length_mm", kde=True) # possible to add a KDE curve
sns.displot(data=penguins, x="flipper_length_mm", kind="kde") # kind parameter to select a different representation
sns.displot(data=penguins, x="flipper_length_mm", kind="ecdf") # three main plot kinds; histograms, kernel density estimates, empirical cumulative distribution functions
# bivariate
sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm") # To draw a bivariate plot, assign both x and y
sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde")
sns.displot(data=penguins, x="flipper_length_mm", y="bill_length_mm", kind="kde", rug=True) # can also show individual observations with a marginal “rug”

# figure is constructed using a FacetGrid, meaning that you can also show subsets on distinct subplots, or “facets”
# Each kind of plot can be drawn separately for subsets of data using hue mapping:
sns.displot(data=penguins, x="flipper_length_mm", hue="species", kind="kde") 
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack") 
sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde") 

# Because the figure is drawn with a FacetGrid, col can be used to show subsets on distinct subplots, or “facets”
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="sex", kind="kde")

# Because the figure is drawn with a FacetGrid, you control its size and shape with the height and aspect parameters, axis labels, axis titles
sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="sex", kind="kde", height=4, aspect=.7,)
g.set_axis_labels("Density (a.u.)", "Flipper length (mm)")
g.set_titles("{col_name} penguins")

# histplot - Plot univariate or bivariate histograms to show distributions of datasets.
# histplot([data, x, y, hue, weights, stat, …])
## univariate
sns.histplot(data=penguins, x="flipper_length_mm", binwidth=3, kde=True) # vertical bars
sns.histplot(data=penguins, y="flipper_length_mm", bins=10, fill=False, element="step") # horizontal bars
sns.histplot(data=penguins) # If neither x nor y is assigned, the dataset is treated as wide-form, and a histogram is drawn for each numeric column
sns.histplot(data=penguins, x="flipper_length_mm", hue="species") # You can otherwise draw multiple histograms from a long-form dataset with hue mapping
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack") # The default approach to plotting multiple distributions is to “layer” them, but you can also “stack” them
sns.histplot(penguins, x="flipper_length_mm", hue="species", element="step") # Overlapping bars can be hard to visually resolve. A different approach would be to draw a step function
sns.histplot(penguins, x="flipper_length_mm", hue="species", element="poly") # You can move even farther away from bars by drawing a polygon with vertices in the center of each bin

# To compare the distribution of subsets that differ substantially in size, use indepdendent density normalization
sns.histplot(penguins, x="bill_length_mm", hue="island", element="step", stat="density", common_norm=False,)

# It’s also possible to normalize so that each bar’s height shows a probability, which make more sense for discrete variables
tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="size", stat="probability", discrete=True)

# You can even draw a histogram over categorical variables (although this is an experimental feature)
sns.histplot(data=tips, x="day", shrink=.8)

# Real-world data is often skewed. For heavily skewed distributions, it’s better to define the bins in log space. 
planets = sns.load_dataset("planets")
sns.histplot(data=planets, x="distance", log_scale=True)

# cumulative histograms: cumulative=True

## bivariate
# When both x and y are assigned, a bivariate histogram is computed and shown as a heatmap
sns.histplot(penguins, x="bill_depth_mm", y="body_mass_g", hue="species")
# one of the variables is discrete
sns.histplot(penguins, x="bill_depth_mm", y="species", hue="species", legend=False)
# bivariate histogram accepts all of the same options for computation as its univariate counterpart, using tuples to parametrize x and y independently
sns.histplot(planets, x="year", y="distance", bins=30, 
             discrete=(True, False), log_scale=(False, True),)
#legend - annotate the colormap, add a colorbar
sns.histplot(
    planets, x="year", y="distance", bins=30, 
    discrete=(True, False), log_scale=(False, True),
    cbar=True, cbar_kws=dict(shrink=.75),)


# kdeplot - Plot univariate or bivariate distributions using kernel density estimation.
# kdeplot([x, y, shade, vertical, kernel, bw, …])
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")

# ecdfplot - Plot empirical cumulative distribution functions.
# ecdfplot([data, x, y, hue, weights, stat, …])
sns.ecdfplot(data=penguins, x="bill_length_mm", hue="species", stat="count", complementary=True) # stat - Distribution statistic to compute, complementary - if True, use the complementary CDF

# rugplot - Plot marginal distributions by drawing ticks along the x and y axes.
# rugplot([x, height, axis, ax, data, y, hue, …])
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
sns.rugplot(data=tips, x="total_bill", y="tip", hue="time", height=-.02, clip_on=False) # we represent a third variable with hue mapping

# Show the density of a larger dataset using thinner lines and alpha blending:
diamonds = sns.load_dataset("diamonds")
sns.scatterplot(data=diamonds, x="carat", y="price", s=5)
sns.rugplot(data=diamonds, x="carat", y="price", lw=1, alpha=.005)

# distplot - DEPRECATED: Flexibly plot a univariate distribution of observations.
# distplot([a, bins, hist, kde, rug, fit, …])





### Categorical plots
# https://seaborn.pydata.org/api.html
# catplot(*[, x, y, hue, data, row, col, …]) - Figure-level interface for drawing categorical plots onto a FacetGrid.
## Categorical scatterplots:
# stripplot(*[, x, y, hue, data, order, …]) - Draw a scatterplot where one variable is categorical.
# swarmplot(*[, x, y, hue, data, order, …]) - Draw a categorical scatterplot with non-overlapping points.
## Categorical distribution plots:
# boxplot(*[, x, y, hue, data, order, …]) - Draw a box plot to show distributions with respect to categories.
# violinplot(*[, x, y, hue, data, order, …]) - Draw a combination of boxplot and kernel density estimate.
# boxenplot(*[, x, y, hue, data, order, …]) - Draw an enhanced box plot for larger datasets.
## Categorical estimate plots:
# pointplot(*[, x, y, hue, data, order, …]) - Show point estimates and confidence intervals using scatter plot glyphs.
# barplot(*[, x, y, hue, data, order, …]) - Show point estimates and confidence intervals as rectangular bars.
# countplot(*[, x, y, hue, data, order, …]) - Show the counts of observations in each categorical bin using bars.

# swarm plot - a scatter plot that adjusts the positions of the points along the categorical axis so that they don’t overlap
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

# Alternately, you could use kernel density estimation to represent the underlying distribution that the points are sampled from:
sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

# Or you could show only the mean value and its confidence interval within each nested category
sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")

sns.set_theme(style="ticks")
exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise, kind="bar") # kind - scatter plots (strip, swarm), distribution plots (box, violin, boxen), estimate plots (point, bar, count)

# Facet along the columns to show a third categorical variable
g = sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=exercise,
                height=5, aspect=.8) # Use a different height and aspect ratio for the facets

# Make many column facets and wrap them into the rows of the grid
titanic = sns.load_dataset("titanic")
g = sns.catplot(x="alive", col="deck", col_wrap=4,
                data=titanic[titanic.deck.notnull()],
                kind="count", height=2.5, aspect=.8)

# Plot horizontally and pass other keyword arguments to the plot function
g = sns.catplot(x="age", y="embark_town",
                hue="sex", row="class",
                data=titanic[titanic.embark_town.notnull()],
                orient="h", height=2, aspect=3, palette="Set3",
                kind="violin", dodge=True, cut=0, bw=.2)

# Use methods on the returned FacetGrid to tweak the presentation
g = sns.catplot(x="who", y="survived", col="class",
                data=titanic, saturation=.5,
                kind="bar", ci=None, aspect=.6)
(g.set_axis_labels("", "Survival Rate")
  .set_xticklabels(["Men", "Women", "Children"])
  .set_titles("{col_name} {col_var}")
  .set(ylim=(0, 1))
  .despine(left=True))









# Regression plots
# lmplot(*[, x, y, data, hue, col, row, …]) - Plot data and regression model fits across a FacetGrid.
# lmplot() is a figure-level function that combines regplot() and FacetGrid
# regplot(*[, x, y, data, x_estimator, …]) - Plot data and a linear regression model fit.
# regplot() is an axes-level function 
# residplot(*[, x, y, data, lowess, …]) - Plot the residuals of a linear regression.

# enhance a scatterplot by including a linear regression model (and its uncertainty) 
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")

# Plot a simple linear relationship between two variables
tips = sns.load_dataset("tips")
g = sns.lmplot(data=tips, x="total_bill", y="tip")

# Condition on a third variable and plot the levels in different colors
g = sns.lmplot(data=tips, x="total_bill", y="tip", 
               hue="smoker", markers=["o", "x"], 
               palette="Set1", # palette=dict(Yes="g", No="m") - custom palette using a dictionary
               height=6, aspect=.4, x_jitter=.1)

# Plot the levels of the third variable across different columns
g = sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips)

# Wrap the levels of the column variable into multiple rows
g = sns.lmplot(x="total_bill", y="tip", col="day", hue="day",
               data=tips, col_wrap=2, height=3)

# Condition on two variables to make a full grid
g = sns.lmplot(x="total_bill", y="tip", row="sex", col="time",
               data=tips, height=3)

# Discrete data
# It’s possible to fit a linear regression when one of the variables takes discrete values
# however, the simple scatterplot produced by this kind of dataset is often not optimal
sns.lmplot(x="size", y="tip", data=tips,
           x_jitter=.05, # One option is to add some random noise (“jitter”) to the discrete values to make the distribution of those values more clear
           x_estimator=np.mean); # A second option is to collapse over the observations in each discrete bin to plot an estimate of central tendency along with a confidence interval

# Fitting different kinds of models - when simple linear regression is not good enough
anscombe = sns.load_dataset("anscombe")
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});

# fit a polynomial regression model to explore simple kinds of nonlinear trends in the dataset
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80});

# In the presence of outliers, it can be useful to fit a robust regression, which uses a different loss function to downweight relatively large residuals
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80});

# logistic regression - When the y variable is binary 
tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03,
           ci=None); # confidence interval around the regression line is computed using a bootstrap procedure, you may wish to turn this off for faster iteration

# fit a nonparametric regression using a lowess smoother
# This approach has the fewest assumptions, although it is computationally intensive
# lowess - locally weighted scatterplot smoothing
# methodology - fitting simple models to localized subsets of the data to build up a function that describes the deterministic part of the variation in the data, point by point
sns.lmplot(x="total_bill", y="tip", data=tips,
           lowess=True);

# residplot() function can be a useful tool for checking whether the simple regression model is appropriate for a dataset
# It fits and removes a simple linear regression and then plots the residual values for each observation
# Ideally, these values should be randomly scattered around y = 0
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});
# If there is structure in the residuals, it suggests that simple linear regression is not appropriate
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80});







### Matrix plots
## heatmap(data, *[, vmin, vmax, cmap, center, …]) - Plot rectangular data as a color-encoded matrix.
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 12)
normal_data = np.random.randn(10, 12)
ax = sns.heatmap(uniform_data,
                 vmin=0, vmax=1, # Change the limits of the colormap
                 center=0) # Plot a heatmap for data centered on 0 with a diverging colormap

# Plot a dataframe with meaningful row and column labels
flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights
                 , annot=True, fmt="d" # Annotate each cell with the numeric value using integer formatting
                 , linewidths=.5 # Add lines between each cell
                 , cmap="YlGnBu" # Use a different colormap
                 , center=flights.loc["Jan", 1955]) # Center the colormap at a specific value

# Plot every other column label and don’t plot row labels
data = np.random.randn(50, 20)
ax = sns.heatmap(data, xticklabels=2, yticklabels=False
                 , cbar=False) # Don’t draw a colorbar

# Use different axes for the colorbar
grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(flights, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "horizontal"})

# Use a mask to plot only part of a matrix
corr = np.corrcoef(np.random.randn(10, 200))
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True)
    
## clustermap(data, *[, pivot_kws, method, …]) - Plot a matrix dataset as a hierarchically-clustered heatmap.
# Plot a clustered heatmap
import seaborn as sns; sns.set_theme(color_codes=True)
iris = sns.load_dataset("iris")
species = iris.pop("species")
lut = dict(zip(species.unique(), "rbg"))
row_colors = species.map(lut)
g = sns.clustermap(iris,
                   figsize=(7, 5), # Change the size and layout of the figure
                   row_cluster=False,
                   dendrogram_ratio=(.1, .2),
                   cbar_pos=(0, .2, .03, .4),
                   row_colors=row_colors, # Add colored labels to identify observations
                   cmap="mako", vmin=0, vmax=10, # Use a different colormap and adjust the limits of the color range
                   metric="correlation", # Use a different similarity metric
                   method="single", # Use a different clustering method
                   #standard_scale=1, # Standardize the data within the columns
                   z_score=0) # Normalize the data within the rows






# Composite views onto multivariate datasets
# joinplot - plots the joint distribution between two variables along with each variable’s marginal distribution
penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

# another example
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg");

# pairplot(), takes a broader view: it shows joint and marginal distributions for all pairwise relationships and for each variable, respectively
sns.pairplot(data=penguins, hue="species")





### FacetGrid
# https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid
# class seaborn.FacetGrid(data, *, row=None, col=None, hue=None, col_wrap=None, 
#   sharex=True, sharey=True, height=3, aspect=1, palette=None, row_order=None, 
#   col_order=None, hue_order=None, hue_kws=None, dropna=False, legend_out=True, 
#   despine=True, margin_titles=False, xlim=None, ylim=None, subplot_kws=None, 
#   gridspec_kws=None, size=None)

# col_wrap - “Wrap” the column variable at this width, so that the column facets span multiple rows
# share{x,y} - bool, ‘col’, or ‘row’ optional - If true, the facets will share y axes across columns and/or x axes across rows
# palette - palette name, list, or dict
'''
sns.color_palette() # all colors from the current default color cycle
sns.color_palette("pastel") # Other variants on the seaborn categorical color palette can be referenced by name
sns.color_palette("husl", 9) # Return a specified number of evenly spaced hues in the “HUSL” system
sns.color_palette("Set2") # Return all unique colors in a categorical Color Brewer palette
sns.color_palette("flare", as_cmap=True) # Return one of the perceptually-uniform colormaps included in seaborn
sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True) # Return a customized cubehelix color palette
sns.color_palette("light:#5A9", as_cmap=True) # Return a light-themed sequential colormap to a seed color
'''
# despine - Remove the top and right spines from the plots

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time",  row="sex") # This initializes the grid, but doesn’t plot anything on it
g.map(sns.scatterplot, "total_bill", "tip") # To draw a plot on every facet, pass a function and the name of one or more columns in the dataframe to FacetGrid.map()

g = sns.FacetGrid(tips, col="time",  row="sex", height=3.5, aspect=.65)
g.map_dataframe(sns.histplot, x="total_bill", binwidth=2)
g.set_axis_labels("Total bill", "Count")
g.add_legend()

# You can pass custom functions to plot with, or to annotate each facet
# Your custom function must use the matplotlib state-machine interface to plot on the “current” axes
# and it should catch additional keyword arguments
import matplotlib.pyplot as plt
def annotate(data, **kws):
    n = len(data)
    ax = plt.gca()
    ax.text(.1, .6, f"N = {n}", transform=ax.transAxes)
g = sns.FacetGrid(tips, col="time")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill", "Tip")
g.map_dataframe(annotate)

# The FacetGrid object has some other useful parameters and methods for tweaking the plot
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill", "Tip")
g.set_titles(col_template="{col_name} patrons", row_template="{row_name}")
g.set(xlim=(0, 60), ylim=(0, 12), xticks=[10, 30, 50], yticks=[2, 6, 10])
g.tight_layout()
g.savefig("facet_plot.png")

# You also have access to the underlying matplotlib objects for additional tweaking
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True, despine=False)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill", "Tip")
g.fig.subplots_adjust(wspace=0, hspace=0)
for (row_val, col_val), ax in g.axes_dict.items():
    if row_val == "Lunch" and col_val == "Female":
        ax.set_facecolor(".95")
    else:
        ax.set_facecolor((0, 0, 0, 0))
        




### additional seaborn features

# Classes and functions for making complex graphics
# These tools work by combining axes-level plotting functions with objects that manage the layout of the figure, linking the structure of a dataset to a grid of axes
g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))


# Opinionated defaults 
# when possible, functions will automatically add informative axis labels and legends that explain the semantic mappings in the plot
# seaborn will also choose default values for its parameters based on characteristics of the data
# categorical variables - distinct hues (blue, orange, and sometimes green) to represent different levels 
# numeric variable - some functions will switch to a continuous gradient
sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)


# Flexible customization
# multiple built-in themes that apply to all figures
# functions have standardized parameters that can modify the semantic mappings for each plot
# additional keyword arguments are passed down to the underlying matplotlib artsts
# plot properties can be modified through both the seaborn API and by dropping down to the matplotlib layer for fine-grained tweaking
sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.fig.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)



