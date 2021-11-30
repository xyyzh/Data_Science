#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:58:57 2021

@author: xinyi
"""

import argparse
import json
import math
import sys

def compute_tfdif(w, pony, data):
    #with open(script, 'r') as f:
    #    data = json.load(f)
    tf = data[pony][w]
    df = 0
    for pony_name in data:
        if w in data[pony_name]:
            df += 1
    idf = math.log10(6/df)
    tfdif = tf*idf
    return tfdif

# compute tf-dif score for each word for the pony
# and sort words by score from high to low
# return a list of sorted words with a specified length
def sort_words(pony, script, num_words):
    word_score = dict()
    with open(script, 'r') as f:
        data = json.load(f)
        
    words_count = data[pony]
    for word in words_count:
        word_score[word] = compute_tfdif(word, pony, data)
        
    word_score_sorted = dict(sorted(word_score.items(), key=lambda item: item[1], reverse=True))
    word_sorted = list(word_score_sorted.keys())[:num_words]
    return word_sorted

def get_output(jsonfile, num_words):
    output = dict()
    for pony in ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash",  "fluttershy"]:
        output[pony] = sort_words(pony, jsonfile, num_words)
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--jsonfile")
    parser.add_argument("-n", "--num_words", type=int)
    args = parser.parse_args()
    jsonfile = args.jsonfile
    num_words = args.num_words
    
    output = get_output(jsonfile, num_words)

    #sys.stdout.write(json.dumps(output, indent=4) + '\n')
    print(json.dumps(output, indent=4))
    
if __name__ == "__main__":
    main()
    
    