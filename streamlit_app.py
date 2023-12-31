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

option = st.sidebar.selectbox(
  "オプションを選択してください",
  ("option_1","option_2","option_3"))
st.write("選択したオプション：",option)

if option == "option_1":
  if st.button("ページ１のボタン"):
    st.title("ページ１のタイトル")


if st.button("クリック",help = "クリックするとandが表示されます",use_container_width=True,on_click=lambda:st.write("クリックされました")):
  st.write(b)
  
st.download_button(
  label="写真をダウンロードする",
  data="ダウンロードした",
  file_name="写真.txt",
  mime="text/plain"
  )

st.link_button("リンク先に飛ぶ","https://google.co.jp",use_container_width=True)

data_1 = [[3,24,35,46,65,666],[100,200,322,43,53,6]]

#st.write(st.session_state)

co1,co2,co3 = st.columns(3)

with co1.expander("クリックして展開"):
    st.write("非表示のコンテンツ")
  
co2.line_chart(data_1)

with co3.container():
  st.write("外側のコンテンツ")
  st.metric("メタリック",value=123)
  with st.container():
    st.write("内側のコンテンツ")

col1,col2 = st.columns(2)
with col1:
    st.line_chart([0, 1, 2, 3, 4])
with col2:
    st.line_chart([4, 3, 2, 1, 0])

# widthとheightの引数を使用した例
column1,column2 = st.columns(2)
with column1:
    st.bar_chart([0, 1, 2, 3, 4],width=400,height=200)
with column2:
    st.line_chart([4, 3, 2, 1, 0],width=400,height=200)
#st.form_submit_button("クリック")
#st.experimental_rerun("クリック")
