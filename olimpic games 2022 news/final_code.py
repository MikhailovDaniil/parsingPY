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
url = "https://www.google.com/search?q=олимпиада&sxsrf=APq-WBvDA7edewa5jBhoh_R3-274Fe9vAQ:1644488930864&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjBk77U9vT1AhXksIsKHWOHAXUQ_AUoAXoECAIQAw"
browser.get(url)

for i in tqdm(range(1, 11)):
    sleep(5)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    cards = soup.findAll("g-card", class_ = "ftSUBd")
    
    for card in cards:
        try:
            company = card.find("div", class_ = "CEMjEf NUnG9d").find("span").text.strip()
        except:
            company = "-"
        try:
            topic = card.find("div", class_ = "iRPxbe").findAll("div")[1].text.strip()
        except:
            topic = "-"
        try:
            link = card.find("a", class_ = "WlydOe").get("href")
        except:
            link = "-"
        data.append([company, topic, link])
        
    try:
        browser.find_element(By.CSS_SELECTOR, "#pnnext > span:nth-child(2)").click()
    except:
        break

headers = ["company", "topic", "link"]
df = pd.DataFrame(data, columns=headers)

df.to_csv("./news.csv", sep = ";", encoding = 'utf8')