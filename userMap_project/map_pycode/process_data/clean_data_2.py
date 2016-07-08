# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:47:43 2016

@author: xinruyue
"""
import pandas as pd

name = ['place']
data = pd.read_csv("loc_data.csv",names=name,encoding='utf-8')

count = data['place'].value_counts()
print count

count.to_csv('count_pc.csv')
