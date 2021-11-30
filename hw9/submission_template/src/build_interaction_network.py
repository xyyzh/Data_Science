#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:11:00 2021

@author: xinyi
"""

import argparse
import pandas as pd
import networkx as nx
import json

'''
def filter_character(infile):
    df = pd.read_csv(infile)
    filtered = pd.DataFrame()
    for ind in range(len(df)):
      splitted = df['pony'][ind].lower().split()
      if not (("others" in splitted) or ("ponies" in splitted) or ("and" in splitted) or ("all" in splitted)):
        filtered = filtered.append(df.iloc[ind])
    return filtered
'''

def find_top101(infile):
    df = pd.read_csv(infile)
    counts = df['pony'].value_counts().to_dict()
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    top101 = []
    counter = 0
    for pony in sorted_counts.keys():
        if counter == 101: break
        splitted = pony.lower().split()
        if not (("others" in splitted) or ("ponies" in splitted) or ("and" in splitted) or ("all" in splitted)):
            top101.append(pony.lower())
            counter += 1
    return top101

def contain_words(s):
  splitted = s.split()
  if ("others" in splitted) or ("ponies" in splitted) or ("and" in splitted) or ("all" in splitted):
    return True
  return False

def build_network(infile, top101):
    G = nx.MultiGraph()
    
    df = pd.read_csv(infile)
    for ind in range(1, len(df)):
      prev_pony = df['pony'][ind-1].lower()
      curr_pony = df['pony'][ind].lower()
      # skip the row if different episodes, or consecutive same character
      if (df['title'][ind] != df['title'][ind-1]) or (curr_pony == prev_pony): 
        continue
      # skip if contain certain words
      if contain_words(curr_pony) or contain_words(prev_pony):
        continue
      # skip if not in the most frequent 101 characters
      if (curr_pony not in top101) or (prev_pony not in top101):
        continue
      G.add_edge(prev_pony, curr_pony)
    return G

# count number of interactions for a specific pony (character)
def check_edges(G, pony, top101):
  count = dict()
  copy101 = top101.copy()
  copy101.remove(pony)
  for char in copy101:
    #if char not in count:
      #count[char] = 0
      
    if G.number_of_edges(pony, char):
        count[char] = G.number_of_edges(pony, char)
  return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile")
    parser.add_argument("-o", "--outfile")
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    
    top101 = find_top101(infile)
    #print(top101)
    G = build_network(infile, top101)
    
    interaction = dict()
    for pony in top101:
        interaction[pony] = check_edges(G, pony, top101)
    
    with open(outfile, 'w') as fout:
        json.dump(interaction, fout, indent=4)
    
    
    
    
if __name__ == "__main__":
    main()