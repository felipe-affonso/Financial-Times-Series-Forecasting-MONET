#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 17:03:28 2018

@author: FelipeAffonso
"""

import numpy as np
import pandas as pd
import csv
import os

nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

pais = nyse

clusters_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Clusters"+pais

#ALTERAR NUMERO DE PASTAS A SEREM PERCORRIDAS DE ACORDO COM O NUMERO DE GRUPOS CRIADOS
for i in range(0,20):
    group_path = clusters_path+str(i)+"/"

    files = os.listdir(group_path)
    
    my_dict = {}
    for f in files:
        file = open(group_path+f, mode='r', encoding='iso-8859-1')
        count = 0;
        for line in file.readlines():
            if (count == 0):
                count+=1
            else:
                line = line.split(',')
                date = line[0]
                close = float(line[4])
                if date in my_dict:
                    my_dict[date] = float(my_dict.get(date))+close
                else:
                    my_dict[date] = close
        file.close()
        
        n = len(files)
        
        for d in my_dict.keys():
            my_dict[d] = my_dict.get(d)/n
            
    result_file = clusters_path+"Group_"+str(i)+".csv"
    df = pd.DataFrame(list(my_dict.items()), columns=['Date', 'Close'])
    df = df.sort_values('Date')
    df.to_csv(result_file, sep=',', index=None)
    
    
            
            