from tkinter import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# window
window = Tk()
window.title("GFL Max Stats Comparator/Look up")
window.geometry('435x310')

# labels
lbl = Label(window, text="Enter the name(s) of T-doll(s).", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)
lbl_type = Label(window, text="Type(HG, SMG, RF, AR, MG): ", font=("Arial Bold", 12))
lbl_type.grid(column=0, row=1)
lbl_first = Label(window, text="First: ", font=("Arial Bold", 12))
lbl_first.grid(column=0, row=2)
lbl_second = Label(window, text="Second: ", font=("Arial Bold", 12))
lbl_second.grid(column=0, row=3)

# text area
type_txt = Entry(window, width=15)
type_txt.grid(column=1, row=1)
first_txt = Entry(window, width=15)
first_txt.grid(column=1, row=2)
second_txt = Entry(window, width=15)
second_txt.grid(column=1, row=3)

# listboxs to display results
listbox1 = Listbox(window)
listbox2 = Listbox(window)


def compare():
    listbox1.delete(0, END)
    listbox2.delete(0, END)
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
            result.append(["T-doll name: " + td_list[1].text.strip('\n'),
                           "Index: " + td_list[0].text.strip('\n'),
                           "Max Dmg: " + td_list[2].text.strip('\n'),
                           "Max EVA: " + td_list[3].text.strip('\n'),
                           "Max ACC: " + td_list[4].text.strip('\n'),
                           "Max ROF: " + td_list[5].text.strip('\n'),
                           "Max HP: " + td_list[6].text.strip('\n')])
    for doll in result:
        temp_count = 1
        for data in doll:
            if result.index(doll) == 0:
                listbox1.insert(temp_count, data)
                temp_count += 1
            else:
                listbox2.insert(temp_count, data)
                temp_count += 1


window.bind('<Return>', (lambda event: compare()))
btn = Button(window, text="Search", command=compare)
btn.grid(column=0, row=4)
listbox1.grid(column=0, row=5)
listbox1.configure(width=30)
listbox2.grid(column=1, row=5)
listbox2.configure(width=30)

window.resizable(0, 0)
window.mainloop()


# print("T-doll name: " + td_list[1].text +
#       "Index: " + td_list[0].text +
#       "Max Dmg: " + td_list[2].text +
#       "Max EVA: " + td_list[3].text +
#       "Max ACC: " + td_list[4].text +
#       "Max ROF: " + td_list[5].text +
#       "Max HP: " + td_list[6].text +
#       "\n")
