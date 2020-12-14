import requests
import time
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def req(url):
    ua = UserAgent()
    headers = {"user-agent": ua.random}
    try:
        response = requests.get(url, headers=headers, verify=True)
        # response = requests.get(url, headers={
        #     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
        # }, verify=True) # SSL 驗證
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            target = BeautifulSoup(response.text,"html.parser")
            return target
        else:
            return None
    except Exception as e:
        return None

soup = req("https://www.plascom.com.tw/zh_TW/index.html")

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
now+=".txt"

with open(now, mode="w", encoding="utf-16") as file:
    for heading in soup.find_all(["h3"]):
        file.write("=====台灣國際機械線上聯展=====\n" + heading.text.strip()+"\n")
        url="https://www.plascom.com.tw"+heading.find("a").get("href")
        file.write(url+"\n\n")

    for news in soup.find_all("ul",class_="list")[0].find_all("li"):
        file.write(news.text.strip()+"\n")
        url="https://www.plascom.com.tw"+news.find("a").get("href")
        file.write(url+"\n")
    else:
        print("台灣國際機械線上聯展: done")

soup = req("https://www.chinaplasonline.com/CPS21/showpress/trad/%e5%b1%95%e6%9c%83%e6%96%b0%e8%81%9e%e7%a8%bf")

with open(now, mode="a",encoding="utf-16") as file:
    file.write("\n=====ChinaPlas=====\n")
    for news in soup.find_all(class_="cms_a"):
        url=news.get("href")
        file.write(news.text.strip()+":\n"+url+"\n")
        page = req(url)
        description = page.find(attrs={"name":"description"})['content']
        if page.find(attrs={"name":"description"})!=None:
            description = page.find(attrs={"name":"description"})['content']
        else:
            description = "No description"
        file.write(description+"\n\n")
    else:
        print("Chinaplas: done")

soup = req("https://www.taipeiplas.com.tw/zh-tw/")

with open(now, mode="a",encoding="utf-16") as file:
    file.write("\n=====TaipeiPlas=====\n")
    for news in soup.find_all("div", class_="news_list")[0].find_all("li"):
        url="https://www.taipeiplas.com.tw"+news.find("a").get("href")
        file.write(url+"\n")
        page = req(url)
        if page.find(attrs={"name":"description"})!=None:
            description = page.find(attrs={"name":"description"})['content']
        else:
            description = "No description"
        file.write(description+"\n\n")
    else:
        print("TaipeiPlas: done")

soup = req("https://www.chanchao.com.tw/expo.asp?cat=PLS")
with open(now, mode="a",encoding="utf-16") as file:
    file.write("\n=====展昭展覽網=====\n")
    for news in soup.find_all("ul", class_="expo")[0].find_all("li"):
        file.write(news.text.replace('\n','')+"\n",)
    else:
        print("展昭展覽網: done")