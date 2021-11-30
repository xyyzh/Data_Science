#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:28:33 2021

@author: xinyi
"""
import json
import argparse
import pandas as pd

def get_count(coded_file):
    result = {"course-related": 0, "food-related": 0, "residence-related": 0, "other": 0}
    df = pd.read_csv(coded_file, sep='\t')
    for categ in df['coding']:
        if categ == 'c':
            result["course-related"] += 1
        elif categ == 'f':
            result["food-related"] += 1
        elif categ == 'r':
            result["residence-related"] += 1
        elif categ == 'o':
            result["other"] += 1
        else:
            print("undefined category!")
    return json.dumps(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--coded")
    parser.add_argument("-o", "--outfile")
    args = parser.parse_args()
    coded_file = args.coded
    outfile = args.outfile

    if outfile:
        with open(outfile, 'w') as fout:
            fout.write(get_count(coded_file))
    else:
        print(get_count(coded_file))
    #print(outfile, jsonfile, num)
        
    return

if __name__ == "__main__":
    main()