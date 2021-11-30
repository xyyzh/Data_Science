#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:15:47 2021

@author: xinyi
"""

import sys
import pandas as pd
import json


input_file = sys.argv[3]
output_file = sys.argv[2]

data = pd.read_csv(input_file)

#data

count = {"twilight sparkle": 0, "applejack": 0, "rarity": 0, "pinkie pie": 0, "rainbow dash": 0, "fluttershy": 0}

for pony in data['pony']:
  if pony.casefold() == "twilight sparkle".casefold():
    count["twilight sparkle"] += 1
  elif pony.casefold() == "applejack".casefold():
    count["applejack"] += 1
  elif pony.casefold() == "rarity".casefold():
    count["rarity"] += 1
  elif pony.casefold() == "pinkie pie".casefold():
    count["pinkie pie"] += 1
  elif pony.casefold() == "rainbow dash".casefold():
    count["rainbow dash"] += 1
  elif pony.casefold() == "fluttershy".casefold():
    count["fluttershy"] += 1

#print(count)



total = len(data['dialog'])

verbosity = count.copy()
for i in verbosity:
  verbosity[i] /= total

#print(verbosity) 

output = {"count": count, "verbosity": verbosity}
#output

with open(output_file, "w") as outfile:
    json.dump(output, outfile)