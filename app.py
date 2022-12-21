# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 15:33:40 2022

@author: User
"""
import streamlit as st
import pandas as pd

#Q13 table
technologies = {
    '組合(1) ': ['0%','20%','80%'],
    '組合(2) ': ['25%','50%','25%'],
    '組合(3) ': ['20%','20%','60%'],
    '組合(4) ': ['80%','10%','10%'],
    '組合(5) ': ['60%','20%','20%']
              }
index_labels=['低風險資產', '中風險資產 ', '高風險資產']
df = pd.DataFrame(technologies,index=index_labels)

question1="Q1.請問您投資的主要目的?"
options1= {
        "為了買房準備頭期款" : 0,
        "為了子女或自已的教育費用" : 0,
         "想要有良好的退休生活" : 0,
         "希望有儲蓄的習慣" : 0,
         "想要與伴侶規劃一場婚禮" : 0
    }

question2_1="Q2請問您的婚姻狀態?"
options2_1 = {"單身":5,"已婚":3}
question2_2="Q2請問您要準備幾位的教育費用? "
options2_2 = {"1位":5,"2位":4,"3位":3,"4位":2,"5位以上":1}
question2_3="Q2請問您是否有投保勞工保險或是國民年金? "
options2_3= {"勞工保險":3,"國民年金":2,"公務人員保險":4,"都沒有":1}
question2_4=" Q2-4請問您儲蓄的主要目的?"
options2_4 = {"不想讓薪水縮水，想要抵抗物價漲價":2,"沒有特別的目的，只想要讓財富增加":3,"為了將來想要移居別的國家做準備":5}
question2_5="Q2請問您與您的伴侶有訂婚嗎? "
options2_5 = {"有":5,"沒有":3}

question14="Q14.請問您比較偏好下列何種投資組合?"
options14 = ["組合(1)","組合(2)","組合(3)","組合(4)","組合(5)"]

Q1answer=st.radio(question1, options1.keys())
if Q1answer=="為了買房準備頭期款":
    Q2answer=st.radio(question2_1,options2_1.keys())
    point = options2_1[Q2answer]
elif Q1answer=="為了子女或自已的教育費用":
    Q2answer=st.radio(question2_2,options2_2.keys())
    point = options2_2[Q2answer]
elif Q1answer=="想要有良好的退休生活":
    Q2answer=st.radio(question2_3,options2_3.keys())
    point = options2_3[Q2answer]
elif Q1answer=="希望有儲蓄的習慣":
    Q2answer=st.radio(question2_4,options2_4.keys())
    point = options2_4[Q2answer]
elif Q1answer=="想要與伴侶規劃一場婚禮":
    Q2answer=st.radio(question2_5,options2_5.keys())
    point = options2_5[Q2answer]
else:
    print("您尚未回答Q1")

questions = [
    ("What is your favorite color?", {"Red": 3, "Blue": 2, "Green": 1}),
    ("What is your favorite animal?", {"Dog": 3, "Cat": 2, "Bird": 1}),
    ("What is your favorite sport?", {"Soccer": 3, "Basketball": 2, "Tennis": 1}),
]
questions = [ (" Q3.請問您的生理性別?", {"男": 5, "女": 3, }),
("Q4.請問您預計多久以後會使用到這筆錢?", {"2年": 1, "5年": 2, "10年": 3, "15年": 4, "20年": 5,}),
("Q5.請問您的目標金額是多少?", {"50萬": 1, "100萬": 2, "300萬": 3, "500萬": 4, "1000萬": 5,}),
("Q6.請問您目前的年齡?", {"20歲-30歲以下": 3,"31歲-40歲以下": 5,"41歲-50歲以下": 4,"51歲-65歲以下": 2,"65歲以上": 1, }),
("Q7.請問您有個人的投資經驗嗎", {"大概投資2年": 2, "已經3年了": 3,"初次投資": 1,"投資老手，投資5年或以上": 5,"投資滿4年": 4, }),
("Q8.請問您對金融商品的理解程度有多少", {"普通": 3, "非常理解，什麼商品都懂": 5,"可能不是很懂": 2,"大概知道啦，大概啦": 4,"我什麼都不懂": 1, }),
("Q9.假設您投資了10萬NTD，您能夠接受自已虧損多少?", {"5萬NTD ": 3, "8萬NTD ": 4,"2萬NTD ": 2,"10萬NTD ": 5,"1塊錢都不能虧": 1, }),
("Q10.假設您投資了10萬NTD，目前已經虧損2萬NTD，您會採取何種行動?", {"賺錢的機會，加碼就對了": 5, "氣定神閒，什麼都不做": 3,"好像有點心痛，是不是要認賠了": 2,"快跑啊，經濟要崩盤了": 1,"好像有賺錢的機會，是不是要加碼": 4, }),
("Q11.投資會您多久會察看一次您的投資情況?", { "佛系投資，想到再看": 5, "每天每分每秒都在看": 1,"有放假才看": 2,"換季才看": 4,"每個月發薪日才看": 3, }),
("Q12.請問您對「風險」這個詞的理解最接近下列選項?", {"我可能會失去所有": 1, "我看到賺更多錢的機會": 5,"我知道這是投資的一部份": 3,"享受投資的快感": 4,"失去一點，是可以承受的": 2, }),
("Q13.請問您比較偏好下列何種投資組合?", {"組合(1)": 5, "組合(2)": 3,"組合(3)": 4,"組合(4)": 1,"組合(5)": 2, }),]
total_score = 0

for question, options in questions:
    answer = st.radio(question, options.keys())
    score = options[answer]
    total_score += score
    if question=="Q13.請問您比較偏好下列何種投資組合?":
        st.dataframe(df)

#Q14
st.write(question14)
value1 = st.slider("每月定期定額", min_value=1000, max_value=1000000,step=1000)
value2 = st.slider("單次投入多少元 ", min_value=10000, max_value=10000000,step=10000)

#總分計算
all_total_score=total_score+point
st.write("Total score:", all_total_score)