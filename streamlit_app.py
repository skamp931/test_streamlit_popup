import streamkit as st
import time

st.set_page_config(
  page_title = "streamlit page to uo popupwindows",
  layout = "wide",
  initial_sidebar_state = "expanded"
)

#init
def init():
  if "init" not in st.session_state:
    st.session_state.init= True
    reset_session()
    count()
    return True
  else:
    return False

def tab_session():
  if not st.session_state.now_tab == st,session_state.tab:
    reset_session()
  st.session_state.now_tab = st.session_state.tab

#expand
def ck():
  if "ck" not in st.session_state:
      st.session_state.ck = -1
  st.session_state.ck += 1
  return st.session_state.ck

def count():
  if "count" not in st.session_state:
    st.session_state.count = 0
  st.session_state.count += 1

#UI componets
def deco_horizontal(func):
  def wrapper(*args, **kwargs):
    st.write("---")
    func(*args, **kwargs)
    st.write("---")
  return wrapper

@deco_horizontal
def back_btn():
  st.button(f"back [{ck()}]",on_click=reset_session)

def btn(label="button", key=None,onclick=None,done=None):
  if st.button(label,key=key,on_click=onclick) and done:
    done()

def pop_btn(label="pop",key=None, layer=0, onclick=lambda:None, done=None, description=None):
    placeholder=st.empty()
    with placeholder.container():
        if description:
            st.write(description)
        res=st.button(label,key=key,on_click=lambda:[placeholder.empty(),layer_session(layer),onclick()])
    if res:
        if done:
            with placeholder:
                done()
                placeholder.empty()

def pop(msg, done=None, interval=1):
    with st.spinner(msg):
        time.sleep(interval)
    if done:
        done()

#contents
def index():
  st.write("this is **Index_page** !")

def sample_content(i):
  st.write(f"this is **page_{i} ** [{i}]")
  pop_btn(
    label = f"POP_botton",
    layer = 2,
    onclick=lambda:[count(),print(f"ck[{ck()}]")],
    done = lambda:[
      pop(f"pop_botton push now! [{ck()}]"),
      st.success(f"succes![{ck()}]"),
      time.sleep(1)
    ]
  )

# body
init()
st.session_state.ck=0

st.session_state.tab = st.sidebar.selectbox("選択してください。", ["Index","List"])
tab_session()# TAB切り替えの管理
# delay
time.sleep(0.1)
#
_tab=st.session_state.tab
_layer=st.session_state.layer
if _tab=="Index":
    if _layer==0 or _layer==1:
        layer_session(1)
        index()
elif _tab=="List":
    if _layer==0 or _layer==1:
        layer_session(1)
        sample_content(1)
    elif _layer==2:
        st.info(f"POPによるページ遷移をしました。[{ck()}]")
        sample_content(1)
        back_btn()

