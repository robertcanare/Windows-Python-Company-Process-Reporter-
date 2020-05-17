# Check Work Time Process on office PC
# January 27, 2020
# By Robert John Canare

import os
import smtplib
import getpass
import socket
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Email sender
email = 'email@gmail.com'
password = 'password'

# Email receiver
to_email = "email@gmail.com"
to_email_1 = "email@gmail.com"

# Get the timestamp
datetime.now(tz=None)
date = datetime.now()

# Get the process
process_name = 'wtc.exe'
call = str(os.popen(f"tasklist | findstr {process_name}").read())
count_line = call.count('\n')

# Sleep for a minute
time.sleep(120)


def send_email():
    mail_content = f'''
    As of {date} WTC Client Application is not running on user {getpass.getuser()} on computer {socket.gethostname()}.

    [THIS IS AN AUTOMATED MESSAGE - PLEASE DO NOT REPLY DIRECTLY TO THIS EMAIL]'''

    message = MIMEMultipart()
    message['From'] = email
    message['To'] = to_email
    message['Subject'] = f'Application Logs for the user {current_user}'
    message.attach(MIMEText(mail_content, 'plain'))

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)
    text = message.as_string()
    session.sendmail(email, to_email, text)
    session.sendmail(email, to_email_1, text)
    session.quit()


while count_line >= 1:
    print("running")
    break
else:
    print("Sending an Email...")
    send_email()
