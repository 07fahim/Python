import streamlit as st
import numpy as np 
import pandas as pd

## Tittle of the app
st.title("Hello Streamlit")

## Display simple text
st.write("Hey What's upp")

## Create a dataframe
df=pd.DataFrame({
    'First Column':[1,2,3,4,5],
    'Second Column':[10,20,30,40,50]
})

## Display dataframe
st.write("Here is my Dataframe")
st.write(df)

## Create a line chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)