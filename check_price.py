#!/usr/bin/env python

from googlefinance import getQuotes
import sys

import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = 'ylm.neu@gmail.com'
gmail_pwd = 'r9bbtzhy'

def mail(to, subject, text, attach=None):
    global gmail_user, gmail_pwd
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    if attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()

#-----------------------------------------
# stock price
#-----------------------------------------
target_list = ['AMD', 'QCOM', 'NVDA']

# basic info
buy_price_dd = {}
buy_volume_dd = {}

buy_price_dd['AMD'] = 13.105
buy_volume_dd['AMD'] = 200

buy_price_dd['QCOM'] = 61.8246
buy_volume_dd['QCOM'] = 500

buy_price_dd['NVDA'] = 100.8448
buy_volume_dd['NVDA'] = 200


for stock_name in target_list:
    result = getQuotes(stock_name)
    current_time = result[0]['LastTradeDateTimeLong']
    current_price = float(result[0]['LastTradePrice'])
    
    my_price = buy_price_dd[stock_name]
    my_volume = buy_volume_dd[stock_name]
    
    gainSell_price = my_price * 1.13 # increase 13%
    loseSell_price = my_price * 0.90 # drop 10%
    
    if current_price >= gainSell_price or current_price <= loseSell_price:
        send_msg = stock_name + ' : \n\tCost: ' + str(my_price) 
        send_msg += ', \n\tCurrent: ' + str(current_price) + '\n\t'
        send_msg += str(current_time)
        try:
            mail("leimingyu830@gmail.com", "stock_warn", send_msg)
        except:
            sys.stderr.write('Something went wrong...')
