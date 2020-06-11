#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:18:20 2018

@author: FelipeAffonso
"""
import scipy.cluster.vq
import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


initial_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Filtered"
end_file = "/NASDAQ - DATA FRAME - MATRIX - CORRELATION.CSV"
final_file = "/NASDAQ - AGRUPAMENTO CORRELATION.CSV"
path = initial_path + end_file

df = pd.read_csv(path, sep=",", header=0, index_col=0)

W = scipy.cluster.vq.whiten(df)

#NUMERO DE CLUSTERS
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 100):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(W)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 100), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#########
#finalizando
K = scipy.cluster.vq.kmeans(W, 20)
VQ = scipy.cluster.vq.vq(W, K[0])
groups = VQ[0]

groups = pd.DataFrame(data = groups, index=df.index.values)

groups.to_csv(initial_path+final_file, sep=',')
#################