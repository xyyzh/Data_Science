#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:40:06 2021

@author: xinyi
"""

import pandas as pd
pd.options.mode.chained_assignment = None

header_list = ['Unique Key', 'Created Date', 'Closed Date', 'Agency',	'Agency Name', 	
'Complaint Type', 	'Descriptor', 	'Location Type', 	'Incident Zip', 	'Incident Address', 	
'Street Name', 	'Cross Street 1', 	'Cross Street 2', 'Intersection Street 1', 	'Intersection Street 2', 	
'Address Type', 'City', 'Landmark',	'Facility Type', 	'Status','Due Date', 	
'Resolution Description', 	'Resolution Action Updated Date', 	'Community Board', 	'BBL', 	
'Borough', 	'X Coordinate (State Plane)', 	'Y Coordinate (State Plane)', 	
'Open Data Channel Type', 	'Park Facility Name', 	'Park Borough', 	'Vehicle Type', 	
'Taxi Company Borough', 	'Taxi Pick Up Location', 	'Bridge Highway Name', 	'Bridge Highway Direction', 	
'Road Ramp', 	'Bridge Highway Segment', 	'Latitude', 	'Longitude', 	'Location']

df = pd.read_csv('/Users/xinyi/OneDrive/COMP598/hw4/nyc_311_limit.csv',  names=header_list)
filtered = df[(df['Created Date'].str.contains("2020"))]
output = filtered.dropna(subset=['Incident Zip', 'Closed Date'])
#print(output['Incident Zip'].dtypes)

# because the NaN value in some rows, read_csv will convert the zipcode to float number
# need to drop them first, then convert back to int
# ref: https://stackoverflow.com/questions/39666308/pd-read-csv-by-default-treats-integers-like-floats

output['Incident Zip'] = output['Incident Zip'].astype(int)
output.to_csv('/Users/xinyi/OneDrive/COMP598/hw4/nyc_311_trimmed.csv', index=False)
