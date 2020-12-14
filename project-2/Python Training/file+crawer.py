import urllib.request as req

def getData(url, file):
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            file.write(title.a.string+"\n")
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

with open("crawler.txt", mode="w", encoding="utf-8") as file:
    pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
    count=0
    while count<3:
        pageURL="https://www.ptt.cc"+getData(pageURL,file)
        count+=1
# 抓取一個頁面的標題
