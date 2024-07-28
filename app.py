import streamlit as st
st.title('SPHERE CALCULATION')
number = st.number_input("Insert a number")
if st.button("Calculate"):
  st.write("the number is", number)
