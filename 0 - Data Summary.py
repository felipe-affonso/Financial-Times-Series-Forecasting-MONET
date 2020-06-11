#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:20:59 2018

@author: FelipeAffonso
"""

import math
import csv
import os
import pandas as pd

initial_path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Dataset"

nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

us_df = pd.DataFrame(columns=['Stock', 'lines'])

files = os.listdir(initial_path + nyse)



for file_dir in files:
    lines = 0
    file = open(initial_path+nyse+file_dir, mode='r', encoding='iso-8859-1')
    for line in file:
        if (lines != 0):
            lines += 1
        
    file_name = file    
    us_df.append({'Stock': file_name}, ignore_index=True)
        
        
    file.close()