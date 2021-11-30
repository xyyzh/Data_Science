#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:23:46 2021

@author: xinyi
"""

import argparse
import networkx as nx
import json

def build_network(infile):
    G = nx.Graph()
    with open(infile) as fin:
        record = json.load(fin)
    for pony in record:
        for key in record[pony]:
            G.add_edge(pony, key, weight=record[pony][key])
            
    return G

#The top three most connected characters by # of edges
def rank_edge(G):
    node_degrees = {}
    for v in G.nodes():
        node_degrees[v] = G.degree(v)
    sorted_deg = sorted(node_degrees.items(), key=lambda item: item[1], reverse=True)[:3]
    return [i[0] for i in sorted_deg]

# The top three most connected characters by sum of the weight of edges.
def rank_weight(G):
    node_degrees = dict(G.degree(weight='weight'))
    sorted_deg = sorted(node_degrees.items(), key=lambda item: item[1], reverse=True)[:3]
    return [i[0] for i in sorted_deg]
    
# The top three most central characters by betweenness.
def rank_betweenness(G):
    betweenness = nx.betweenness_centrality(G)
    sorted_betweenness = sorted(betweenness.items(), key=lambda item: item[1], reverse=True)[:3]
    return [i[0] for i in sorted_betweenness]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile")
    parser.add_argument("-o", "--outfile")
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    
    out = dict()
    G = build_network(infile)
    out["most_connected_by_num"] = rank_edge(G)
    out["most_connected_by_weight"] = rank_weight(G)
    out["most_central_by_betweenness"] = rank_betweenness(G)

    with open(outfile, 'w') as fout:
        json.dump(out, fout, indent=4)
    
if __name__ == "__main__":
    main()