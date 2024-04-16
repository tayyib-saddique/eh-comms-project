import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
print(current)
parent = os.path.dirname(current)
parent_ = os.path.dirname(parent)
parent__ = os.path.dirname(parent_)
sys.path.append(parent__)

import streamlit as st
import datetime
from llm.generate_questions import *
from llm.summarise import description

st.set_page_config(page_title="Summarise News")

side_bar_title = st.sidebar.title('News Filters')
subject = st.sidebar.selectbox('Subject',['Police & Crime','Sports','Education'])
today = datetime.datetime.now()
last_year = today.year - 1
jan_1 = datetime.date(last_year, 1, 1)
dec_31 = datetime.date(last_year, 12, 31)

d1 = st.sidebar.date_input(
    "Select date range for news summary",
    (jan_1, datetime.date(last_year, 1, 7)),
    jan_1,
    today
    
)

region = st.sidebar.selectbox('Region',['North East', 'North West', 'Yorkshire and The Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'])
news_source = st.sidebar.selectbox('News Sources',['Any', 'Chronicle Live','The Northern Echo','BBC'])

st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Generate questions")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"{generate_questions(prompt, subject, region, news_source, description)}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})