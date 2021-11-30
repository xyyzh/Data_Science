#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:40:36 2021

@author: xinyi
"""

import argparse
import json

def compute(infile):
    total_length = 0
    with open(infile) as f:
        for line in f:
            post = json.loads(line)
            if 'title' in post['data']:
                title = post['data']['title']
                total_length += len(title)
    
    avg_title_length = round(total_length/1000, 2)
    return avg_title_length


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()
    infile = args.input_file
    avg_title_length = compute(infile)
    print(avg_title_length)
    
    
if __name__ == "__main__":
    main()