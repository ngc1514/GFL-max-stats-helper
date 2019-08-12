from tkinter import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

window = Tk()

window.title("GFL Max Stats Comparator/Look up")
window.geometry('360x300')

lbl = Label(window, text="Please enter names of two T-dolls.", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

lbl_type = Label(window, text="Type(HG, SMG, RF, AR): ", font=("Arial Bold", 12))
lbl_type.grid(column=0, row=1)
lbl_first = Label(window, text="First: ", font=("Arial Bold", 12))
lbl_first.grid(column=0, row=2)
lbl_second = Label(window, text="Second: ", font=("Arial Bold", 12))
lbl_second.grid(column=0, row=3)

type_txt = Entry(window,width=10)
type_txt.grid(column=1, row=1)
first_txt = Entry(window,width=10)
first_txt.grid(column=1, row=2)
second_txt = Entry(window,width=10)
second_txt.grid(column=1, row=3)

first_result= Label(window, text="", font=("Arial Bold", 12))
first_result.grid(column=0, row=4)
second_result = Label(window, text="", font=("Arial Bold", 12))
second_result.grid(column=1, row=4)


def clicked():
    lbl.configure(text="Btn clicked")


def compare():
    result = []
    site = "https://en.gfwiki.com/wiki/List_of_" + type_txt.get().strip().upper() + "_by_Maximum_Stats"

    # gflwiki checks for user agent otherwise you'll get 403
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    bs = BeautifulSoup(page, features="lxml")

    # skip first entry.
    tbody = bs.tbody
    tr_list = tbody.find_all("tr")
    iter_tr_list = iter(tr_list)
    next(iter_tr_list)

    for tr in iter_tr_list:
        td_list = tr.find_all("td")
        hred_list = td_list[1].find("a")
        if first_txt.get().lower() == hred_list.attrs['title'].lower() or second_txt.get().lower() == hred_list.attrs['title'].lower():
            result.append([td_list[1].text.strip('\n'),
                           td_list[0].text.strip('\n'),
                           td_list[2].text.strip('\n'),
                           td_list[3].text.strip('\n'),
                           td_list[4].text.strip('\n'),
                           td_list[5].text.strip('\n'),
                           td_list[6].text.strip('\n')])
    for doll in result:
        print(doll)
        print()


btn = Button(window, text="Compare", command=compare)
btn.grid(column=0, row=4)

window.mainloop()
