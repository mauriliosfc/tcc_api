# coding: utf-8
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

import pandas as pd
import json

ds = SupervisedDataSet(24,1)
tf = pd.read_excel("G1.xlsx")
dados = tf.iloc[:,:23]
res = tf.iloc[:,24]

#ds.setField('input', dados)
ds.setField('target',  res)

# print(res)

# rename = {
#     "Sim":"1",
#     "Nao":"0"
# }
# res = res.map(rename)
# print(res)

# for line in tf.readlines():
#     data = [float(x) for x in line.strip().split(',') if x != ''] 
#     indata =  tuple(data[:])
#     outdata = tuple(data[19:])
#     print(indata)
#     print(outdata)
#     ds.addSample(indata,outdata)

# nn = buildNetwork(ds.indim,8,8,ds.outdim,recurrent=True)
# t = BackpropTrainer(nn,learningrate=0.01,momentum=0.5,verbose=True)
# t.trainOnDataset(ds,100)
# t.testOnData(verbose=True)

# z = nn.activate([(1.0),( 2.0),( 1.0),( 2.0),( 0.0),( 46.0),( 0.0),( 0.0),( 0.0),( 75.0),( 0.0),( 4.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 1.0),( 1.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 0.0),( 0.0),( 0.0),( 1.0)])

# print('Previsao Infeccao', str(z))

# z = nn.activate([(1.0),( 2.0),( 1.0),( 4.0),( 0.0),( 30.0),( 0.0),( 0.0),( 0.0),( 45.0),( 0.0),( 4.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 1.0),( 1.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 1.0),( 0.0),( 0.0),( 1.0)])
# print('Previsao Infeccao', str(z))

# z = nn.activate([(1.0),( 2.0),( 1.0),( 4.0),( 0.0),( 30.0),( 0.0),( 0.0),( 0.0),( 45.0),( 0.0),( 4.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 1.0),( 1.0),( 0.0),( 1.0),( 0.0),( 2.0),( 0.0),( 1.0),( 0.0),( 0.0),( 1.0)])
# print('Previsao Infeccao', str(z))