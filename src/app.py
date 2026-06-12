import streamlit as st

st.title("Autonomous Stock Research Agent")
ticker = st.text_input("Enter NSE Ticker")
if ticker:
    st.write(f"selected: {ticker}")

