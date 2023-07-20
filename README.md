# API-Stock-Signalling
###### NOTE: this is a project to practice your Python industry skills. Please upload your solutions by opening a new branch to the main. All files that are instantly merged to the main will be deleted. 
## Overview
A small consultancy who is currently delivering client work for a major bank wants to monitor the Tesla stock price. Once the stock falls below a certain price, they want to be immediately notified so that they can be purchase Tesla stock. 
## Goal
Write a real time Python application that monitors the price then notifies the user when the price falls below £194.50 GBP.
## Brief
To do this, the client has recommended using a popular automation website called IFTTT: https://ifttt.com/. They are willing to use a different provider or solution (use those consultancy skills!) if you believe there is a better option.
#### IFTTT Applet

IFTTT stands for “If This Then That” and it’s an automation platform that allows you to connect different apps and services together. An applet is a connection between two or more apps or devices that enables you to do something that those services couldn’t do on their own. Applets consists of two parts triggers and actions. Triggers tell an applet to start, and actions are the end result of an applet run. To use an applet, you’ll need to create a free IFTTT account and connect your apps and devices to IFTTT so that they can talk to each other.

#### Proposed Workflow
- Write a script that returns the Tesla stock price. This will involve making an API request.
- Set up a IFTTT account and applet. This will be accessible via the mobile app which allows you to trigger the webhook service provided by IFTTT.
- You will need to configure the 'webhooks' service to receive web requests. You can find more details here: https://ifttt.com/maker_webhooks. 
- Python application makes a HTTP request (https://cs.fyi/guide/http-in-depth) to 

## Main Considerations
- Choose an automation approach. Are you planning on using IFTTT or another approach?
- What API are you going to use?
