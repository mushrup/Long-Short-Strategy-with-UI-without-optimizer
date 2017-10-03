from zipline.api import *
from matplotlib import style
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
style.use('ggplot')

def get_LongPricing(portfolio,date):
  total = 0
  for token in portfolio:
    try:
      df = pd.DataFrame.from_csv(token+'_adj_.csv')
      price = df.loc[date,'Close']
      total = price + total
    except:
      pass
  return total

def get_ShortPricing(portfolio,date):
  total = 0
  for token in portfolio:
    try:
      df = pd.DataFrame.from_csv(token+'_adj_.csv')
      price = df.loc[date,'Close']
      total = price + total
    except:
      pass
  return total

def initialize(context):
    df = pd.DataFrame(pd.read_csv('bridge.csv',encoding = 'utf-8',converters={'long': lambda x: str(x),'short': lambda x: str(x)}))
    context.longs = df['long']
    context.shorts = df['short']

def handle_data(context, data):
    date = pd.to_datetime(get_datetime()).date()
    Long_price = get_LongPricing(context.longs,date)
    Short_price = get_ShortPricing(context.shorts,date)
    Equity = Long_price - Short_price
    try:
      Leverage = Short_price/Equity
    except:
      Leverage = 0
    record(DATE = date,LONG = Long_price,SHORT = -Short_price, EQUITY = Equity, LEVERAGE = Leverage)

def analyze(context=None, results=None):
  
  print (results.LONG.loc['2015-02-01':'2015-02-28'])
  results.LONG.replace(0, np.nan, inplace=True)
  results.SHORT.replace(0, np.nan, inplace=True)
  results.EQUITY.replace(0, np.nan, inplace=True)
  results.LEVERAGE.replace(0, np.nan, inplace=True)

  results.LONG.fillna(method = 'ffill', inplace=True)
  results.SHORT.fillna(method = 'ffill', inplace=True)
  results.EQUITY.fillna(method = 'ffill', inplace=True)
  results.LEVERAGE.fillna(method = 'ffill', inplace=True)
  print (results.LONG.loc['2015-02-01':'2015-02-28'])

  # Graph 1
  plt.figure(figsize=(50,5))
  ax = results.LONG.plot()
  ax.set_title('Long Short Position')
  results.EQUITY.plot(ax = ax)

  # Graph 2
  plt.figure(figsize=(50,5))
  ax2 = results.LEVERAGE.plot()
  ax2.set_title('Leverage rate')
  plt.show()




