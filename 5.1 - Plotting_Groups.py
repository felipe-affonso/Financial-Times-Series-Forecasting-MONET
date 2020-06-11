#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:22:42 2018

@author: FelipeAffonso
"""

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
import matplotlib.pyplot as plt

nyse = "/US/NYSE/"
nasdaq = "/US/NASDAQ/"
poland = "/PL/WSE/"
germany = "/GR/XETRA/"

pais = nasdaq

clusters_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Clusters"+pais

image_path = clusters_path
#ALTERAR NUMERO DE PASTAS A SEREM PERCORRIDAS DE ACORDO COM O NUMERO DE GRUPOS CRIADOS
for i in range(0,20):
    group_path = clusters_path+str(i)+"/"

    files = os.listdir(group_path)
    
    my_dict = {}
    dataset = {}
    for f in files:
        if not f.startswith('.'):
            stock_name = f.split('.')
            dataset[stock_name[0]] = pd.read_csv(group_path+f)
        
    for name, df in dataset.items():
        df['log'] = np.log(df.Close)
        plt.plot(df.index.values, df['log'])
        
    plt.savefig(image_path+'Group_'+str(i), dpi=500)
    plt.clf()



    
    
            
            