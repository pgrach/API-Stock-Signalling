following YAGNI guideline indtead of calling API 
we import yfinance library keeping the codebase simpler and more focused in the task.

using smtplib library allows to send email notifications directly 
from the Programme running lically. it is a straightforward solution to meet email notification needs. 
integrating IFTTT would involve setting up an applet to handle email notifications, setting up additional steps
to trigger the applet. Hence, smtplib could be seen as a more direct and controllable solution for this use case.
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

