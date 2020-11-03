# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:49:18 2020

@author: vivek
"""

# sending email

'''
Provider - SMTP server domain name
Gmail (will need App Password) - smtp.gmail.com
Yahoo Mail - smtp.mail.yahoo.com
Outlook.com/Hotmail.com - smtp-mail.outlook.com
AT&T - smpt.mail.att.net (Use port 465)
Verizon - smtp.verizon.net (Use port 465)
Comcast - smtp.comcast.net
'''

# connect with smtp
import smtplib # simple mail transfer protocol library
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo() # ehlo() command which "greets" the server and establishes the connection
smtp_object.starttls() # When using the 587 port, this means you are using TLS encryption, which you need to initiate by running the starttls() command. If you are using port 465, this means you are using SSL and you can skip this step

# For hidden passwords
import getpass
result = getpass.getpass("Type something here and it will be hidden: ")
result

'''
Note for Gmail Users, you need to generate an app password instead of your normal email password. This also requires enabling 2-step authentication. Follow the instructions here to set-up 2-Step Factor Authentication as well as App Password Generation:https://support.google.com/accounts/answer/185833?hl=en/. Set-up 2 Factor Authentication, then create the App Password, choose Mail as the App and give it any name you want. This will output a 16 letter password for you. Pass in this password as your login password for the smtp.
'''

email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

# Now we can send an email using the .sendmail() method
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

'''
{}
If you get back an empty dictionary, then the sending was successful.
'''

smtp_object.quit() # You can then close your session with the .quit() method.


# Overview of Received Emails¶
# we will use the built-in imaplib library. We will also use the built in email library for parsing through the recieved emails
import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass
user = input("Enter your email: ")

# Remember , you may need an app password if you are a gmail user
password = getpass.getpass("Enter your password: ")

M.login(user,password)

M.list()
M.select("inbox") # Connect to your inbox
# Use if you get an error saying limit was reached
imaplib._MAXLINE = 10000000

typ ,data = M.search(None,'SUBJECT "this is a test email for python"') # search and confirm if a particular email is there
typ # 'OK'
data # [b'28298'] , The data is a list of unique ids.

result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# We can use the built in email library to help parse this raw string.
import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
# b'This is a test to see if the python search worked.\r\n'

