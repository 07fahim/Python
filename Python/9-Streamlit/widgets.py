import streamlit as st

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

age=st.slider("Enter your age:",0,100,25)
st.write(f"{name} age is {age}")    