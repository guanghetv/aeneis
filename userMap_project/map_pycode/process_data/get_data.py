# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:23:06 2016

@author: xinruyue
"""
from pymongo import MongoClient
import sys

reload(sys)
sys.setdefaultencoding('utf8')

userAttr = MongoClient("10.8.8.111:27017")['cache']['userAttr']

#user "from" to split data 
platform = ['teacher','mobile','ios','pc','android']
#get loc data
loc_data = []
for each in platform:
    pipeline = [
    {"$match":{"from":each}},
    {"$group":{"_id":"None","location":{"$push":"$location"}}}]
    
    loc_data += list(userAttr.aggregate(pipeline))[0]['location']
print len(loc_data)

#save data as csvfile
with open ("loc_data.csv",'w') as ld:
    for each in loc_data:
        if each != None:
            ld.write(each + '\n')
ld.close()
