
# Loading the Dataset
import plotly.express as px
df = px.data.tips() 

# Exploratory Data Analysis 
from dataprep.eda import plot
plot(df) # distribution of each column and calculates dataset statistics
plot(df,'tip') # distribution of column x in various ways and calculates column statistics
plot(df, 'tip', 'total_bill') # depicting the relationship between columns x and y

# Plot corr
from dataprep.eda import plot_correlation
plot_correlation(df) # plots correlation matrices (correlations between all pairs of columns)
plot_correlation(df, 'tip') # plots the most correlated columns to column x
plot_correlation(df, 'tip', 'total_bill') # plots the joint distribution of column x and column y and computes a regression line

# Plot missing data
from dataprep.eda import plot_missing
plot_missing(df) # plots the amount and position of missing values, and their relationship between columns
plot_missing(df, 'tip') # plots the impact of the missing values in column x on all other columns
plot_missing(df, 'tip', 'total_bill') # plots the impact of the missing values from column x on column y in various ways

# Report
'''
Overview: detect the types of columns in a dataframe
Variables: variable type, unique values, distint count, missing values
Quantile statistics like minimum value, Q1, median, Q3, maximum, range, interquartile range
Descriptive statistics like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
Text analysis for length, sample and letter
Correlations: highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
Missing Values: bar chart, heatmap and spectrum of missing values
'''
from dataprep.eda import create_report
create_report(df, title='My Report')
# report = create_report(df, title='My Report')
# report.show_browser()
# report.save(filename='report_01', to='~/Desktop')


# Clean
'''
DataPrep.Clean provides functions for quickly and easily cleaning and validating your data.
    Column Headers
    Country Names
    Email Addresses
    Geographic Goordinates
    IP Addresses
    Phone Numbers
    URLs
    US Street Addresses
'''
from dataprep.clean import clean_headers
clean_headers(df)

import pandas as pd
import numpy as np
df = pd.DataFrame({"country": ["Canada", "foo canada bar", "cnada", "northern ireland", " ireland ", "congo, kinshasa", "congo, brazzaville", 304, "233", " tr ", "ARG", "hello", np.nan, "NULL"]})
from dataprep.clean import clean_country
clean_country(df, "country")
clean_country(df, "country", input_format="name") # official, alpha-2, alpha-3, numeric
clean_country(df, "country", output_format="official")
clean_country(df, "country", strict=True) # allows for control over the type of matching used for “name” and “official” input formats
clean_country(df, "country", fuzzy_dist=1) # fuzzy_dist parameter sets the maximum edit distance (number of single character insertions, deletions or substitutions required to change one word into the other) allowed between the input and a country regex
clean_country(df, "country", fuzzy_dist=2, inplace=True) # just deletes the given column from the returned dataframe. A new column containing cleaned coordinates is added



