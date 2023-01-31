#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plotting_demo：
選用的資產池類型說明
價格走勢圖
@author: hank_deng
"""

import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
def assest_pool_demo():
 
   st.set_option('deprecation.showPyplotGlobalUse', False)
   
   st.markdown(
       """
       資產池
       """
       )
   df = pd.read_csv('AccessPoolType.csv') #Read Assest pool csv
   symbols=df.Tickers.tolist()
   five_years_ago = datetime.now() - timedelta(days=365*5) #Five years end from today
   data = yf.download(symbols, start=five_years_ago, end=datetime.now()) 
   data=data["Adj Close"]
   st.line_chart(data)
   selected_columns = df[["Tickers", "Description", "Category"]]
   st.dataframe(selected_columns,height=500)