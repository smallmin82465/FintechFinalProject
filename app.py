#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main for the stremlit app
Created on Mon Jan 30 15:07:39 2023
@author: hank_deng
"""
import streamlit as st

st.write("# 長庚大學風險評估理財建議模擬👋")
st.sidebar.success("選擇服務")
with open("Homepage.md") as f:
    content = f.read()
st.markdown(content)
    