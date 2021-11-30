#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:04:55 2021

@author: xinyi
"""

from bokeh.plotting import figure, show, output_file
import pandas as pd

df = pd.read_csv('../dashboard_data.csv')

zipcode = "All"
#get a particular row
time = df.loc[df['Zipcode']==zipcode]
month = df.columns()[1:]

output_file = "test.html"

# create a new plot with a title and axis labels
p = figure(title="nyc_dash", x_axis_label='month', y_axis_label='avg response time')

# add a line renderer with legend and line thickness to the plot
p.line(month, time, legend_label=zipcode, line_width=2)

p.show()
