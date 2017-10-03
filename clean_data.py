from zipline.api import *
from matplotlib import style
import csv
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Date_template.csv',index_col = ['Date'])
df = df.drop(['Symbol','Open','High','Low','Close','Close_Adj'], 1)

tokens = ['00905','00218','01476','01297','02100','08106','08206','08236']

for token in tokens:
  df2 = pd.read_csv(token+'_adj.csv',index_col = ['Date'])
  df2.replace(0,np.nan,inplace=True)
  df2.fillna(method = 'ffill',inplace=True)
  result = df.join( df2, how = 'outer')
  result.index.name = 'Date'
  result.fillna(method = 'ffill',inplace=True)
  result.fillna(method = 'bfill',inplace=True)
  result.drop(['Volumn'] , 1 , inplace=True)
  result.to_csv(token+'_adj_.csv', encoding ='utf-8')

'''
df1 = pd.read_csv()
pd.concat()
'''

