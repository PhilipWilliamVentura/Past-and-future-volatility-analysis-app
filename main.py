import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from scipy.interpolate import griddata
import datetime
import plotly.express as px

st.set_page_config(layout='wide')

# Function to fetch option data
def fetch_option_data(ticker):
    stock = yf.Ticker(ticker)
    options = stock.options
    data = []
    
    # Loop through all available expirations and collect data
    for expiration in options:
        opt_data = stock.option_chain(expiration)
        calls = opt_data.calls
        puts = opt_data.puts

        # Select relevant columns
        for call in calls.itertuples():
            data.append([call.strike, expiration, call.impliedVolatility, 'call'])
        for put in puts.itertuples():
            data.append([put.strike, expiration, put.impliedVolatility, 'put'])
    
    return pd.DataFrame(data, columns=["Strike", "Expiration", "ImpliedVolatility", "OptionType"])

# Function to calculate moneyness (Stock price / Strike price)
def calculate_moneyness(stock_price, strike_price):
    return stock_price / strike_price

def implied_volatility():
    st.title("Interactive 3D Implied Volatility Surface")

    ticker = st.text_input("Enter Stock Ticker Symbol:", "AAPL")
    
    # Fetch data for the stock ticker
    if ticker:
        # Fetch the stock data from Yahoo Finance
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period="1d")
            
        # Check if stock data is fetched
        if stock_data.empty:
            st.error(f"No data found for {ticker}. Please check the ticker symbol.")
            return
            
        stock_price = stock_data["Close"].iloc[-1]
        st.write(f"Stock Price: ${stock_price:.2f}")
            
        # Get option data (Implied Volatility, Strike Price, Expiration)
        option_data = fetch_option_data(ticker)
        option_data['Moneyness'] = option_data['Strike'].apply(lambda x: calculate_moneyness(stock_price, x))
            
        # Filter out rows with missing implied volatility
        option_data = option_data.dropna(subset=['ImpliedVolatility'])
            
        # Get 3D data (Moneyness, Expiration, ImpliedVolatility)
        moneyness = option_data['Moneyness'].values
        expiration = pd.to_datetime(option_data['Expiration']).apply(lambda x: (x - pd.to_datetime('today')).days).values
        implied_volatility = option_data['ImpliedVolatility'].values

        # Create a grid for interpolation
        grid_moneyness, grid_expiration = np.mgrid[min(moneyness):max(moneyness):100j, min(expiration):max(expiration):100j]
            
        # Interpolate implied volatility on the grid
        grid_iv = griddata((moneyness, expiration), implied_volatility, (grid_moneyness, grid_expiration), method='linear')

        # Create the 3D plot with plotly
        fig = go.Figure(data=[go.Surface(
            z=grid_iv,
            x=grid_moneyness,
            y=grid_expiration,
            colorscale='Viridis',
            colorbar=dict(title='Implied Volatility'),
            hovertemplate="Moneyness: %{x}<br>Time to Expiration: %{y} days<br>Implied Volatility: %{z}<extra></extra>"
        )])

        fig.update_layout(
            title=f'Implied Volatility Surface for {ticker}',
            scene=dict(
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),  
                zaxis=dict(showgrid=False, zeroline=False, showticklabels=False),  
            ),
            autosize=True,
            height=800, 
            width=1200,  
        )

        st.plotly_chart(fig)

def historical_volatility():
    st.title("Historical volatility determined by Bollinger bands")

    tickers = [st.text_input("Enter Stock Ticker Symbol:", "AAPL")]

    start_date = st.text_input("Enter start date as such \"YYYY-MM-DD\": ", "2023-01-01")
    end_date = datetime.date.today().strftime('%Y-%m-%d')

    #Stock Dataframe
    each_df = {}
    for ticker in tickers:
        each_df[ticker] = yf.download(ticker, start=start_date, end=end_date)

    stocks = pd.concat(each_df, axis=1, keys=tickers)
    stocks.columns.names = ["Ticker Symbol", "Stock Info"]

    
    closing_prices = each_df[ticker]["Adj Close"]

    if stocks.empty:
        st.error('No data for this ticker. Please input another ticker')

    #Bollinger Bands
    std = closing_prices.rolling(window=20).std()
    sma_20 = closing_prices.rolling(window=20).mean()
    upper_band = sma_20 + 2*std
    lower_band = sma_20 - 2*std
    Bollinger_graph = go.Figure()
    Bollinger_graph.add_trace(go.Scatter(x=closing_prices.index, y=closing_prices, mode="lines", name="Closing Prices"))
    Bollinger_graph.add_trace(go.Scatter(x=closing_prices.index, y=upper_band, mode="lines", name="Upper Bollinger Band"))
    Bollinger_graph.add_trace(go.Scatter(x=closing_prices.index, y=lower_band, mode="lines", name="Lower Bollinger Band"))
    Bollinger_graph.add_trace(go.Scatter(x=closing_prices.index, y=sma_20, mode="lines", name="SMA(20)"))
    Bollinger_graph.update_layout(xaxis_title="Date", yaxis_title="Price", hovermode="x")

    #Distance between Bollinger Bands
    distance_bands = upper_band - lower_band

    #Final graph
    final = go.Figure(data=[go.Candlestick(x=each_df[ticker].index, open=each_df[ticker]["Open"], close=each_df[ticker]["Close"], high=each_df[ticker]["High"], low=each_df[ticker]["Low"])])
    final.add_trace(go.Scatter(x=closing_prices.index, y=upper_band, mode="lines", name="Upper Bollinger Band", marker = {"color" : "violet"}))
    final.add_trace(go.Scatter(x=closing_prices.index, y=lower_band, mode="lines", fill="tonexty", name="Lower Bollinger Band", marker = {"color" : "violet"}))
    final.add_trace(go.Scatter(x=closing_prices.index, y=sma_20, mode="lines", name="SMA(20)", marker = {"color" : "yellow"}))
    final.add_trace(go.Scatter(x=closing_prices.index, y=distance_bands, mode="lines", name="Volatility (Bollinger Band Distance)", marker = {"color" : "lightgrey"}))
    final.update_layout(title= f'Technical analysis of {ticker}', xaxis_title="Date", yaxis_title="Price", hovermode="x", plot_bgcolor = "black", height = 800, width = 1200)

    st.plotly_chart(final, use_container_width=True, height = 800)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Implied Volatility", "Historical Volatility"])

    if page == "Implied Volatility":
        implied_volatility()
    elif page == "Historical Volatility":
        historical_volatility()

if __name__ == "__main__":
    main()
