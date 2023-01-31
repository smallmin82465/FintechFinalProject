#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
intro:
    首頁
    標題

@author: hank_deng
"""

def intro():
    import streamlit as st

    st.write("# 長庚大學風險評估理財建議模擬👋")
    st.sidebar.success("選擇服務")
    st.markdown(
    """
        ## **👈 在左側中選擇想要的服務**
        
        -首頁：此頁面.
        
        -資產池一覽：理財規劃所選用的資產池及每個資產池的類型及說明,包含截至今日的價格走勢圖.
        
        -無問卷隨機理財規劃：隨機分配資產池中的權重並進行理財規劃分析.
        
        -填寫風險評估問卷：填寫問卷根據風險評估分數進行適合使用者的理財規劃.
    """
    )