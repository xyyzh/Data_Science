#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:43:44 2021

@author: xinyi
"""

import requests
import requests.auth
import os, sys
import os.path as osp
import json
import argparse


credentials = {"client_id": "pGJsGtnE_aXYHRIcggWVFg",
"client_secret": "CaGzWnrOV83dBD9LVfdhAYLU385dKA",
"username": "wedeservehappiness",
"password": "#pwFORcomp598hw"
}

def request_token():
    #with open("credential.json", "r") as cre:
        #credentials = json.load(cre)
        
    client_auth = requests.auth.HTTPBasicAuth(credentials['client_id'], credentials['client_secret'])
    post_data = {"grant_type": "password", "username": credentials['username'], "password": credentials['password']}
    headers = {"User-Agent": f"ChangeMeClient/0.1 by /u/{credentials['username']}"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    token = response.json()['access_token']
    user_agent = headers['User-Agent']
    return token, user_agent

def collect_post(subreddit):
    token, user_agent = request_token()
    headers = {"Authorization": f"bearer {token}", "User-Agent": user_agent}
    
    response = requests.get(f"https://oauth.reddit.com{subreddit}/new.json?limit=100", headers=headers)
    root_element = response.json()
    # this is a list containing 100 posts (two fields: 'kind' and 'data')
    posts = root_element['data']['children']
    return posts

def write_to_file(posts, outfile):
    with open(outfile, 'w') as fout:
        for p in posts:
            json.dump(p, fout)
            fout.write("\n")
    return
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile")
    parser.add_argument("-s", "--subreddit")
    args = parser.parse_args()
    outfile = args.outfile
    subreddit = args.subreddit
    
    write_to_file(collect_post(subreddit), outfile)
        
    return

if __name__ == "__main__":
    main()
