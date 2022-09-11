from email.message import EmailMessage
# from app2 import password
import ssl
import smtplib

send_ema = 'stevkamwa@gmail.com'
sendpass ='your account app password'

reciever = 'jofid51158@esmoud.com'
subject = "Hello boss"
body=""" 
hjhjkljhkjhkj

"""
emai =EmailMessage()
emai['From'] = send_ema
emai['To'] = reciever
emai['subject'] = subject
emai.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
  smtp.login(send_ema,sendpass)
  smtp.sendmail(send_ema, reciever, emai.as_string())
