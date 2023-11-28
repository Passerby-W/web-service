import streamlit as st


st.set_page_config(
    page_title="Demo",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "本网页只为测试使用，内容均为AI生成，不代表开发者任何观点"
    }
)

st.title("🤠 Demo")


with st.container():
    st.divider()
    st.markdown("**本网页只为测试使用，内容均为AI生成，不代表开发者任何观点**")