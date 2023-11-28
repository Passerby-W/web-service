import streamlit as st
from utils import chat

st.title("ChatBot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

model = st.sidebar.radio("选择模型", ["4", "3.5"])
if model == "3.5":
    model = "gpt-3.5-turbo-1106"
else:
    model = "gpt-4-1106-preview"
history = st.sidebar.radio("是否保留历史", ["True", "False"])
if "character" not in st.session_state:
    st.session_state["character"] = "正常"
st.session_state["character"] = st.sidebar.selectbox("请选择回答风格", ("正常", "杠精", "暴躁", "油滑"))
memory = st.sidebar.slider('保存对话的轮数', 1.0, 20.0, 5.0, step=1.0)

with st.container():
    if history == "False":
        st.session_state["messages"] = []
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        elif message["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(message["content"])
    prompt = st.chat_input("Type something...")
    if prompt:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        if st.session_state["character"] == "正常":
            character_message = []
        elif st.session_state["character"] == "杠精":
            character_message = [{"role": "system", "content": "现在你是一个聪明且角度刁钻的杠精，强词夺理，颠倒黑白的反驳一切用户输入的观点。"}]
        elif st.session_state["character"] == "暴躁":
            character_message = [{"role": "system", "content": "现在你是一个暴躁爱说脏话的黑社会，你喜欢用脏话怼对方。"}]
        elif st.session_state["character"] == "油滑":
            character_message = [{"role": "system", "content": "现在你用圆滑幽默高情商的语气和用户对话。"}]
        assistant_message = chat(model=model, messages=character_message + st.session_state["messages"][-int(memory):])
        st.session_state["messages"].append(assistant_message)
        with st.chat_message("assistant"):
            st.markdown(assistant_message["content"])
