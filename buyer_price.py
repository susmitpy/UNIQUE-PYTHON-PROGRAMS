import myparse, re, csv

names = []
prices = []

f = open("name_price.csv", "w")
writer = csv.writer(f)
def newurl(number):
    stanurl = "http://econpy.pythonanywhere.com/ex/"
    newurl = stanurl + "00" + str(number) + ".html"
    return newurl

def scrap(soup):
    soup = soup
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text = soup.getText()
    ########   NAMES
    allnames = re.findall(r'[A-Za-z]+ [A-Za-z]+.+', text)
    [names.append(i) for i in allnames]
    ######## PRICES
    allprices = re.findall(r'\$\d+\.\d+', text)
    [prices.append(i) for i in allprices]

def preparesoups():
    links = [str(i) for i in range(1, 6)]
    for i in links:
        soup = myparse.parse(newurl(i))
        scrap(soup)

def preparedict(n, p):
    name_price = {i:j for i, j in zip(n, p)}
    return name_price

preparesoups()
semi_final = preparedict(names, prices)

for i, j in semi_final.items():
    writer.writerow([i, j])
f.close()

for i, j in semi_final.items():
    print(i + " : " + j)



