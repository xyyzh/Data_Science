#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:13:21 2021

@author: xinyi
"""


import pandas as pd
#import datetime
from dateutil.parser import parse

df = pd.read_csv('/Users/xinyi/OneDrive/COMP598/hw4/nyc_311_trimmed.csv')
data = df[['Created Date', 'Closed Date', 'Incident Zip']].copy()

def responseTime(row):
    createTime = parse(row['Created Date'])
    closeTime = parse(row['Closed Date'])
    diff = closeTime - createTime
    hours = diff.days*24 + diff.seconds/3600
    return hours

data['Response Time'] = data.apply(lambda row: responseTime(row), axis=1)
data = data[(data['Response Time'] >= 0)]

def month(row):
    closeTime = parse(row['Closed Date'])
    return closeTime.strftime("%b")

data['Month'] = data.apply(month, axis=1)

#preprocessed data
#data: ['Created Date', 'Closed Date', 'Incident Zip', 'Response Time','Month']
data.to_csv('/Users/xinyi/OneDrive/COMP598/hw4/nyc_311_preprocessed.csv', index=False)