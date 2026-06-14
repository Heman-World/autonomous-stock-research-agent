from numpy.random import f
import streamlit as st
import time
from main import run_analysis
import pandas as pd
import logging

def format_market_cap(value):
    if value is None:
        return "N/A"
    if value >= 1_000_000_000_000:
        return f"₹ {value/1_000_000_000_000:.2f} T"
    if value >= 1_000_000_000:
        return f"₹ {value/1_000_000_000:.2f} B"
    return f"₹ {value:,.0f}"

st.title("Autonomous Stock Research Agent")
ticker = st.text_input("Enter NSE Ticker")
if st.button ("Analyze"):
    try:
        if not ticker.strip():
            st.error("Please enter NSE ticker", icon="🚨", width="stretch", title=None)
        else:
            try:
                st.caption(f"Selected Stock: {ticker.upper()}.NS")
                with st.spinner(text="Wait while we display the result", show_time=True, width="content"):
                    results =   run_analysis(f"{ticker}.NS")
                if results is None:         
                    st.error("Invalid ticker or delisted ticker", icon="🚨", width="stretch", title=None)
                    st.stop()
                else:
                    st.subheader(f"Stock Research Report: {ticker.upper()}")
                    st.markdown("-------")
                    st.write(f"**Ticker:** {ticker.upper()}")
                    st.write(f"**Sector:** {results['sector']}")
                    st.write(f"**Industry:** {results['industry']}")

                    tab1 , tab2 = st.tabs(["Technical Analysis","Fundamental Analysis"])
                    with tab1:      
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Highest Close", round(results["highest_close"],2))                    
                        with col2:
                            st.metric("Lowest Close", round(results["lowest_close"],2))
                        with col3:
                            st.metric("Average Volume", f"{results["average_volume"]:,.0f}")
                    with tab2:
                        col1, col2, col3= st.columns(3)

                        with col1:
                            st.metric("PE_Ratio", round(results["pe_ratio"],2))
                        with col2:
                            st.metric("Dividend Yield", round(results["dividend_yield"],2))
                        with col3:
                            st.metric("Market Cap", format_market_cap(results["market_cap"]))
                    st.success("Done!")
            except Exception as e:
                logging.error(f"Error downloading data: {e}")
    except Exception as e:
       logging.error(f"Input is blank: {e}") 
