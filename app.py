import requests
import streamlit as st

st.title("Chatbot GPT")

AGENT_URL = "https://agent-cloud-771619624508.us-central1.run.app/chatbot"

def call_agent(message):
    response = requests.post(url=AGENT_URL, json={"message": message}).json()
    return response["answer"]


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = call_agent(st.session_state.messages[-1]["content"])
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
