from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    
st.title("💬 Chatbot GPTalkmate3.5-PR")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["systemprompt"] = [{"role": "system", "content": "Now, you're a Japanese conversation practice assistant. Please assess the user's language proficiency based on their vocabulary, grammar complexity, sentence length, and grammar errors. Respond at a level equivalent to the user's language proficiency. For instance, if the user's vocabulary and grammar are simple, adjust your response to match that simplicity; if they're more complex, respond accordingly. Additionally, in your replies, guide the user for the next part of the conversation by asking questions. Also, try to simulate everyday conversations—avoid overly lengthy sentences or excessive consecutive questioning."}]
    st.session_state["messages"] = [{"role": "system", "content": "Now, you're a Japanese conversation practice assistant. Please assess the user's language proficiency based on their vocabulary, grammar complexity, sentence length, and grammar errors. Respond at a level equivalent to the user's language proficiency. For instance, if the user's vocabulary and grammar are simple, adjust your response to match that simplicity; if they're more complex, respond accordingly. Additionally, in your replies, guide the user for the next part of the conversation by asking questions. Also, try to simulate everyday conversations—avoid overly lengthy sentences or excessive consecutive questioning."}, {"role": "assistant", "content": "日本語の練習をしましょう！今日何について話そうか考えてみましょう…旅行の話題について話しましょう！どうですか？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
        
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
