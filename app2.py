import streamlit as st 
st.title("kindly add city and age")
age=st.slider("enter your age",1,100)
city=st.selectbox("select your city",["new york","los angeles","chicago","houston","phoenix"])
if st.button("submit"):
    st.write("age",age)
    st.write("city",city)