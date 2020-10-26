from bs4 import BeautifulSoup
from urllib.request import urlopen
url="https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
page=urlopen(url)
soup=BeautifulSoup(page.read(), features="lxml")

tables_rows = soup.findAll("tr", class_="TableBase-bodyTr")

player_list=[]
for row in tables_rows:
	td = row.find_all("td")
	info_list=[info_item for info_item in td]
	name = td[0].find('a').text.strip()
	position = td[0].find('span',class_="CellPlayerName-position").text.strip()
	team=td[0].find('span',class_="CellPlayerName-team").text.strip()
	touchdowns = td[8].text.strip()
	player_list.append([name, position, team, touchdowns])

for i in range(0,20):
	print(player_list[i][0], "|", player_list[i][1], "|", player_list[i][2], "|", player_list[i][3])

