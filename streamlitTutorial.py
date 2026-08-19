import streamlit as st
import pandas as pd
import numpy as np


st.title("hello guys!! ")
name=st.text_input("Ask you questions")

st.write("this is your first streamlit app")
st.text("lets get started")
name=st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"hello,{name}")

#how to upload any file
upload_file = st.file_uploader("upload a csv file",type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is header")
st.subheader("this is subheader")
st.markdown("[Link](https://streamlit.io/)")
st.text_area("write your message")
st.number_input('pick a number',  min_value=0, max_value=10)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["amba","kela","santra"])
st.multiselect("select language",["java","python","cpp"])
st.radio("pick one",["option A","option B"])
st.checkbox("i agree Terms and Conditions")

#form tags
with st.form("login form"):
    username=st.text_input("username")
    password=st.text_input("password",type="password")
    submitted=st.form_submit_button("login")

    if submitted:
        st.success(f"welcome {username}")

    df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)

