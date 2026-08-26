import streamlit as st
import pandas as pd
import numpy as np

st.title("SPORTS ANALYTICS")

with st.sidebar:
    st.header("DASHBORD CONTROLS")
    player=st.selectbox("SELECT PLAYER",["Virat Kohli","MS Dhoni"])
    match_phase=st.slider("Overs Played",1,5,10)

st.subheader(f"LIVE STATS: {player}")

col1,col2=st.columns(2)
with col1:
    runs=match_phase*7
    st.metric("TOTAL RUNS",value=runs,delta="+7",delta_color="normal")
with col2:
    strike_rate=130+(match_phase*2)
    st.metric(label="STR",value=strike_rate,delta="2",delta_color="inverse")

st.divider()
st.subheader("RUN RATE")

char_data=pd.DataFrame(np.random.randn(match_phase,1)*3+8,columns=["RUN per Over"])

st.line_chart(char_data)