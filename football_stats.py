from bs4 import BeautifulSoup
from urllib.request import urlopen
url="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
page=urlopen(url)
soup=BeautifulSoup(page.read())

tables_rows = soup.findAll("tr", class_="TableBase-bodyTr")
player_list=[]
# Go through all the rows
for row in tables_rows:
	td = row.find_all("td")
	name = td[0].find('a').text.strip()
	touchdowns = td[8].text.strip()
	player_list.append([name,touchdowns])

for i in range(0,20):
	print(player_list[i][0], "|", player_list[i][1])

