#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:58:25 2021

@author: xinyi
"""

import requests
import requests.auth
import os, sys
import os.path as osp
import json


'''
request
In [1]: import requests
In [2]: import requests.auth
In [3]: client_auth = requests.auth.HTTPBasicAuth('p-jcoLKBynTLew', 'gko_LXELoV07ZBNUXrvWZfzE3aI')
In [4]: post_data = {"grant_type": "password", "username": "reddit_bot", "password": "snoo"}
In [5]: headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
In [6]: response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
In [7]: response.json()
Out[7]: 
{u'access_token': u'fhTdafZI-0ClEzzYORfBSCR7x3M',
 u'expires_in': 3600,
 u'scope': u'*',
 u'token_type': u'bearer'}

use
In [8]: headers = {"Authorization": "bearer fhTdafZI-0ClEzzYORfBSCR7x3M", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
In [9]: response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
In [10]: response.json()
'''

def request_token():
    with open("credential.json", "r") as cre:
        credentials = json.load(cre)
        
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
    all_posts = []
    
    for sub in subreddit:
        response = requests.get(f"https://oauth.reddit.com/r/{sub}/new.json?limit=100", headers=headers)
        root_element = response.json()
        # this is a list containing 100 posts (two fields: 'kind' and 'data')
        curr_sub_posts = root_element['data']['children']
        all_posts.extend(curr_sub_posts)
    return all_posts

def write_to_file(all_posts, outfile):
    with open(outfile, 'w') as fout:
        for p in all_posts:
            json.dump(p, fout)
            fout.write("\n")
    return
        

def main():
    subreddit1 = ["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned" ]
    subreddit2 = ["AskReddit", "memes", "politics", "nfl", "nba", "wallstreetbets", "teenagers", "PublicFreakout", "leagueoflegends", "unpopularopinion"]
    
    write_to_file(collect_post(subreddit1), "../sample1.json")
    write_to_file(collect_post(subreddit2), "../sample2.json")
        
    return

if __name__ == "__main__":
    main()