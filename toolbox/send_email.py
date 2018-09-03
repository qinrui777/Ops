#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "qinrui.cool@gmail.com"
toaddr = "qinrui0929@foxmail.com,3051173318@qq.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "subject for you"

body = "dear, all ....."

msg.attach(MIMEText(body,'plain'))

filename = "ADCC_script_20180706.xlsx"
attachment = open("/Users/ruqin/Desktop/ADCC_script_20180706.xlsx","rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("qinrui.cool@gmail.com","Persist@1993")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()