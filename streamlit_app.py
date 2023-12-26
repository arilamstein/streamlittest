import streamlit as st

st.header('Button app!')

if st.button('Say Hello'):
    st.write('Hello')
else:
    st.write('Goodbye')
