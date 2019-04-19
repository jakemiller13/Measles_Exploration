#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:27:35 2019

@author: Jake
"""

# https://www.who.int/immunization/monitoring_surveillance/burden/vpd/
# surveillance_type/active/measles_monthlydata/en/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load in dataframe. Also print disclaimer from WHO
disc = pd.read_excel('measlescasesbycountrybymonth.xls',
                     sheet_name = 'Read Me')
df = pd.read_excel('measlescasesbycountrybymonth.xls',
                   sheet_name = 'WEB')
df.fillna(0.0, inplace = True)
print('\nDisclaimer:\n' + disc.iloc[4][1] + '\n')

# Print top 5 lines and first entry to see what data looks like
print(df.head())
print('\n' + str(df.iloc[0]))

# How many regions
regions, regions_counts = np.unique(df['Region'], return_counts = True)
print('\nRegions:\n' + str(regions))

# Plot cases over time
# TODO need to test summation when using regions
def plot_cases(region = None,
               country = None,
               plot_all_years = False,
               year = None):
    '''
    Plots cases for EITHER "region" -OR- "country" - must specify one OR other
    If "plot_all_years" == True, plots cases over all years
    Otherwise, you must specify "year" to plot
    '''
    if region:
        loc_col = 'Region'
        location = region
    elif country:
        loc_col = 'Country'
        location = country
    
    if plot_all_years == True:
        x_plot = np.unique(df['Year'])
        y_plot = [df[(df[loc_col] == location) & (df['Year'] == i)].\
                     iloc[:,4:].sum().sum() for i in x_plot]
    else:
        x_plot = df.columns[4:]
        y_plot = df[(df[loc_col] == location) & (df['Year'] == year)].\
                    iloc[:,4:].values[0]
    
    plt.plot(x_plot, y_plot)
    # TODO make plots pretty