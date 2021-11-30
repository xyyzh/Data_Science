#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:12:34 2021

@author: xinyi
"""

import json
import argparse
import random


def extract_post(jsonfile, num):
    posts = []
    num_lines = sum(1 for line in open(jsonfile, 'r'))
    
    for line in open(jsonfile, 'r'):
        posts.append(json.loads(line))
        
    if num_lines <= num:
        return posts
    else:
        #selected = []
        #for i in range(num):
         #   selected.append(random.choice(posts))
        selected = random.sample(posts, num)
        return selected

def write_to_tsv(posts, outfile):
    with open(outfile, 'w') as fout:
        fout.write("Name\ttitle\tcoding\n")
        for p in posts:
            fout.write("{}\t{}\t\n".format(p['data']['name'], p['data']['title']))
    return





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile")
    parser.add_argument("jsonfile")
    parser.add_argument("num", type=int)
    args = parser.parse_args()
    outfile = args.outfile
    jsonfile = args.jsonfile
    num = args.num
    
    write_to_tsv(extract_post(jsonfile, num), outfile)
    #print(outfile, jsonfile, num)
        
    return

if __name__ == "__main__":
    main()