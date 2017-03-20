# -*- coding: utf-8 -*-

import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
import unicodedata

def analyze(handle):
    twitter_consumer_key = 'KbkK2ZR6ztGjdXEV8f5mDtPnt'
    twitter_consumer_secret = 'jskCfNPfid93B3UIjueyxKCH9AcafU3BgcVLnEYgwIhnZDN2Pn'
    twitter_access_token = '44017949-usl03eZ8zRVKI2cieLXzeYSKkvbPiwziMRet2qhYi'
    twitter_access_secret = 'Mu1im6RpnUFf2p1Zi2m2ZL4cR2m06KvMqII6RTzNIRoAB'

    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)


    statuses = twitter_api.GetUserTimeline(screen_name=handle,count=42,include_rts=True)

    text = ""




    for status in statuses:
        status = status.len("en")
        text += status.text.encode('utf-8')

    print text

    pi_username = "1ba1f5dd-421f-46f2-9cf2-3b97298a3642"
    pi_password = "s0YxNZCqf1KV"

    personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
    pi_result = personality_insights.profile(text)
    return pi_result

def flatten(orig):
  data = {}
  for c in orig['tree']['children']:
    if 'children' in c:
      for c2 in c['children']:
        if 'children' in c2:
          for c3 in c2['children']:
            if 'children' in c3:
              for c4 in c3['children']:
                if (c4['category'] == 'personality'):
                  data[c4['id']] = c4['percentage']
                  if 'children' not in c3:
                    if (c3['category'] == 'personality'):
                      data[c3['id']] = c3['percentage']
  return data

def compare(dict1, dict2):
  compared_data = {}
  for keys in dict1:
    if dict1[keys] != dict2[keys]:
      compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

user_handle = "@sudoferraz"
celebrity_handle = "@pythontrending"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)


user = flatten(user_result)
celebrity = flatten(celebrity_result)



compared_results = compare(user, celebrity)

sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

for keys, value in sorted_result[:5]:
    print keys,
    print(user[keys]),
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])

print sorted_result
print user
"""
# role em ptbr
for status in statuses:
    status = status.text
    status = unicodedata.normalize('NFKD', status)
    status = status.encode('ascii', 'ignore')
    print status
"""
