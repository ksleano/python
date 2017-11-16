__author__ = 'kslea_000'
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser


productNameList = []
priceList = []
productType = []
productLink = []

results = {}
links = {}

button = []




def search(item):
    while True:
        try:
            amazonURL = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
            item = item.replace(' ','+')
            amazonURL = amazonURL + item
            print(amazonURL)
            html = urlopen(amazonURL)
            break
        except:
            print("HTTP Error 503. Overloading requests. Try again")
    return BeautifulSoup(html.read(), "html.parser")


def getResults(soup):
    for tag in soup.find_all("li", {"class":"s-result-item celwidget"}):

        # Product Link
        try:
            link = tag.find("a", href = True)['href']
            productLink.append(link)
            print(str(link))
        except:
            productLink.append('n/a')
            pass

        # Product Name
        try:
            title = tag.find("h2").text
            productNameList.append(title)
            print(title)
        except:
            pass

        # Product Type
        try:
            type = tag.find("h3").text
            productType.append(type)
            print(type)
        except:
            productType.append("n/a")
            pass

        # Product Price. Two parts.
        try:
            price = tag.find(class_="sx-price")
            priceWhole = price.findChildren()[1].text
            priceFractional = price.findChildren()[2].text
            price =  "$" + priceWhole +"." + priceFractional
            priceList.append(price)
            print(price)
        except:
            priceList.append("n/a")
            pass
        print()


def populateResults():
    index = 0
    for (name, type, price, link) in zip(productNameList, productType, priceList, productLink):
        results[index] = [name, type, price]
        links[name] = link
        index += 1
def createButtons():
    for i in range(len(results)):
        url = links[results[i][0]]
        fText = results[i][0] + " " + results[i][1] + "\n" + results[i][2]
        b = Button(root, text = fText, command = lambda link = url: openLink(link))
        button.append(b)
        button[i].grid(column = 1, row = i+1, sticky = W+E)

################################
def clickEvent(event):
    getResults(search(str(entry_1.get())))
    populateResults()
    createButtons()
    print(len(results))


def openLink(link):
    webbrowser.open_new(link)

root = Tk()

entry_1 = Entry(root)
button_1 = Button(root, text = "Search")
#button function
button_1.bind("<Button-1>", clickEvent)
# button placements
button_1.grid(row = 0, column = 2)
entry_1.grid(row = 0, column = 1)

root.mainloop()
