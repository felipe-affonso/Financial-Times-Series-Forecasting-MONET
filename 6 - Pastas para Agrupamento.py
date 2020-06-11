#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:41:27 2018

@author: FelipeAffonso
"""

import numpy as np
import pandas as pd
import csv
import os
from shutil import copyfile

#CRIANDO GRUPOS
nyse_g = "/NYSE"
nasdaq_g = "/NASDAQ"
poland_g = "/POLAND"
germany_g = "/GERMANY"
pais_grupo = nyse_g

group_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Filtered"+pais_grupo+" - AGRUPAMENTO CORRELATION.CSV"
groups = pd.read_csv(group_path, sep=",", header=0, index_col=None)
groups.columns = ['Stock', 'Grupo']

listagem_grupos = groups['Grupo'].unique()
listagem_grupos.sort()


#ABRINDO PASTA DAS ACOES
nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

pais = nyse

stock_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Filtered"+pais

files = os.listdir(stock_path)

#CRIANDO DIRETORIO FINAL
clusters_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Clusters"+pais

for f in files:
    if not f.startswith('.'):
        file = f.split('.')
        file = file[0]
        src = stock_path+f
        
        g = groups[groups['Stock']==file]
        g = g.iloc[0][1]
        
        folder = clusters_path+str(g)
        
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        dst = folder+"/"+f
        copyfile(src, dst)
    



