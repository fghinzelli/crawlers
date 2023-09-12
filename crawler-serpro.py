import smtplib
import datetime
import json
import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url_base = os.getenv('SERPRO_URL_BASE')
url_json = os.getenv('SERPRO_URL_JSON')
file_name = os.getenv('SERPRO_FILE_NAME')
email_origin = os.getenv('SERPRO_EMAIL_ORIGIN')
smtp_server = os.getenv('SERPRO_SMTP_SERVER')
destination_list = os.getenv('SERPRO_DESTINATION_LIST')

def send_mail(email_destino):
    message = "Alterações identificadas na página " + url_base
    msg = MIMEMultipart()
    msg['From'] = email_origin
    msg['To'] = email_destino
    msg['Subject'] = "Novas atualizações SERPRO | " + str(datetime.date.today())
    
    # add in the message body 
    msg.attach(MIMEText(message, 'plain'))
    
    #create server 
    server = smtplib.SMTP(smtp_server)
    
    server.starttls()   
    
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print("successfully sent email to %s" % (msg['To']))

url = Request(url_base, headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url_json).read()
response_json = json.loads(response)

with open(file_name, "r") as outputFile:
    fileContent = outputFile.read()
    outputFile.close()

if fileContent != json.dumps(response_json):
    print(datetime.date.today().strftime('%d-%m-%Y %H:%M:%S ') + 'Novas alterações encontradas')
    with open(file_name, 'w') as outputFile:
        outputFile.write(json.dumps(response_json))
        outputFile.close()
    for email in destination_list.split(';'):
        send_mail(email)