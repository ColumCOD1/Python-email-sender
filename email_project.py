from email.message import EmailMessage 
import ssl
import smtplib

email_sender = 'alexander.rinzler@gmail.com'
email_password = 'cxumcsfkxlfnwepg'

email_reciever = 'fomav30750@cebaike.com'

subject = "Stop & Think"
body = "This is something meant to be philisophical but I forgot what to say."

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())