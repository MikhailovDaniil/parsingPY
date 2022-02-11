# Google "News" tab web scraping

I decided to collect first 10 pages of news about the olimpic games 2022 in google's news tab (Russian language)
This can be really useful if we want to analyze news topics (for example, how different news affilates tell people about ups and downs of their country or what they write about any doping scandals)
Of course, this code is universal in some way: to collect the information about others topics (or change the amount of loaded data) you just need to change some symbols in this code


Used libraries:
* [Selenium](https://www.selenium.dev/)
with their special [WebDriver](https://chromedriver.chromium.org/home) for the Chrome browser (`chromedriver.exe` is for the 98 Chrome version)
* [BeautifulSoup or bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Time](https://docs.python.org/3/library/time.html)
* [tqdm](https://github.com/tqdm/tqdm)
* [Pandas](https://pandas.pydata.org/)
