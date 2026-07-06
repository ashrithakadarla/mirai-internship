import streamlit as st

st.set_page_config(page_title="Calculator")

st.title("Calculator")

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "result" not in st.session_state:
    st.session_state.result = ""

def append(value):
    st.session_state.expression += value

def clear():
    st.session_state.expression = ""
    st.session_state.result = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    try:
        st.session_state.result = str(eval(st.session_state.expression))
    except:
        st.session_state.result = "Error"

with st.form("calc_form"):
    expression = st.text_input(
        "Enter Expression",
        value=st.session_state.expression,
        placeholder="Enter your expression"
    )

    submitted = st.form_submit_button("Calculate")

    st.session_state.expression = expression

    if submitted:
        calculate()

st.markdown("### Result")

if st.session_state.result != "":
    st.success(st.session_state.result)

st.divider()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]

for row in buttons:
    cols = st.columns(4)
    for col, button in zip(cols, row):
        with col:
            if st.button(button, use_container_width=True):
                append(button)
                st.rerun()

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("C", use_container_width=True):
        clear()
        st.rerun()

with c2:
    if st.button("⌫", use_container_width=True):
        backspace()
        st.rerun()

with c3:
    if st.button("=", use_container_width=True):
        calculate()
        st.rerun()