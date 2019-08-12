'''
    Title format is:
    <td>
        <a href="/wiki/MP41" title="MP41">MP41</a>
    </td>
'''

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def compare(str_type, first, second):
    result = []
    site = "https://en.gfwiki.com/wiki/List_of_" + str_type.strip().upper() + "_by_Maximum_Stats"


# gflwiki checks for user agent otherwise you'll get 403
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    bs = BeautifulSoup(page, features="lxml")

    # iter next first entry
    tbody = bs.tbody
    tr_list = tbody.find_all("tr")
    iter_tr_list = iter(tr_list)
    next(iter_tr_list)

    for tr in iter_tr_list:
        td_list = tr.find_all("td")
        hredLst = td_list[1].find("a")
        if first.lower() == hredLst.attrs['title'].lower() or second == hredLst.attrs['title'].lower():
            result.append([td_list[1].text.strip('\n'),
                           td_list[0].text.strip('\n'),
                           td_list[2].text.strip('\n'),
                           td_list[3].text.strip('\n'),
                           td_list[4].text.strip('\n'),
                           td_list[5].text.strip('\n'),
                           td_list[6].text.strip('\n')])
            print("T-doll name: " + td_list[1].text +
                  "Index: " + td_list[0].text +
                  "Max Dmg: " + td_list[2].text +
                  "Max EVA: " + td_list[3].text +
                  "Max ACC: " + td_list[4].text +
                  "Max ROF: " + td_list[5].text +
                  "Max HP: " + td_list[6].text +
                  "\n")
    for doll in result:
        print(doll)
        print()

# prompt for input
type_txt = "SMG"
first = input("First t-doll name.\n")
second = input("T-doll to compare.\n")
compare(type_txt, first, second)


