from bs4 import BeautifulSoup
from urllib.request import urlopen
url="https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
page=urlopen(url)
soup=BeautifulSoup(page.read(), features="lxml")
stock_data=soup.find_all("tr", class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")
stock_list=[]
for data in stock_data:
	date_info=data.find_all("td", class_="Py(10px) Ta(start) Pend(10px)")
	stock_date=date_info[0].find("span").text.strip()
	price_data=data.find_all("td", class_="Py(10px) Pstart(10px)")
	stock_price=price_data[4].text.strip()
	print(stock_date, stock_price)

