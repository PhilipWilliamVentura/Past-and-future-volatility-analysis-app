# Past-and-future-volatility-analysis-app
This code combines an interactive 3d implied volatility surface with a historical volatility representation using Bollinger Bands to evaluate the overall volatility of a certain asset.

Dependencies

Python
Version: Python 3.7 or higher.

Libraries
pip install numpy pandas yfinance plotly scipy streamlit

NumPy: For numerical operations, including creating grids.
Pandas: To handle stock and option data.
yfinance: To fetch stock data from Yahoo Finance.
Plotly: To create interactive 3D plots.
SciPy: To use the griddata function for interpolation.
Streamlit: To build the interactive web application.

To run the application (Streamlit framework)
After installing the dependencies, you can run the Streamlit app with the following command:
streamlit run main.py
