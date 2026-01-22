import streamlit as st 
st.title("Basic Calculator")
num1=st.number_input("Enter first number")
num2=st.number_input("Enter second number")

operation=st.selectbox("choose operation",["add","subtract","multiply","divide"])
if st.button("Calculate"):
    if operation=="add":
        st.write(num1+num2)
    elif operation=="subtract":
        st.write(num1-num2)
    elif operation=="multiply":
        st.write(num1*num2)
    elif operation=="divide":
        st.write(num1/num2)
    else:
        st.write("invalid operation")