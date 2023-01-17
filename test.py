#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:42:54 2023

@author: hank_deng
"""
import streamlit as st
import os
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import json
st.set_option('deprecation.showPyplotGlobalUse', False)

with open('question.json') as f:
    data = json.load(f)
    
for i in range(data):
    answer = st.radio(data[i]['Questions'], data[i]['Options'].keys())
    score = answer
