import streamlit as st
from PIL import Image
import time
import pandas as pd
import requests
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.title("ALGO May 8th tutorial")
st.write("hello world")

image = Image.open('cat.jpg')

st.image(image, caption='A cat')

with st.sidebar:
    ticker = st.text_input('ticker symbol','AAPL')

st.write('ticker symbol is', ticker)
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 5, 7, 23, 59).timetuple()))
interval = '1d' # 1d, 1m

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose'
df = pd.read_csv(query_string)
st.write(df)

#plotting with matplotlib
st.header("stock price plotted with matplotlib")
plt_fig,ax = plt.subplots()

ax.scatter(df['Date'].apply(lambda x: pd.Timestamp(x)),df['Close'])

st.pyplot(plt_fig)

#plotting with plotly:
st.header("stock price plotted with plotly")
fig = go.Figure(data =go.Scatter(x=df['Date'].apply(lambda x: pd.Timestamp(x)), y=df['Close'], mode='markers',name='Seller Exhaustion',marker = {'color':'green'}))
st.plotly_chart(fig)