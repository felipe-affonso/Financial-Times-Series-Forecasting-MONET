#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:56:51 2018

@author: FelipeAffonso
"""

import math
import csv
import os
import pandas as pd

initial_path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Dataset/"
new_path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Dataset/Filtered" 

nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

pais = germany

dias = []
count = 0
files = os.listdir(initial_path + pais)
for file in files:
    if not file.startswith('.'):
        data = pd.read_csv(initial_path+pais+file, sep=",")
        newdf = data[(data['Date']>'2007-12-31') & (data['Date']<='2018-03-29')]    
        dias.append(newdf.shape[0])
        
        if (newdf.shape[0] == 2603):
            count+=1
            newvar = file.split('.')
            newdf.to_csv(new_path+pais+newvar[0]+'.csv', index=False, float_format='%.3f')

print (max(dias, key = dias.count))
print (count)

    
        
