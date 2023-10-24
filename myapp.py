# yfinance is yahoo yfinance
# for ticker symbols refer to : https://finance.yahoo.com/lookup/

import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price Analysis App")
st.write("""
This app retrieves the stock prices and volume of a selected company.
""")

tickerSymbol = st.text_input("Enter Ticker Symbol:", 'GOOGL')

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-5-25')

st.subheader(f"Stock Price Chart for {tickerSymbol}")
st.line_chart(tickerDf.Close)

st.subheader(f"Volume Chart for {tickerSymbol}")
st.line_chart(tickerDf.Volume)


st.subheader("Historical Data Table")
st.write(tickerDf)
