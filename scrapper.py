import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.com/Kindle-Now-with-Built-in-Front-Light/dp/B07978J597/ref=sr_1_1?dchild=1&keywords=amazon+kindle&qid=1593724648&sr=8-1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
def check_price():
    page = request.get(URL, header=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 70.00):
        send_mail()
    print(converted_price)
    print(title.strip)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('myfamurewa@gmail.com', 'wownownaojoqjqoqo232')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Kindle-Now-with-Built-in-Front-Light/dp/B07978J597/ref=sr_1_1?dchild=1&keywords=amazon+kindle&qid=1593724648&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'myfamurewa@gmail.com',
        'famurewm@gmail.com',
        msg
    )
    print('Hey the email has been sent')

    server.end()
while(True):
    check_price()
    time.sleep(3600 * 24)