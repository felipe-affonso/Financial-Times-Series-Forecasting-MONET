#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:47:44 2018

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

us_df = pd.DataFrame(columns=['Stock', 'lines', 'first_Date', 'last_date'])

file_counter = 0
lines = 0

#CONTAGEM LINHAS NYSE
files = os.listdir(initial_path + nyse)

for file_dir in files:
    file = open(initial_path+nyse+file_dir, mode='r', encoding='iso-8859-1')
    file_counter +=1
    for line in file:
        lines += 1
        
    file.close()

print(file_counter)
  

#CONTAGEM LINHAS NASDAQ
files = os.listdir(initial_path + nasdaq)
for file_dir in files:
    file = open(initial_path+nasdaq+file_dir, mode='r', encoding='iso-8859-1')
    file_counter +=1
    for line in file:
        lines += 1
        
    file.close()

print (lines)
us_lines= lines
us_files= file_counter
print("Bolsas Americanas: ", us_files, us_lines)


#CONTAGEM POLONIA
files = os.listdir(initial_path + poland)
for file_dir in files:
    file = open(initial_path+poland+file_dir, mode='r', encoding='iso-8859-1')
    file_counter +=1
    for line in file:
        lines += 1
        
    file.close()
    
pl_lines = lines - us_lines
pl_files = file_counter - us_files
print("Bolsa Polandesa: ", pl_files, pl_lines)
    
#CONTAGEM ALEMANHA
files = os.listdir(initial_path + germany)
for file_dir in files:
    file = open(initial_path+germany+file_dir, mode='r', encoding='iso-8859-1')
    file_counter +=1
    for line in file:
        lines += 1
        
    file.close()

gr_lines = lines - pl_lines - us_lines
gr_files = file_counter - pl_files - us_files
print("Bolsa Alemanha: ", gr_files, gr_lines)
    
    
print("Bolsas Totais: ", file_counter, lines)