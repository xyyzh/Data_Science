#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:24:59 2021

@author: xinyi
"""

import argparse
import json
import dateutil.parser
from datetime import datetime, timezone
import pytz

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest='input', help = "input filename")
    parser.add_argument("-o", dest='output', help = "output filename")
    args = parser.parse_args()
    infile = args.input
    outfile = args.output
    return infile, outfile

# 5
def remove_invalid(line):
    try:
        record = json.loads(line)
        return record
    except ValueError:
        return None
    
# 1, 2
def validate_title(record):
    if not record: return None
    if "title_text" in record:
        record["title"] = record.pop("title_text")
    if "title" in record:
        return record
    return None

# 3, 4
def standardize_time(record):
    if not record: return None
    if "createdAt" in record:
        time = record["createdAt"]
        try:
            # parse ISO format
            time = dateutil.parser.isoparse(time)
            # convert to UTC timezone
            time = time.astimezone(pytz.utc)
            # convert back to ISO
            time = time.isoformat()
            record["createdAt"] = time
            return record
        except ValueError:
            return None
    return record
    

# 6
def filter_author(record):
    if not record: return None
    if "author" in record:
        if (not record["author"]) or (record["author"]=="N/A"):
            return None
        else:
            return record
    return record

# 7, 8
def cast_int(record):
    if not record: return None
    if "total_count" in record:
        if type(record["total_count"]) not in [int, float, str]:
            return None
        try:
            count = (int)(record["total_count"])
            record["total_count"] = count
            return record
        except ValueError:
            return None
    return record

# 9
def tag_split(record):
    if not record: return None
    if "tags" in record:
        #empty list?
        tags = record["tags"]
        tags = [word for phrase in tags for word in phrase.split()]
        record["tags"] = tags
        return record
    return record

def main():
    infile, outfile = arg_parse()
    fin = open(infile, 'r')
    lines = fin.readlines()
    fout = open(outfile, 'w')

    for json_line in lines:
        filtered_record = tag_split(cast_int(filter_author(standardize_time(validate_title(remove_invalid(json_line))))))
        if filtered_record:
            json.dump(filtered_record, fout)
            fout.write("\n")
    return

if __name__ == "__main__":
    main()
    
    
'''
def main():
    infile, outfile = arg_parse()
    fout = open(outfile, 'w')
    with open(infile) as fin:
        for json_line in fin:
            try:
                record = json.loads(json_line)
                #print(validate_title(record))
                if (validate_title(record)):
                    json.dump(record, fout)
            except ValueError:
                continue
    return
'''