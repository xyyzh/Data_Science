#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:35:50 2021

@author: xinyi
"""

import argparse
import json
import hashlib
import os.path as osp
import os
import requests
from bs4 import BeautifulSoup

def cache(cache_dir, person):
    url = "https://www.whosdatedwho.com/dating/" + person
    fname = hashlib.sha1(url.encode('utf-8')).hexdigest()
    full_fname = osp.join(cache_dir, fname)
    
    if not osp.exists(cache_dir):
        os.makedirs(cache_dir)

    if not osp.exists(full_fname):
        r = requests.get(url)
        contents = r.text
        
        f = open(full_fname, 'w')
        f.write(contents)

    return full_fname

def find_candidate(candidate, person_url):
    relationships = []
    for c in candidate:
        if 'href' not in c.attrs:
            continue
        href = c['href']
        if href.startswith('/dating') and href!=person_url:
            relationships.append(href[8:])
    return relationships
    

def fetch_relationship(file, person):
    relationships = []
    #url = "https://www.whosdatedwho.com/dating/" + person
    person_url = "/dating/" + person
    
    soup = BeautifulSoup(open(file, 'r'), 'html.parser')
    #print("----soup", soup)
    status_h4 = soup.find('h4', 'ff-auto-status')
    #print("-------status_h4 is", status_h4)
    key = status_h4.next_sibling
    candidate = key.find_all('a')
    relationships.extend(find_candidate(candidate, person_url))
    
    rel_h4 = soup.find('h4', 'ff-auto-relationships')
    sib = rel_h4.next_sibling
    while sib and sib.name=='p':
        candidate = sib.find_all('a')
        relationships.extend(find_candidate(candidate, person_url))
        sib = sib.next_sibling
        
    return relationships


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    configfile = args.config
    outfile = args.output
    
    with open(configfile, 'r') as f:
        json_line = json.load(f)
        
    cache_dir = json_line['cache_dir']
    target_people = json_line['target_people']
    #print(cache_dir)
    #print(target_people)
    
    output_dict = {}
    for p in target_people:
        file = cache(cache_dir, p)
        #print(file)
        relationship = fetch_relationship(file, p)
        output_dict[p] = relationship
        
    with open(outfile, 'w') as fout:
        json.dump(output_dict, fout)
        
if __name__ == "__main__":
    main()
    