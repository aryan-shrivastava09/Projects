import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib

my_email = "aryansri009@gmail.com"
my_password = "Prioryofsion09"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
}

url_item1 = "https://www.amazon.in/realme-Buds-Wireless-Earbuds-Black/dp/B08BPHPNCT/ref=sr_1_1?dchild=1&keywords=realme+q+buds&qid=1616574314&sr=8-1"
response = requests.get(url= url_item1, headers = headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")
pricestring = (soup.find("span", id = "priceblock_ourprice").getText()).split("\xa0")[1]

def priceformatter(p):
    price = ""
    for i in range(0,len(p)):
        if p[i] == ",":
            continue
        else:
            price += p[i]
    return float(price)

price1 = priceformatter(pricestring)

url_item2 = "https://www.flipkart.com/realme-buds-q-bluetooth-headset/p/itm2a9c125711e36?gclid=CjwKCAjwxuuCBhATEiwAIIIz0evRBh-aQFaG4rZauQoMyEDK0e7RruyJQFSH73s8b6sobJo3d6ZzJhoCJ4oQAvD_BwE&pid=ACCFVWN4PGNTEFGY&lid=LSTACCFVWN4PGNTEFGYNDRHV5&marketplace=FLIPKART&cmpid=content_headphone_840394530_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,472199938969,,,,c,,,,,,,&ef_id=CjwKCAjwxuuCBhATEiwAIIIz0evRBh-aQFaG4rZauQoMyEDK0e7RruyJQFSH73s8b6sobJo3d6ZzJhoCJ4oQAvD_BwE:G:s&s_kwcid=AL!739!3!472199938969!!!g!1039855654517!&gclsrc=aw.ds"
response = requests.get(url = url_item2, headers = headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
pricestring2 = soup.find("div", class_ = "_30jeq3 _16Jk6d").getText()
price2 = priceformatter(pricestring2[1:])

if price1<1500.0 or price2<1500.0:
    if price1<1500.0:
        p = price1
        u = url_item1
        website = "Amazon"
    elif price2<1500.0:
        p = price2
        u = url_item2
        website = "Flipkart"
    connection = smtplib.SMTP("smtp.gmail.com", port= 587)
    connection.starttls()
    connection.login(user= my_email, password= my_password)
    connection.sendmail(from_addr= my_email, to_addrs= "aryan.shrivastava9@gmail.com", msg= f"Subeject:Price Drop Aryan!\n\nBuy {u} from {website} at {p}")
    connection.close()
