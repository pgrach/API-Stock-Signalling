
# Why smtplib over IFTTT
Following YAGNI principle we believe the requirement of sending notification via email provides exactly what we need. For this task smtplib offers more direct and controllable solution, also it is free.

Considering further versions, IFTTT would be chosen for additional web notification solutions, such as Facebook, Telegram, SMS etc. 

# Why yfinance over API
yfinance library provides a simpler interface for fetching stock data compared to making HTTP requests to an API, parsing the responses, and handling errors. Given that we are planning to run the script every minute, this would total to a max of 1,440 requests per day (assuming one request per run). This falls well within the documented rate limits for the public API based on IP address (48,000 requests per day)

# Create & use app passwords

To help keep your account secure, use "Sign in with Google" to connect apps to your Google Account

1. Go to your Google Account.
2. Select Security.
3. Under "Signing in to Google," select 2-Step Verification.
4. At the bottom of the page, select App passwords.
5. Enter a name that helps you remember where you’ll use the app password.
6. Select Generate and follow the instructions on your screen. The app password is the 16-character code that generates on your device.

Paste it in .env file replacing here past your pass with whatever 16-character you got:
EMAIL_PASS=here past your pass

