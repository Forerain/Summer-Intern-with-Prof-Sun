import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf 
from tensorflow.keras import models,layers

df = pd.read_csv('C:/Users/lsy/data1.csv')
df.head(10)

dftrain_raw = df.iloc[0:1500,:]
dftest_raw = df.iloc[1500:,:]

def preprocessing(dfdata):
    #preprocess the data 
    dfresult= pd.DataFrame()
    
    #set category column
    dfspacegroup = pd.get_dummies(dftrain_raw['spacegroup'])
    dfspacegroup.columns = ['group_' +str(x) for x in dfspacegroup.columns ]
    dfresult = pd.concat([dfresult,dfspacegroup],axis = 1)
    
    #set numerical columns
    dfresult['atomic_volume'] = dfdata['atomic_volume']
    dfresult['band_gap'] = dfdata['band_gap']
    dfresult['diff_electroneg'] = dfdata['diff_electroneg']
    dfresult['outer_electron'] = dfdata['outer_electron']

    return(dfresult)


x_train = preprocessing(dftrain_raw)
y_train = dftrain_raw['band_gap.is_direct'].values

x_test = preprocessing(dftest_raw)
y_test = dftest_raw['band_gap.is_direct'].values

#define keras model
tf.keras.backend.clear_session()

model = models.Sequential()
model.add(layers.Dense(15,activation = 'relu',input_shape=(34,)))
model.add(layers.Dense(10,activation = 'relu' ))
model.add(layers.Dense(1,activation = 'sigmoid' ))

model.summary()

#train the model
model.compile(optimizer='adam',
            loss='binary_crossentropy',
            metrics=['AUC'])

history = model.fit(x_train,y_train,
                    batch_size= 75,
                    epochs= 30,
                    validation_split=0.2 
                   )

#visualize the results

def plot_metric(history, metric):
    train_metrics = history.history[metric]
    val_metrics = history.history['val_'+metric]
    epochs = range(1, len(train_metrics) + 1)
    plt.plot(epochs, train_metrics, 'bo--')
    plt.plot(epochs, val_metrics, 'ro-')
    plt.title('Training and validation '+ metric)
    plt.xlabel("Epochs")
    plt.ylabel(metric)
    plt.legend(["train_"+metric, 'val_'+metric])
    plt.show()

plot_metric(history,"loss")
plot_metric(history,"AUC")