#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:07:39 2023
@author: hank_deng
"""
import streamlit as st
import intro , Assestpool


def random_demo():
    import pandas as pd
    import random
    st.title("無問卷隨機理財規劃")
    df = pd.read_csv('AccessPoolType.csv') #Read Assest pool csv
    symbols=df.Tickers.tolist()
    symcount=len(symbols)

    def generate_random_numbers(n):
        total = 1
        num_list = []
        for i in range(n-1):
            num = round(random.uniform(0, total), 2)
            num_list.append(num)
            total -= num
            num_list.append(total)
            random.shuffle(num_list)
            return num_list

    st.write(generate_random_numbers(4))

    
    
def data_frame_demo():
    import altair as alt
    import pandas as pd
    import streamlit as st
    from vega_datasets import data
    
    

    @st.experimental_memo
    def get_data():
        source = data.stocks()
        source = source[source.date.gt("2004-01-01")]
        return source
    
    @st.experimental_memo(ttl=60 * 60 * 24)
    def get_chart(data):
        hover = alt.selection_single(
            fields=["date"],
            nearest=True,
            on="mouseover",
            empty="none",
            )

        lines = (
            alt.Chart(data,width=1200, height=600, title="Evolution of stock prices")
            .mark_line()
            .encode(
                x=alt.X("date", title="Date"),
                y=alt.Y("price", title="Price"),
                color="symbol",
                )
            )

        # Draw points on the line, and highlight based on selection
        points = lines.transform_filter(hover).mark_circle(size=65)
        
        # Draw a rule at the location of the selection
        tooltips = (
            alt.Chart(data)
            .mark_rule()
            .encode(
                x="yearmonthdate(date)",
                y="price",
                opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
                tooltip=[
                    alt.Tooltip("date", title="Date"),
                    alt.Tooltip("price", title="Price (USD)"),
                    ],
                )
            .add_selection(hover)
            )
        
        return (lines + points + tooltips).interactive()
    
    
    st.title("⬇ Time series annotations")
    
    st.write("Give more context to your time series using annotations!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker = st.text_input("Choose a ticker (⬇💬👇ℹ️ ...)", value="⬇")
        with col2:
            ticker_dx = st.slider(
                "Horizontal offset", min_value=-30, max_value=30, step=1, value=0
                )
            with col3:
                ticker_dy = st.slider(
                    "Vertical offset", min_value=-30, max_value=30, step=1, value=-10
                    )
                
                # Original time series chart. Omitted `get_chart` for clarity
                source = get_data()
                chart = get_chart(source)
                

                # Create a chart with annotations
                annotations_df = pd.DataFrame( columns=["date", "event"])
                annotations_df.date = pd.to_datetime(annotations_df.date)
                annotations_df["y"] = 0
                annotation_layer = (
                    alt.Chart(annotations_df)
                    .mark_text(size=15, text=ticker, dx=ticker_dx, dy=ticker_dy, align="center")
                    .encode(
                        x="date:T",
                        y=alt.Y("y:Q"),
                        tooltip=["event"],
                        )
                    .interactive()
                    )
                
                # Display both charts together
                st.altair_chart((chart + annotation_layer).interactive(), use_container_width=True)

page_names_to_funcs = {
    "首頁": intro.intro,
    "資產池一覽": Assestpool.assest_pool_demo,
    "無問卷隨機理財規劃": random_demo,
    "填寫風險評估問卷": data_frame_demo
}
demo_name = st.sidebar.selectbox("選擇想進行的服務", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()