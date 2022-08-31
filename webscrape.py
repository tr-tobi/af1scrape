from bs4 import BeautifulSoup
import smtplib
import time

# declaring URL
url = "https://www.nike.com/gb/t/air-force-1-07-shoes-DMJP7P/CW2288-111"

# declaring header
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # getting the current price of white af1's
    price = soup.find("div", {"class": "product-price css-11s12ax is--current-price css-tpaepq"}).text
    # removing "£" sign
    real_price = float(price[1:])
    
    # checking if price of product has decreased
    if real_price < 109.95:
        # function notifying user
        send_email()


def send_email():
    # setting up the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # logging in
    server.login('tobithomas99@gmail.com', 'ptnpjylhubojsfxb')
    # declaring the subject, body and message
    subject = "Price decrease!"
    body = "Click the link: https://www.nike.com/gb/t/air-force-1-07-shoes-DMJP7P/CW2288-111"
    msg = f"Subject: {subject}\n\n{body}"
    # sending the email
    server.sendmail(
        'tobithomas99@gmail.com',
        'trixtertobi@gmail.com',
        msg
    )
    # stopping the server
    server.quit()

# checking price every 10 minutes
while True:
    check_price()
    time.sleep(600)