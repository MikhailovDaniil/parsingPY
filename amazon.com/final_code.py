from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from tqdm import tqdm
import pandas as pd

data = []

s = Service("./chromedriver")
browser = Chrome(service = s)
url = "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172541&s=featured-rank&qid=1644647363&rnid=386442011&ref=sr_st_featured-rank"
browser.get(url)

sleep(3)

soup = BeautifulSoup(browser.page_source, "lxml")

for i in tqdm(range(1,16)):
    sleep(4)
    cards = soup.findAll("div", class_ = "s-card-container s-overflow-hidden aok-relative s-expand-height s-include-content-margin s-latency-cf-section s-card-border")
    for card in cards:
        try:
            link = "https://www.amazon.com"+card.find("div", class_ = "a-section").find("a").get('href')
        except:
            link = ""
        try:
            name = card.find("div", class_ = "a-section").find("h2").find("span").text.strip()
        except:
            name =""
        try:
            price = card.findAll("span", class_ = "a-offscreen")[0].text
        except:
            price = "-"
        try:
            noDiscountPrice = card.findAll("span", class_ = "a-offscreen")[1].text
        except:
            noDiscountPrice = price
        try:
            Avg_review_outof5 = card.find("span", class_ = "a-icon-alt").text.split(" ")[0]
        except:
            Avg_review_outof5 = ""
        try:
            Reviews_amount = card.find("span", class_ = "a-size-base s-underline-text").text
        except:
            Reviews_amount = ""
        
        data.append([name, price, noDiscountPrice, Avg_review_outof5, Reviews_amount, link])
    
    try:
        browser.find_element(By.CLASS_NAME, "s-pagination-next").click()
    except:
        break

headers = ["name", "price", "noDiscountPrice", "Avg_review_outof5", "Reviews_amount", "link"]
df = pd.DataFrame(data, columns = headers)
df.to_csv("./amazon.csv", sep = ";", encoding = "utf8")