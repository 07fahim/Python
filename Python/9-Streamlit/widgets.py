import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")


age=st.slider("Enter your age:",0,100,25)
st.write(f"{name} age is {age}")

options=['C','C++','Java','Python','Dart','JavaScript']
choice=st.selectbox("Choice your favourite language:",options)
st.write(f"You selected {choice}.")

data = {
"Name": ["John", "Jane", "Jake", "Jill"],
"Age": [28, 24, 35, 40],
"City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
df.to_csv("Sample data.csv")
st.write(df)

uploded_file=st.file_uploader("Choose a CSV file",type='csv')

if uploded_file is not None:
    df=pd.read_csv(uploded_file)
    st.write(df)