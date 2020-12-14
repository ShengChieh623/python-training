import requests
import csv
import time
import random
import codecs
from bs4 import BeautifulSoup

def req(url):
    try:
        response = requests.get(url, headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
        }, verify=True) # SSL 驗證
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            target = BeautifulSoup(response.text,"html.parser")
            time.sleep(random.uniform(1, 4))
            return target
    except Exception as e:
        return None

try:
    with open('keywords.txt', 'r', encoding='utf_8_sig') as kw:
        for keybrard in kw.readlines():
            keybrard=keybrard.strip('\n')
            url="https://www.google.com/search?q="+keybrard
            # 進入搜尋引擎
            if req(url) != None:
                soup = req(url)
                filename = keybrard+'.csv'
                print(keybrard+' searching..')
                with open(filename, 'w', newline='', encoding="utf_8_sig") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Title', 'URL', 'Keywords', 'Description', 'h1']) 
                    # 爬搜尋結果 10 項 target
                    for target in soup.find_all("div", class_="yuRUbf"):
                        url = target.find("a").get("href")
                        if req(url) != None:
                            page = req(url) # 進入頁面
                            if page.find("title") != None: # 沒寫 meta
                                title = page.find("title").text.replace('\n','')
                            else:
                                title = target.find("a").text.replace('\n','')
                            if page.find(attrs={"name":"description"}) != None:
                                description = page.find(attrs={"name":"description"})['content'].replace('\n','')
                            else:
                                description = 'None'
                            if page.find(attrs={"name":"keywords"}) != None:
                                keywords = page.find(attrs={"name":"keywords"})['content'].replace('\n','')
                            else:
                                keywords = 'None'
                            if page.find('h1') != None:
                                h1 = page.find('h1').text.replace('\n','')
                            else:
                                h1 = 'None'
                            writer.writerow([str(title), url, str(keywords), str(description), str(h1)])
                        else:
                            continue
            else:
                continue
            print(keybrard+' search Page 1 done.')

        # 搜尋下一頁直到 i > 3 第三頁
        i=1

        for page in soup.find_all("tr")[0].find_all(class_="fl"):
            nextPage = "https://www.google.com"+page.get("href")
            if req(nextPage) != None:                
                np = req(nextPage)
                with open(filename, 'a', newline='', encoding="utf_8_sig") as csvfile:
                    writer = csv.writer(csvfile)
                    for target in np.find_all("div", class_="yuRUbf"):                
                        url = target.find("a").get("href")
                        if req(url) != None:
                            page = req(url) # 進入頁面
                            if page.find("title") != None: # 沒寫 meta
                                title = page.find("title").text.replace('\n','')
                            else:
                                title = target.find("a").text.replace('\n','')
                            if page.find(attrs={"name":"description"}) != None:
                                description = page.find(attrs={"name":"description"})['content'].replace('\n','')
                            else:
                                description = 'None'
                            if page.find(attrs={"name":"keywords"}) != None:
                                keywords = page.find(attrs={"name":"keywords"})['content'].replace('\n','')
                            else:
                                keywords = 'None'
                            if page.find('h1') != None:
                                h1 = page.find('h1').text.replace('\n','')
                            else:
                                h1 = 'None'
                            writer.writerow([str(title), url, str(keywords), str(description), str(h1)])
                        else:
                            continue
                i+=1
                if i > 3:
                    break
            else:
                break
            print(keybrard+' search Page '+str(i+1)+' done.')
except Exception as e:
    print('error')