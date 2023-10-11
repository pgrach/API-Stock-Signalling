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

email_pass = os.getenv('EMAIL_PASS')
if email_pass is None:
    print("EMAIL_PASS environment variable not found")

# Initialize currency converter
currency_converter = CurrencyRates()

# Define the stocks to monitor and the email details
stocks_to_monitor = ["AAPL", "MSFT", "GOOGL", "TSLA", "NKE"]
email_user = 'gpu2003@gmail.com'
email_pass = os.environ['EMAIL_PASS']

def send_notification(ticker, price_usd, price_gbp):
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        subject = f'Current Market Price for {ticker}'
        body = f'The price of {ticker} is currently {price_usd} USD ({price_gbp} GBP).'
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(email_user, 'gpu2003@gmail.com', msg)
        print('Email sent successfully')

def check_stock_prices():
    for ticker in stocks_to_monitor:
        stock = yf.Ticker(ticker)
        current_price_usd = stock.info['currentPrice']
        
        # Convert the price from USD to GBP
        current_price_gbp = currency_converter.convert('USD', 'GBP', current_price_usd)
        
        # Send an email notification with the current price
        send_notification(ticker, current_price_usd, current_price_gbp)

# Call the function to check the stock prices and send an email notification
check_stock_prices()