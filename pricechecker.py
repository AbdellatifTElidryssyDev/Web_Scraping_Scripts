import requests
from bs4 import BeautifulSoup
import smtplib

# ============= scraping e-comm product informaiton ===================

# variebles

url      = "https://www.amazon.com/Espresso-Machine-Cappuccino-Barista-Steamer/dp/B01LWUI6B8/ref=sr_1_2_sspa?dchild=1&hvadid=330070486472&hvdev=c&hvlocphy=1009974&hvnetw=g&hvpos=1t1&hvqmt=b&hvrand=13380686503794165896&hvtargid=kwd-295913715042&keywords=coffee+maker+and+espresso&qid=1619864144&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzU0lVQlI2V0hDNlVWJmVuY3J5cHRlZElkPUEwMDI0NjQ1MlNaU0ZYS1lXQUtLNyZlbmNyeXB0ZWRBZElkPUEwMDAyMzk0MkZRRFlKQ1FFWVFRNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers  = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
"}
price_value    = 219
email_adress   = "put_your_sender_email"
password       = "put_your_choice_password"
reciever_email = "put_your_reciever_email"


# fuction for track prices


def trackPrices():
    price = float(getPrice())
    if price > price_value:
        diff =int(price - price_value)
        print(f"still ${diff} too expensive")

    else:
        print("Cheaper! Notyfing...")
        sendEmail()


# fuction for get price

def getPrice():
    page  = requests.get(url, headers=headers)
    soup  = BeautifulSoup(page.content, 'html-parser')
    title = soup.find(id='productTitle').get_text().strip()    #strip method for delete blank space 
    price = soup.find(id='priceblock_ouprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price 


# function for send email

def sendEmail():
    subject  = "Amazone Price has Dropped!"
    mailtext = 'subject:'+subject+'\n\n'+url
    server   = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(email_adress,password)
    server.sendmail(email_adress, reciever_email, mailtext)



def __name__ == "__main__":
    trackPrices()


