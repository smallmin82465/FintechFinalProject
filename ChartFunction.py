#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:24:06 2023

專門放各種繪圖函式的檔案

@author: hank_deng
"""

def gaugeChart(Min,Max,DataValue):
    """
    畫出儀表圖
    需要傳遞的參數:Min,Max,DataValue
    Min:問卷的最低分值
    Max:問卷最高分值
    DataValue:實際得分
    """
    option = {
      "series": [
        {
          "type": 'gauge',
          "startAngle": 180,
          "endAngle": 0,
          "min": Min,
          "max": Max,
          "splitNumber": 10,
          "itemStyle": {
            "color": '#58D9F9',
            "shadowColor": 'rgba(0,138,255,0.45)',
            "shadowBlur": 10,
            "shadowOffsetX": 2,
            "shadowOffsetY": 2
          },
          "progress": {
            "show": True,
            "roundCap": True,
            "width": 18
          },
          "pointer": {
            "icon": 'path://M2090.36389,615.30999 L2090.36389,615.30999 C2091.48372,615.30999 2092.40383,616.194028 2092.44859,617.312956 L2096.90698,728.755929 C2097.05155,732.369577 2094.2393,735.416212 2090.62566,735.56078 C2090.53845,735.564269 2090.45117,735.566014 2090.36389,735.566014 L2090.36389,735.566014 C2086.74736,735.566014 2083.81557,732.63423 2083.81557,729.017692 C2083.81557,728.930412 2083.81732,728.84314 2083.82081,728.755929 L2088.2792,617.312956 C2088.32396,616.194028 2089.24407,615.30999 2090.36389,615.30999 Z',
            "length": '75%',
            "width": 16,
            "offsetCenter": [0, '5%']
          },
          "axisLine": {
            "roundCap": True,
            "lineStyle": {
              "width": 18
            }
          },
          "axisTick": {
            "splitNumber": 2,
            "lineStyle": {
              "width": 2,
              "color": '#999'
            }
          },
          "splitLine": {
            "length": 12,
            "lineStyle": {
              "width": 3,
              "color": '#999'
            }
          },
          "axisLabel": {
            "distance": 30,
            "color": '#999',
            "fontSize": 20
          },
          "title": {
            "show": False
          },
          "detail": {
            "backgroundColor": '#fff',
            "borderColor": '#999',
            "borderWidth": 2,
            "width": '60%',
            "lineHeight": 40,
            "height": 40,
            "borderRadius": 8,
            "offsetCenter": [0, '35%'],
            "valueAnimation": True,
            "formatter":str(DataValue)+'分',
            "rich": {
              "value": {
                "fontSize": 50,
                "fontWeight": 'bolder',
                "color": '#777'
              },
              "unit": {
                "fontSize": 20,
                "color": '#999',
                "padding": [0, 0, -20, 10]
              }
            }
          },
          "data": [
            {
              "value": DataValue
            }
          ]
        }
      ]
    };
    return option


def liquidChart(Max,DataValue):
    """
    畫出液體圖
    需要傳遞的參數:Min,DataValue
    Max:問卷最高分值
    DataValue:實際得分
    """
    liquidfill_option = {
    "series": [{"type": "liquidFill", "data": [DataValue/Max]}]
    }
    return liquidfill_option


def lineChart(Date,Data):
    """
    繪製折線圖
    Date:日期陣列,必須和Data同長度(type:list)
    Data:值陣列,必須和Date同長度(type:list)
    """
    line_options = {
        "title": {"text": "投資金額變化折線圖"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["總金額"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": Date,
     },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "總金額",
                "type": "line",
                "stack": "總量",
                "data": Data ,
         },
     ],
    }
    return line_options



def pieChart(piedata):
    pie_options = {
        """
        資產配置權重pie,piedata必須為value,name{}組合.
        """
        "title": {"text": "資產配置權重圓餅圖", "subtext": "", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "Ticker",
                "type": "pie",
                "radius": "50%",
                "data": piedata,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "normal": {
                        "formatter": '{b}: {d}%'
                        }
                    }                
                }
        ],
    }
    return pie_options
