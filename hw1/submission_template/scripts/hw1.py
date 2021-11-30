#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:47:33 2021

@author: xinyi
"""

def mentionsTrump (name, line):
    curr = 0
    while curr < len(line):
        flag = 0
        ind = line.find("Trump", curr)
        if (ind == -1):
            return False
        else:
            if ind-1>=0:
                if line[ind-1].isalnum():
                    flag += 1
            if ind+5<len(line):
                if line[ind+5].isalnum():
                    flag += 1
        if (flag == 0):
            return True
        else:
            curr += 5
            
    return False
                
            
            
with open("clean_data.tsv", "r") as f:
    lines = f.readlines()
    
lines[0] = lines[0].replace("\n", "\ttrump_mention")

for i in range(1, len(lines)):
    if (mentionsTrump("Trump", lines[i])):
        lines[i] = lines[i].replace("\n", "\tT")
    else:
        lines[i] = lines[i].replace("\n", "\tF")



with open("dataset.tsv", "w") as dataset:
    contents = "\n".join(lines)
    dataset.write(contents)
    
