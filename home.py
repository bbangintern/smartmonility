import streamlit as st

st.write('# HI WELCOME MY APP!')

st.write("반갑습니다. 저의 웹에 오신것을 환영합니다. 재밌네요")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

import datetime

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

