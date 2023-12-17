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
  
st.download_button(
  label="写真をダウンロードする",
  data="ダウンロードした",
  file_name="写真.txt",
  mime="text/plain"
  )

st.link_button("リンク先に飛ぶ","https://google.co.jp",use_container_width=True)

data_1 = [[3,24,35,46,65,666],[1,2,3,4,5,6]]

#st.write(st.session_state)

st.line_chart(data_1)
