# Pour le lancer : streamlit run data.py
import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["Harsh", "Gupta"],
    "age":[21,32],
    "city":["noida", "dalhi"]
}

data = pd.read_csv("/Users/yann/Desktop/Ydays/Data/WebScraping/Alvergnas1.csv")
#print(data)
st.dataframe(data)
st.table(dic)
st.json(dic)
st.write(dic)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))