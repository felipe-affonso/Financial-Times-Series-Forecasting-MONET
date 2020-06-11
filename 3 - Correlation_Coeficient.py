#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:08:12 2018

@author: FelipeAffonso
"""

import numpy as np
import math
import csv
import os
import pandas as pd

initial_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Filtered"

resultado = "/NYSE - CORRELATION MATRIX.csv"
result_file = open(initial_path+resultado, 'w')

nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

pais = nyse

files = os.listdir(initial_path + pais)
writer = csv.writer(result_file, quoting=csv.QUOTE_NONE, delimiter=' ', quotechar='', escapechar='\\')

chaves = []

for file_dir in files:
    if not file_dir.startswith('.'):
        for file_2_dir in files:
            texto = []
            if not file_2_dir.startswith('.'):
                acao_a = file_dir.split('.')
                acao_b = file_2_dir.split('.')
                acao_a = acao_a[0]
                acao_b = acao_b[0]
                if (acao_a not in chaves and acao_b not in chaves):
                    df_x = pd.read_csv(initial_path+pais+file_dir, sep=",")
                    df_y = pd.read_csv(initial_path+pais+file_2_dir, sep=",")
                    x = df_x['Close']
                    y = df_y['Close']
                    correlation = np.corrcoef(x, y)
                    correlation = correlation[0][1]
                    
                    before_distance = (2 * (1 - correlation))
                    if before_distance > 0:
                        distancia = math.sqrt(before_distance)
                    else:
                        distancia = 0
                    texto.append(acao_a+'|'+acao_b+'|'+str(correlation)+'|'+str(distancia))
                    writer.writerow(texto)
                    del(texto)
        chaves.append(acao_a)
                
result_file.close()
