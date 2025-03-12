import streamlit as st
from agent import chatbot_agent

st.title("Chatbot GPT")


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
        state = chatbot_agent.invoke(
            {
                "messages": [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            }
        )
        response = state["messages"][-1].content
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
