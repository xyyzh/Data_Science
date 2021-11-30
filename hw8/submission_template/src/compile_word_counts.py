#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:08:23 2021

@author: xinyi
"""


import argparse
import pandas as pd
import json
import os, pathlib


stopwords="a about above across after again against all almost alone along already also although always among an and another any anybody anyone anything anywhere are area areas around as ask asked asking asks at away b back backed backing backs be became because become becomes been before began behind being beings best better between big both but by c came can cannot case cases certain certainly clear clearly come could d did differ different differently do does done down down downed downing downs during e each early either end ended ending ends enough even evenly ever every everybody everyone everything everywhere f face faces fact facts far felt few find finds first for four from full fully further furthered furthering furthers g gave general generally get gets give given gives go going good goods got great greater greatest group grouped grouping groups h had has have having he her here herself high high high higher highest him himself his how however i if important in interest interested interesting interests into is it its itself j just k keep keeps kind knew know known knows l large largely last later latest least less let lets like likely long longer longest m made make making man many may me member members men might more most mostly mr mrs much must my myself n necessary need needed needing needs never new new newer newest next no nobody non noone not nothing now nowhere number numbers o of off often old older oldest on once one only open opened opening opens or order ordered ordering orders other others our out over p part parted parting parts per perhaps place places point pointed pointing points possible present presented presenting presents problem problems put puts q quite r rather really right right room rooms s said same saw say says second seconds see seem seemed seeming seems sees several shall she should show showed showing shows side sides since small smaller smallest so some somebody someone something somewhere state states still still such sure t take taken than that the their them then there therefore these they thing things think thinks this those though thought thoughts three through thus to today together too took toward turn turned turning turns two u under until up upon us use used uses v very w want wanted wanting wants was way ways we well wells went were what when where whether which while who whole whose why will with within without work worked working works would x y year years yet you young younger youngest your yours z"

# filter words in the dialog for a specific pony, return the word counts
# replace punctuations
# remove stopwords, words with non alphabetic characters
def filter_words(infile, pony):
    word_count = dict()
    df = pd.read_csv(infile)
    df = df[['pony','dialog']]
    data = df.loc[df['pony']==pony]
    for text in data['dialog']:
        string = ""
        for char in text:
            if char in "()[],-.?!:;#&":
                char = " "
            string += char.lower()
        
        words = string.split()
        for word in words:
            if word not in stopwords.split() and word.isalpha():
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count
        
# only keep words that occur at least 5 times
def exclude_rare(word_count):
    word_count_copy = word_count.copy()
    for key in word_count:
        if word_count[key] < 5:
            word_count_copy.pop(key)
    return word_count_copy

def get_all_count(infile):
    count_all = {"twilight sparkle": {}, "applejack": {}, "rarity": {}, "pinkie pie": {}, "rainbow dash": {}, "fluttershy": {}}
    for pony in ["Twilight Sparkle", "Applejack", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]:
        count_all[pony.lower()] = exclude_rare(filter_words(infile, pony))
    return count_all

# This function is made for unittest
# same as get_all_count, but it doesn't have the restriction about rare words
def get_all_count_test(infile):
    count_all = {"twilight sparkle": {}, "applejack": {}, "rarity": {}, "pinkie pie": {}, "rainbow dash": {}, "fluttershy": {}}
    for pony in ["Twilight Sparkle", "Applejack", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]:
        count_all[pony.lower()] = filter_words(infile, pony)
    return count_all



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile")
    parser.add_argument("-d", "--infile")
    args = parser.parse_args()
    outfile = args.outfile
    infile = args.infile
    
    count_all = get_all_count(infile)
        
    # create directories in case they do not exist
    # does not raise an exception if the directory already exists.
    head_tail = os.path.split(outfile)
    pathlib.Path(head_tail[0]).mkdir(parents=True, exist_ok=True) 
    with open(outfile, 'w') as fout:
        json.dump(count_all, fout, indent=4)
    
if __name__ == "__main__":
    main()
    
    
    