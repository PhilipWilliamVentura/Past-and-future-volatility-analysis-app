# Past-and-future-volatility-analysis-app
This code combines an interactive 3d implied volatility surface with a historical volatility representation using Bollinger Bands to evaluate the overall volatility of a certain asset.< br / >

Dependencies<br/>

Python<br/>
Version: Python 3.7 or higher.< br / >

Libraries
```
pip install numpy pandas yfinance plotly scipy streamlit
```

NumPy: For numerical operations, including creating grids.< br / >
Pandas: To handle stock and option data.< br / >
yfinance: To fetch stock data from Yahoo Finance.< br / >
Plotly: To create interactive 3D plots.< br / >
SciPy: To use the griddata function for interpolation.< br / >
Streamlit: To build the interactive web application.< br / >

To run the application (Streamlit framework)< br / >
After installing the dependencies, you can run the Streamlit app with the following command:
```
streamlit run main.py
```
