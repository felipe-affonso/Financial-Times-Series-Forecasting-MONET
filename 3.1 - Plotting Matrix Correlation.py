#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:52 2018

@author: FelipeAffonso
"""
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.sparse as sps

sns.set(style="white")

initial_path = "/Users/FelipeAffonso/OneDrive/Pós Graduação/Mestrado/Machine Learning/Trabalho Final/Código/Dataset/Filtered"
resultado = "/NYSE - CORRELATION MATRIX.csv"
end_file = "/NYSE - DATA FRAME - MATRIX - CORRELATION.CSV"
path = initial_path + resultado

# Opening dataset
df = pd.read_csv(initial_path+resultado, sep="|", header=None)
columns = df[0].unique()


#verificar se existem valores nulos
nan_rows = df[df[1].isnull()]
nan_rows

#transforming into matrix
rows = df[0]
col = df[1]
val = df[2]

matrix = pd.DataFrame({'Stock_A':rows, 'Stock_B':col, 'Correlation': val})
matrix.set_index(['Stock_A', 'Stock_B'], inplace=True)
mat = sps.coo_matrix((matrix['Correlation'],(matrix.index.labels[0], matrix.index.labels[1])))
print(mat.todense())

#matrix to array
new_matrix = mat.toarray()

new_df = pd.DataFrame(new_matrix, index=columns, columns=columns)

new_df.to_csv(initial_path+end_file, sep=',')

#ploting
#plt.pcolor(new_df)
#plt.yticks(np.arange(0.1, len(new_df.index), 1), new_df.index)
#plt.xticks(np.arange(0.1, len(new_df.columns), 1), new_df.columns)
#plt.show()


# plot heatmap
ax = sns.heatmap(new_df.T, vmin=-1, vmax=1, center=0, cmap="YlGnBu")

# turn the axis label
for item in ax.get_yticklabels():
    item.set_rotation(0)

for item in ax.get_xticklabels():
    item.set_rotation(90)

# save figure
plt.savefig("NYSE- DATA FRAME - MATRIX - CORRELATION", dpi=1000)
plt.show()

