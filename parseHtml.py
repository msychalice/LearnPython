import requests, bs4

res = requests.get("https://nostarch.com")

try:
    res.raise_for_status()

    noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
    #print(type(noStarchSoup))

    items = noStarchSoup.select("#topics > div > div.view-content > div > ul > li.views-row.views-row-3.views-row-odd > div > span > a")
    #print(type(items))

    for item in items:
        print(item)
        print(item.getText())
        print(f"value of 'href' is {item.get('href')}")
        print(f"value of 'id' is {item.get('id')}")

except Exception as ex:
    print(ex)

