import yfinance as yf
import smtplib
import schedule
import time
import os
from forex_python.converter import CurrencyRates
from dotenv import load_dotenv

# Load environment variables from .env file
success = load_dotenv('C:\\Users\\PavelGrachev\\OneDrive - JCW Resourcing\\Desktop\\github\\YagniStocks\\.env')
print(f'Success: {success}')

# Initialize currency converter
currency_converter = CurrencyRates()

# Define the stocks to monitor and the email details
stocks_to_monitor = ["AAPL", "MSFT", "GOOGL", "TSLA", "NKE"]
previous_prices = {ticker: 0 for ticker in stocks_to_monitor}
email_user = 'gpu2003@gmail.com'
email_pass = os.environ['EMAIL_PASS']
if email_pass is None:
    print("EMAIL_PASS environment variable not found")

def check_stock_prices():
    for ticker in stocks_to_monitor:
        stock = yf.Ticker(ticker)
        current_price_usd = stock.info['currentPrice']
        
        # Convert the price from USD to GBP
        current_price_gbp = currency_converter.convert('USD', 'GBP', current_price_usd)
        
        # Convert the previous price from USD to GBP
        previous_price_gbp = currency_converter.convert('USD', 'GBP', previous_prices[ticker])
        
        # Compare the current price with the previous price
        if previous_price_gbp - current_price_gbp >= 0.01:
            send_notification(ticker, current_price_gbp)
        previous_prices[ticker] = current_price_usd  # Store the price in USD for the next check

def send_notification(ticker, price):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        subject = f'Price Drop Alert for {ticker}'
        body = f'The price of {ticker} has dropped to {price} GBP.'
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(email_user, 'gpu2003@gmail.com', msg)

# Schedule the check_stock_prices function to run every minute
schedule.every(1).minutes.do(check_stock_prices)

while True:
    schedule.run_pending()
    time.sleep(1)