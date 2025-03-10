import os
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from operator import itemgetter

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(name="gpt-4o-mini", api_key=api_key)

def chatbot(state: MessagesState):
    ai_answer = llm.invoke(state["messages"])
    return {"messages": [ai_answer]}

builder = StateGraph(MessagesState)

builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

chatbot_agent = builder.compile()