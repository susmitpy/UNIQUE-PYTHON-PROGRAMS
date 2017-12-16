import bs4, urllib.request as req, pandas as pd

url = "http://quotes.toscrape.com"

sauce = req.urlopen(url)

soup = bs4.BeautifulSoup(sauce, "html.parser")

sauce.close()

##author_quote = {a:b for a, b in zip([e.get_text() for e in soup.find_all("small", class_ = "author")], [d.get_text() for d in soup.find_all("span", class_ = "text")])}

quote = [i.get_text() for i in soup.find_all("span", class_ = "text")]
author = [i.get_text() for i in soup.find_all("small", class_ = "author")]
##author_quote = {i:j for i, j in zip(author, quote)}

author_quote_table = {}
author_quote_table["Author"] = author
author_quote_table["Quote"] = quote

df = pd.DataFrame(author_quote_table)
df.set_index("Author", inplace = True)
print(df)

##for key, value in author_quote.items():
##    print(key + " : " + value)





