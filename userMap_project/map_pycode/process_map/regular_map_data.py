# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:26:37 2016

@author: xinruyue
"""

import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = pd.read_json('pro_data.json')

dic = data.province
cities = []
for each in dic:
    name = each['name']
    print name
    if each.has_key('city'):
        cities.append(name)
        city = each['city']
        for each in city:
            nam = each['name']
            print nam
            cities.append(nam)
            if each.has_key('county'):
                coun = each['county']
                if type(coun) == list:
                    for each in coun:
                        na = each['name']
                        print na
                        cities.append(na)
                else:
                    na = each['name']
                    cities.append(na)
print cities
for each in cities:
    if each == u'市辖区' or each == u'县':
        print each
        cities.remove(each)

with open('all_pro_data.txt','w') as p:
    for each in cities:
        p.write(each)
        p.write('\n')
p.close()

loc = []

for each in cities:
    if len(each) > 2:
        if u'省' in each:
            each = each.strip(u'省')
        if u'市' in each:
            each = each.strip(u'市')
        if u'县' in each:
            each = each.strip(u'县')
        if u'区' in each:
            each = each.strip(u'区')
    loc.append(each)
    
with open('all_pro_data_1.txt','w') as p:
    for each in loc:
        p.write(each)
        p.write('\n')
p.close()        
