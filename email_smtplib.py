import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# library for emails.
# smtp protocol

server = smtplib.SMTP("smtp.gmail.com",25) # the server, host and port as args.
server.ehlo()

server.login("tonynotstark98@gmail.com","Network1998")

msg.MIMEMultipart()
msg["From"] = "Tony Stark"
msg["To"] = "hermanstaro8@gmail.com"
msg["Subject"] = "First try"

with open("msg.txt","r") as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

text = msg.as_string()
server.sendmail("tonynotstark98@gmail.com","hermanstaro8@gmail.com",text)




