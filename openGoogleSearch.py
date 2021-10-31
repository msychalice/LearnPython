import requests, bs4, sys, webbrowser

keyWords = " ".join(sys.argv[1:])
print(f"searching '{keyWords}'")
res = requests.get("https://google.com/search?q=" + keyWords)

try:
    res.raise_for_status()

    #print(res.text)
    htmlFile = open("g.html", "wb")
    for chunk in res.iter_content(10000):
        htmlFile.write(chunk)
    htmlFile.close()

    parsedHtml = bs4.BeautifulSoup(res.text, "html.parser")

    # the class name "kCrYT" is different from Chrome, need to double check in the downloaded html file above
    results = parsedHtml.select("div.kCrYT > a")

    print(f"found {len(results)} results")

    for l in results:
        link = l.get("href")
        #print(link)
        link = link[7:] # remove "/url?q=
        postfix = link.find("&sa=")
        link = link[:postfix] # remove all the character starting from "&sa="

        print(link)
        webbrowser.open(link)

except Exception as ex:
    print(ex)

