import openai
import streamlit as st



st.title("💬 Chatbot GPT3.5")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "日本語の練習をしましょう！今日何について話そうか考えてみましょう…旅行の話題について話しましょう！どうですか？"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():


    client = OpenAI(api_key="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")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
