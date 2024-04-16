import streamlit as st
import datetime



st.title('PM Brief')
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["News Summary", "Potential Questions"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
# Just add it after st.sidebar:
a = st.sidebar.title('News Filters')
b = st.sidebar.selectbox('Subject',['General','Policing','Sports','Education'])
#c = st.sidebar.date_input('Select Date')
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

d = st.sidebar.selectbox('Region',['North East', 'North West', 'Yorkshire and The Humber', 'East Midlands', 'West Midlands', 'East of England', 'London', 'South East', 'South West'])
e = st.sidebar.selectbox('News Sources',['Chronicle Live','The Northern Echo','BBC'])
f = st.sidebar.button('Submit')