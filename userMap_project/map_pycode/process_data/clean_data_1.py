# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:20:06 2016

@author: xinruyue
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from collections import OrderedDict

import re

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

#导入各省市名称文件
cities = []
with open("all_pro_data_1.txt",'r')as p:
    for each in p:
        each = each.rstrip()
        cities.append(each)

py_cities = []
with open("cpy_all_pro_data_1.txt",'r') as pp:
    for each in pp:
        each = each.rstrip()
        py_cities.append(each)

#获取拼音名称的地区
map_data = []
with open("count_pc.csv",'r') as ld:
    for each in ld:
        each = each.rstrip()
        map_data.append(each)

org_pinyin = []
hanzi = []        
for each in map_data:
    if is_chinese(each) == False:
        org_pinyin.append(each)
    else:
        hanzi.append(each)

py_data = OrderedDict()
for each in org_pinyin:
    each = each.split(',')
    py_data[each[0]] = each[1]
pinyin = py_data.keys()
print len(pinyin)
#匹配和替换拼音地名
for each_word in pinyin:
    pattern = re.compile(r'([A-Z][a-z]+)')
    l = re.split(pattern,each_word)
    while '' in l:
        l.remove('')
    while ' ' in l:
        l.remove(' ')
    if len(l) == 2:
        former = l[0]
        latter = l[1]
        try:
            pro_idx = py_cities.index(former)
            pro = cities[pro_idx]
            cap_idx = py_cities.index(latter)
            cap = cities[cap_idx]
            new_word = pro + '省' + cap + '市'
            pinyin[pinyin.index(each_word)]=new_word
        except:
            pinyin[pinyin.index(each_word)]=pro + '省'
    else:
        print each_word

clean_py_data = {}
values = py_data.values()
for each in pinyin:
    clean_py_data[each] = values[pinyin.index(each)]

for key,value in clean_py_data.items():
    if is_chinese(key) == False:
        del clean_py_data[key]

with open('final_data.txt','w') as fd:
    for each in hanzi:
        fd.write(each)
        fd.write('\n')
    for key,value in clean_py_data.items():
        fd.write(key)
        fd.write(',')
        fd.write(value)
        fd.write('\n')
    fd.close()
    
 