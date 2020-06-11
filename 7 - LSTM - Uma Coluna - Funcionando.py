#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:42:29 2018

@author: FelipeAffonso
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 16:20:17 2018

@author: FelipeAffonso
"""

# -*- coding: utf-8 -*-
 
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.layers import  Dropout
import matplotlib.ticker as mtick
import os
import csv 

paises = ['/US/NYSE/']
image_path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Images/"
result_path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Dataset/LSTM_Metrics.csv"
result_file = open(result_path, 'w')
writer = csv.writer(result_file, quoting=csv.QUOTE_NONE, delimiter=' ', quotechar='', escapechar='\\')



texto = []
texto.append('COUNTRY'+'|'+"GRUPO"+'|'+"ACCURACY_TRAIN"+'|'+"MSE_TRAIN"+'|'+"ACCURACY_TEST"+'|'+"MSE_TEST"+"|Tendency")
                
for pais in paises:
    
    path = "C:/Users/Felipe Affonso/Documents/Monet/Código/Dataset/Clusters"+pais
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(path+file):
            if not file.startswith('.'):
                p = pais.split('/')
                p = p[2]
                
                f = file.split('.')
                f = f[0]
                fname=path+file
                print(fname)
                
                data_csv = pd.read_csv(fname)
     
                #how many data we will use 
                # (should not be more than dataset length )
                data_to_use= len(data_csv)
                 
                # number of training data
                # should be less than data_to_use
                train_end =int(data_to_use*0.8)
                total_data=len(data_csv)
                 
                #most recent data is in the end 
                #so need offset
                start=total_data - data_to_use
                 
                 
                #currently doing prediction only for 1 step ahead
                steps_to_predict =1
                yt = data_csv.iloc [start:total_data ,1]
                yt_ = yt.shift (-1)
                data = pd.concat ([yt, yt_,], axis =1)
                data. columns = ['yt', 'yt_']
                         
                data = data.dropna()
                # target variable - closed price
                # after shifting
                y = data ['yt_']
                cols =['yt']
                x = data [cols]
                 
                scaler_x = preprocessing.MinMaxScaler ( feature_range =( -1, 1))
                x = np. array (x).reshape ((len( x) ,len(cols)))
                x = scaler_x.fit_transform (x)
                 
                    
                scaler_y = preprocessing. MinMaxScaler ( feature_range =( -1, 1))
                y = np.array (y).reshape ((len( y), 1))
                y = scaler_y.fit_transform (y)
                 
                     
                x_train = x [0: train_end,]
                x_test = x[ train_end +1:len(x),]    
                y_train = y [0: train_end] 
                y_test = y[ train_end +1:len(y)]  
                x_train = x_train.reshape (x_train. shape + (1,)) 
                x_test = x_test.reshape (x_test. shape + (1,))
                 
                     
                #creating Model 
                fit1 = Sequential ()
                fit1.add (LSTM (  1000, activation = 'tanh', inner_activation = 'hard_sigmoid' , input_shape =(len(cols), 1) ))
                fit1.add(Dropout(0.2))
                fit1.add (Dense (output_dim =1, activation = 'linear'))
                 
                fit1.compile (loss ="mean_squared_error" , optimizer = "adam", metrics=['accuracy'])   
                fit1.fit (x_train, y_train, batch_size =16, nb_epoch =25, shuffle = False)
                
                acc_train, score_train = fit1.evaluate (x_train, y_train, batch_size =1)
                acc_test, score_test = fit1.evaluate (x_test, y_test, batch_size =1)
        
              
                
                pred1 = fit1.predict (x_test) 
                pred1 = scaler_y.inverse_transform (np. array (pred1). reshape ((len( pred1), 1)))
                     
                  
                prediction_data = pred1[-1]     
                    
                #print ("Inputs: {}".format(fit1.input_shape))
                #print ("Outputs: {}".format(fit1.output_shape))
                #print ("Actual input: {}".format(x_test.shape))
                #print ("Actual output: {}".format(y_test.shape)) 
                #print ("prediction data:")
                #print (prediction_data)
                #print ("actual data")
                
                x_test = scaler_x.inverse_transform (np. array (x_test). reshape ((len( x_test), len(cols))))
                
                #print (x_test)
                 
                
                
                y_tendency = []
                for i in range(1, len(y_test)):
                    if (y_test[i-1][0] < y_test[i][0]):
                        y_tendency.append(1) #up
                    elif (y_test[i-1][0] > y_test[i][0]):
                        y_tendency.append(0) #down
                    else:
                        y_tendency.append(-1) #equal
                    
                
                pred_tendency = []
                for i in range(1, len(pred1)):
                    if (pred1[i-1][0] < pred1[i][0]):
                        pred_tendency.append(1) #up
                    elif (pred1[i-1][0] >pred1[i][0]):
                        pred_tendency.append(0) #down
                    else:
                       pred_tendency.append(-1) #equal
                
                count = 0
                for i in range(1, len(pred_tendency)):
                    if (pred_tendency[i] == y_tendency[i]):
                        count+=1
                
                print()
                
                texto.append(p+'|'+f+'|'+str(acc_train)+'|'+str(score_train)+'|'+str(acc_test)+'|'+str(score_test)+'|'+str(count/len(pred_tendency)*100))
                
                #PLOT RESULT
                plt.plot(pred1, label="predictions")
                y_test = scaler_y.inverse_transform (np. array (y_test). reshape ((len( y_test), 1)))
                plt.plot( [row[0] for row in y_test], label="actual")
                plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                          fancybox=True, shadow=True, ncol=2)
                fmt = '$%.0f'
                tick = mtick.FormatStrFormatter(fmt)
                 
                ax = plt.axes()
                ax.yaxis.set_major_formatter(tick)
                #plt.show()0
                plt.savefig(image_path+p+'_'+f, dpi=1000)
                plt.clf()

for t in texto:
    writer.writerow([t])

result_file.close()




#plot model
#from keras.utils.vis_utils import plot_model
#plot_model(fit1,to_file='model_plot.png', show_shapes=True, show_layer_names=True)