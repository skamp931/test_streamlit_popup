import streamlit as st
import time


st.write("テストデータ記載します")
st.header('Configuration： Theme')
st.checkbox(label='Check')
st.slider(label='Slider')
b = st.empty()
a = st.selectbox(label='Choose Your Favourite', options=['Snowpeak', 'Rakuten', 'Toyota Motors'])
st.write(a)
b = "and"

if st.button("クリック",help = "クリックするとandが表示されます",use_container_width=True,on_click=lambda:st.write("クリックされました")):
  st.write(b)
  
