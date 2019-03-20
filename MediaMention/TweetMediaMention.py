# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:02:10 2019

@author: Zhian Wang
"""
import tweepy
import pandas as pd

import os
os.chdir('D:\GitHub\HMAResearch\HSData\MediaMention')

def getAuthData(authfile):
    import csv
    with open(authfile, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    authdata = {}   
    for element in your_list:
        authdata[element[0]] = element[1]
    #print(authdata)
    return authdata


authdata = getAuthData('authdata.csv')

# set up
CONSUMER_KEY = authdata['CONSUMER_KEY']
CONSUMER_SECRET = authdata['CONSUMER_SECRET']
OAUTH_TOKEN = authdata['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = authdata['OAUTH_TOKEN_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api = tweepy.API(auth) 