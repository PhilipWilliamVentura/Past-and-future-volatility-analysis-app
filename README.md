# 📈 Past-and-Future Volatility Analysis App

🚀 **Interactive 3D Implied Volatility & Historical Volatility Analysis**

This application provides a powerful way to **visualize and analyze volatility** for a given asset. By combining an interactive **3D implied volatility surface** with **historical Bollinger Bands**, it offers deep insights into market behavior, helping traders and analysts make data-driven decisions.

## 🔥 Features
- 📊 **3D Implied Volatility Surface**: Visualize option volatility across different strike prices and expirations.
- 📉 **Historical Volatility with Bollinger Bands**: Assess past volatility trends.
- ⚡ **Real-Time Data Fetching**: Uses Yahoo Finance (`yfinance`) to get up-to-date market data.
- 🎨 **Interactive Plots**: Powered by Plotly for smooth visualization.
- 🌐 **User-Friendly Web App**: Built with Streamlit for easy interaction.

## 🛠️ Technologies & Dependencies
### ✅ **Python Version**: 3.7 or higher
Install all dependencies using:
```bash
pip install numpy pandas yfinance plotly scipy streamlit
```
- **NumPy**: Numerical operations, grid creation.
- **Pandas**: Handling stock and option data.
- **yfinance**: Fetching live stock data.
- **Plotly**: Creating interactive 3D visualizations.
- **SciPy**: Grid interpolation for smooth surfaces.
- **Streamlit**: Powering the web-based interface.

## 🚀 How to Run the Application
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/PhilipWilliamVentura/past-and-future-volatility-analysis.git
cd past-and-future-volatility-analysis
```
2️⃣ **Install Dependencies**
```bash
pip install numpy pandas yfinance plotly scipy streamlit
```
3️⃣ **Run the Streamlit App**
```bash
streamlit run main.py
```

## 📌 Example Output
🟢 **Implied Volatility Surface** (3D Plot):
- X-axis: Strike Prices
- Y-axis: Time to Expiration
- Z-axis: Implied Volatility

🔵 **Bollinger Bands Representation**:
- Historical volatility visualized over time.
- Detects periods of high or low market uncertainty.

## 🌟 Why This Project Stands Out
✅ **Bridges Historical & Future Volatility** – Offers a holistic view of market risk.
✅ **Highly Interactive & Data-Driven** – Provides deep insights using real-time market data.
✅ **Showcases Python & Finance Knowledge** – Ideal for machine learning, quant trading, and financial analytics.

