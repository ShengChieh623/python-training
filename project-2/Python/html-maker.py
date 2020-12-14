from fake_useragent import UserAgent
import requests
import csv
import time
import random
import codecs

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

i=0
with open('company.txt', 'r', encoding='utf-8') as kw:
    for keybrard in kw.readlines():
        i+=1
        keybrard=keybrard.strip('\n')
        url="https://www.google.com/search?q="+keybrard
        # 進入搜尋引擎
        if req(url) != None:
            print('Searching ['+str(i)+'. '+keybrard+'] page ...')
            soup = req(url)
            filename = str(i)+'. '+keybrard+'.txt'
            with open(filename, 'w', encoding="utf-8") as file:
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
                        file.write("<div class=\"title_banner about rellax\" data-rellax-zindex=\"1\" style=\"background-image: url('/public/UserFiles/upload/site/brand_bg.png');\">")
                        file.write("<div class=\"container\">\n")
                        file.write("<div class=\"banner_text text-right\">&nbsp;</div>\n")
                        file.write("</div>\n")
                        file.write("</div>\n")
                        file.write("\n")
                        file.write("<section class=\"port_item\">\n")
                        file.write("<div class=\"container-fluid  p-0\">\n")
                        file.write("<div class=\"col-lg-4 p-0\">\n")
                        file.write("<div class=\"port_main_pic rellax\" data-rellax-zindex=\"1\"><img src=\"/public/UserFiles/upload/upload/7-FCS-logo.png\" /></div>\n")
                        file.write("</div>\n")
                        file.write("\n")
                        file.write("<div class=\"col-lg-8 p-0\">\n")
                        file.write("<div class=\"port_text\">\n")
                        file.write("<h1 class=\"port_title\" style=\"color: #333333;\">"+keybrard+"</h1>\n")
                        file.write("\n")
                        file.write("<div class=\"port_propose\">\n")
                        file.write("<div class=\"port_topic\" style=\"background-color: #002b64;\">公司簡介</div>\n")
                        file.write("\n")
                        file.write("<ul>\n")
                        file.write("    <li>"+description+"</li>\n")
                        file.write("</ul>\n")
                        file.write("\n")
                        file.write("<div class=\"p-0 port_propose\">\n")
                        file.write("<div class=\"port_topic\" style=\"background-color: #002b64;\">相關專案連結</div>\n")
                        file.write("\n")
                        file.write("<ul>\n")
                        file.write("    <li><a href=\""+url+"\" target=\"_blank\">品牌官網</a></li>\n")
                        file.write("\n")
                        file.write("</ul>\n")
                        file.write("</div>\n")
                        file.write("</div>\n")
                        file.write("</div>\n")
                        file.write("</div>\n")
                        file.write("</div>\n")
                        file.write("</section>\n")
                        break
                    else:
                        continue
                
        else:
            continue
        time.sleep(random.uniform(1, 4))