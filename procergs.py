import smtplib
import datetime
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url_base = 'https://www.procergs.rs.gov.br/concurso-publico-2023'
file_name = ''

def send_mail():
    message = "Alterações identificadas na página " + url_base
    msg = MIMEMultipart()
    msg['From'] = ""
    msg['To'] = ""
    msg['Subject'] = "Novas atualizações | " + str(datetime.date.today())
    
    # add in the message body 
    msg.attach(MIMEText(message, 'plain'))
    
    #create server 
    server = smtplib.SMTP('')
    
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
    send_mail()