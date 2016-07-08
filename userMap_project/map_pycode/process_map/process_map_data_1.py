# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:44:20 2016

@author: xinruyue
"""

import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = pd.read_json('pro_data.json')
dic = data.province

province = []
for each in dic:
    name = each['name']
    if u'省' in name:
        name = name.strip(u'省')
    if u'市' in name:
        name = name.strip(u'市')
    province.append(name)

for each in dic:
    n = each['name']
    if each.has_key('city'):
        city = each['city']
        c = []
        for each in city:
            na = each['name']
            if na == u'市辖区' or na == u'县':
                continue
            else:        
                c.append(na)

        with open(n + '.txt','w') as f:
            for each in c:
                f.write(each)
                f.write('\n')
            f.close()
    

with open("province_name.txt",'w') as pn:
    for each in province:
        pn.write(each)
        pn.write('\n')
    pn.close()
            