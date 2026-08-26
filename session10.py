import streamlit as st
import pandas as pd
import time

st.subheader("API Latency")

if st.button("FETCH AI"):
    with st.spinner("ANALYZING..."):
        time.sleep(3)
    
    st.toast("ANALYSIS COMPLETED")
    st.write("FINAL ANSWER")

st.subheader("Using forms")

st.write("THE MAIN HEADER")
with st.expander("EXPANDED INFO"):
    st.write("System uptime: 99.9%")
    st.write("System uptime: 99.9%")
    st.write("System uptime: 99.9%")
    
    st.write("System uptime: 99.9%")

with st.form(key="form_1"):
    st.write("Configuring input")
    
    input_1=st.slider("Temperature",0.0,32.0,2.0)
    input_2=st.selectbox("Options",["Option 1","Option 2","Option 3"])
    
    submitted=st.form_submit_button("Submit form")

if(submitted):
    st.success("FORM SUBMITTED")

data=pd.DataFrame(
    {
        "TASK":["READ","CODE","PLAY"],
        "STATUS":["DONE","IN PROGRESS","PENDING"],
        "HOURS":[1,2,2]
    }
)

edited_df=st.data_editor(data,num_rows="fixed")
if st.button("SAVE THE CHANGES"):
    st.write("Modifications saved")
    st.dataframe(edited_df)