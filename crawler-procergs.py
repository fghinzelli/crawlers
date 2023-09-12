import smtplib
import datetime
import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url_base = os.getenv('PRC_URL_BASE')
file_name = os.getenv('PRC_FILE_NAME')
email_origin = os.getenv('PRC_EMAIL_ORIGIN')
smtp_server = os.getenv('PRC_SMTP_SERVER')
destination_list = os.getenv('PRC_DESTINATION_LIST')

def send_mail(email_destination):
    message = "Alterações identificadas na página " + url_base
    msg = MIMEMultipart()
    msg['From'] = email_origin
    msg['To'] = email_destination
    msg['Subject'] = "Novas atualizações PROCERGS | " + str(datetime.date.today())
    
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

response = urlopen(url).read()
soup = BS(response, features="lxml")

resultList = soup.find_all('div', {'class': 'artigo__texto'})
with open(file_name, "r") as outputFile:
    fileContent = outputFile.read()
    outputFile.close()

if fileContent != str(resultList[0]):
    print(datetime.date.today().strftime('%d-%m-%Y %H:%M:%S ') + 'Novas alterações encontradas')
    with open(file_name, 'w') as outputFile:
        outputFile.write(str(resultList[0]))
        outputFile.close()
    for email in destination_list.split(';'):
        send_mail(email)