from numpy.random import f
import streamlit as st
import time
from main import run_analysis
import pandas as pd
import logging

st.title("Autonomous Stock Research Agent")
ticker = st.text_input("Enter NSE Ticker")
if st.button ("Analyze"):
    try:
        if ticker == "" :
            st.error("Please enter NSE ticker", icon="🚨", width="stretch", title=None)
        else:
            try:
                st.write(f"selected: {ticker}.NS")
                with st.spinner(text="Wait while we display the result", show_time=True, width="content"):
                    ##df = pd.DataFrame(run_analysis(f"{ticker}.NS"), index = [0])
                    ##st.write(df)
                    results =   run_analysis(f"{ticker}.NS")
                    ##st.write(results)
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Ticker", ticker)
                    with col2:
                        st.metric("Highest Close", round(results["highest_close"],2))
                    with col3:
                        st.metric("Lowest Close", round(results["lowest_close"],2))
                    with col4:
                        st.metric("Average Volume", round(results["average_volume"],2))
                    st.success("Done!")
            except Exception as e:
                logging.error(f"Error downloading data: {e}")
    except Exception as e:
       logging.error(f"Input is blank: {e}") 
