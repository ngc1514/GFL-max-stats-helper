'''
    Title format is:
    <td>
        <a href="/wiki/MP41" title="MP41">MP41</a>
    </td>
'''

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

site = "https://en.gfwiki.com/wiki/List_of_SMG_by_Maximum_Stats"

# gflwiki checks for user agent
header = {'User-Agent': 'Mozilla/5.0'}
request = Request(site, headers=header)
page = urlopen(request)
soup = BeautifulSoup(page, features="lxml")

tbody = soup.tbody
tr_list = tbody.find_all("tr")
iter_tr_list = iter(tr_list)
next(iter_tr_list)

first = input("First t-doll name.\n")
second = input("T-doll to compare.\n")

for tr in iter_tr_list:
    td_list = tr.find_all("td")
    hredLst = td_list[1].find("a")
    if first.lower() == hredLst.attrs['title'].lower() or second == hredLst.attrs['title'].lower():
        print("T-doll name: " + td_list[1].text +
              "Index: " + td_list[0].text +
              "Max Dmg: " + td_list[2].text +
              "Max EVA: " + td_list[3].text +
              "Max ACC: " + td_list[4].text +
              "Max ROF: " + td_list[5].text +
              "Max HP: " + td_list[6].text +
              "\n")
