# sobh zrdt tqhg iuxn
import requests
from bs4 import BeautifulSoup
from six import print_
import smtplib

re =requests.get("https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html")
res = re.content

soup=BeautifulSoup(res,'html.parser')
price =float(soup.find('p' ,class_='price_color').text[1:])
print(price)

if price <60:
    smt = smtplib.SMTP('smtp.gmail.com' , 587)
    smt.ehlo()
    smt.starttls()
    smt.login('sharifalam206@gmail.com' , 'sobh zrdt tqhg iuxn')
    smt.sendmail('sharifalam206@gmail.com',
                 'sharifalam9667@gmail.com',
                 f"Subject:Earbuds Price Notifier\n\nBabuoo paisa km ho gaeal ba\n jan tare ketna {price}. kharid le")
    smt.quit()










