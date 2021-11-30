#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:15:03 2021

@author: xinyi
"""
import pandas as pd
from collections import OrderedDict
import json


df = pd.read_csv('/Users/xinyi/OneDrive/COMP598/hw4/nyc_311_preprocessed.csv')
print("There are", df['Incident Zip'].nunique(), "unique zipcode.")

#key: month, value:average response time for this month
allData = {}

def addToDict(dataFrame, dic):
    # keep track of the number of each month
    count = {}
    for month,resTime in zip(dataFrame['Month'], dataFrame['Response Time']):
        if month in dic:
            dic[month] += resTime
            count[month] += 1
        else:
            dic[month] = resTime
            count[month] = 1
            
    # get the average
    for key,val in dic.items():
        dic[key] = val/count[key]

addToDict(df, allData)
#print(allData)

# sort by month name
monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
allData = dict(OrderedDict(sorted(allData.items(),key =lambda x:monthName.index(x[0]))))
#print(allData)

#key: zipcode, value: another dictionary where key=month, value=average response time for this month
allZipCode = {}
# a list of unique zipcodes
zipCode = df['Incident Zip'].unique()
for code in zipCode:
    zipCode_dict = {}
    addToDict(df[(df['Incident Zip'] == code)], zipCode_dict)
    zipCode_dict = dict(OrderedDict(sorted(zipCode_dict.items(),key =lambda x:monthName.index(x[0]))))
    allZipCode[str(code)] = zipCode_dict

#print(allZipCode)

output = {"All": allData}
output.update(allZipCode)
#print(output)
with open("dashboard_data.json", "w") as outfile:
    json.dump(output, outfile)


    