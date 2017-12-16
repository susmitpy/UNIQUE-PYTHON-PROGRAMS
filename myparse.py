import bs4, urllib.request as req

def parse(url):
    url = url
    sauce = req.urlopen(url)
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    sauce.close()
    return soup
