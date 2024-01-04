from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


st.title("💬 Chatbot Chatbot GPTalkmate3.5-FT")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["systemprompt"] = [{"role": "system", "content": "GPTalkmateは、ユーザーの言語レベルに応じて返答のレベルを自動的に調整する適応型の会話型AIです。ユーザーの会話内容の深さや言葉の難易度、文法の難易度、そしてその話題に対する理解度を判断し、ユーザーと同じレベルの言葉を使って返答します。"}]
    st.session_state["messages"] = [{"role": "assistant", "content": "日本語の練習をしましょう！今日何について話そうか考えてみましょう…旅行の話題について話しましょう！どうですか？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI()
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=openai_api_key, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)



