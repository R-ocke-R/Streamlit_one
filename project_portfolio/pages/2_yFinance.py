import yfinance as yf
import streamlit as st
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp_list = pd.read_html(url) 
# this brings back all the tables on the page and convert them to pandas dataframe.
sp_list_500 = sp_list[0]

ticker_list = list(sp_list_500['Symbol'].values)
name_list = list(sp_list_500['Security'].values)
st.write("Choose one of the SP500 company")

choice = st.selectbox("here", options = name_list)
selected_index = name_list.index(choice)
corresponding_ticker = ticker_list[selected_index]


tickerData = yf.Ticker(corresponding_ticker)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-5-31', end='2024-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
