import pandas as pd
from bokeh.io import output_notebook
from bokeh.models import CustomJS, Dropdown, ColumnDataSource
from bokeh.layouts import column
from bokeh.plotting import figure, show, curdoc

df = pd.read_csv('dashboard_data.csv')
#cds = ColumnDataSource(df)

# x-axis
month = list(df.columns[1:]) 
# y-axis
all_data = "All"
time_all = df.loc[df['Zipcode']==all_data].values.flatten().tolist()[1:]  

# create a new plot with a title and axis labels
p = figure(title="nyc_dash", x_axis_label='month', y_axis_label='avg response time', x_range=month)

# add a line renderer with legend to the plot
p.line(month, time_all, legend_label=all_data, line_color="blue")

'''
zipcode1 = None
zipcode2 = None
time1 = None
time2 = None
'''
line1 = None
line2 = None

def callback1(event):
    global line1

    zipcode1 = event.item
    time1 = df.loc[df['Zipcode']==zipcode1].values.flatten().tolist()[1:]
    #make the previous line and its legend invisible, and replace it with a new one
    if line1: 
        line1.visible = False
    line1 = p.line(month, time1, legend_label=str(zipcode1), line_color="green")
    line1.visible = True
    
dropdown1 = Dropdown(label='Select zipcode 1', button_type="primary", menu=list(df['Zipcode'])[1:])
#dropdown1.on_change('value', callback1)
dropdown1.on_click(callback1)

def callback2(event):
    global line2

    zipcode2 = event.item
    time2 = df.loc[df['Zipcode']==zipcode2].values.flatten().tolist()[1:]
    if line2: 
        line2.visible = False
    line2 = p.line(month, time2, legend_label=str(zipcode2), line_color="orange")
    line2.visible = True
    
dropdown2 = Dropdown(label='Select zipcode 1', button_type="primary", menu=list(df['Zipcode'])[1:])
#dropdown1.on_change('value', callback2)
dropdown2.on_click(callback2)

curdoc().add_root(column(dropdown1, dropdown2, p))

'''
if zipcode1:
  time1 = df.loc[df['Zipcode']==zipcode1].values.flatten().tolist()[1:]
  p.line(month, time1, legend_label=str(zipcode1), line_color="green")
if zipcode2:
  time2 = df.loc[df['Zipcode']==zipcode2].values.flatten().tolist()[1:]
  p.line(month, time2, legend_label=str(zipcode2), line_color="orange")


curdoc().add_root(column(dropdown1, dropdown2, p))




dropdown2 = Dropdown(label='Select zipcode 2', button_type="success", menu=list(df['Zipcode'])[1:])

# x-axis
month = list(df.columns[1:]) 

#data = {}



# capture selected zipcodes
def handler1(event):
    zipcode1 = event.item



def handler2(event):
    zipcode2 = event.item

#show(dropdown1)
#show(dropdown2)

#dropdown1.on_change('item', handler1)
dropdown1.on_click(handler1)

#dropdown2.on_change('item', handler2)
dropdown2.on_click(handler2)




if zipcode1:
  time1 = df.loc[df['Zipcode']==zipcode1].values.flatten().tolist()[1:]
if zipcode2:
  time2 = df.loc[df['Zipcode']==zipcode2].values.flatten().tolist()[1:]

output_notebook()

# create a new plot with a title and axis labels
p = figure(title="nyc_dash", x_axis_label='month', y_axis_label='avg response time', x_range=month)

# add a line renderer with legend to the plot
p.line(month, time_all, legend_label=all_data, line_color="blue")
if time1:
  p.line(month, time1, legend_label=str(zipcode1), line_color="green")
if time2:
  p.line(month, time2, legend_label=str(zipcode2), line_color="orange")

show(column(dropdown1, dropdown2, p))
#show(p)
'''
