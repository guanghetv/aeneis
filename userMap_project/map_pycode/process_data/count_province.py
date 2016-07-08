# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 16:28:57 2016

@author: xinruyue
"""
# from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json

loc = {}
data = open('final_data.txt','r')
for each in data:
    each = each.strip('\n')
    each = each.split(',')
    loc[each[0]] = int(each[1])

pro_count = []
with open('province_name.txt','r') as pn:
    for each in pn:
        each_count = {}
        num = 0
        each = each.strip('\n')
        for key,value in loc.items():
            if each in key:
                num += value
        each_count['name'] = each
        each_count['value'] = num
        pro_count.append(each_count)

# pro_count = OrderedDict(sorted(pro_count.items(),key = lambda x:x[1],reverse=True))
with open('map_data.txt','w') as f:
    json.dump(pro_count,f,ensure_ascii=False,indent=4)
# for key,value in pro_count.items():
#     print key,value