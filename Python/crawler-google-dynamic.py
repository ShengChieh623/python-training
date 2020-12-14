# coding: utf-8
"""
Post the query to Google　Search and get the return results
"""
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Browser settings 設定參數: 瀏覽器的設定、以及查詢 Query 的關鍵字設定、還有翻頁次數的設定。
chrome_options = Options()
chrome_options.add_argument('--incognito') # 使用無痕模式
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36') # 設定 user-agent
browser = webdriver.Chrome(chrome_options=chrome_options) 

# Query settings
query = '普拉瑞斯'
browser.get('https://www.google.com/search?q={}'.format(query))
next_page_times = 1


# Crawler
for _page in range(next_page_times):
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    content = soup.prettify()

    # Get titles and urls
    titles = re.findall('<h3 class="[\w\d]{6} [\w\d]{6}">\n\ +(.+)', content)
    urls = re.findall('<div class="r">\ *\n\ *<a href="(.+)" onmousedown', soup.prettify())

    for n in range(min(len(titles), len(urls))):
        print(titles[n], urls[n])

    # Wait
    time.sleep(5)

    # Turn to the next page
    try:
        browser.find_element_by_link_text('下一頁').click()
    except:
        print('Search Early Stopping.')
        browser.close()
        exit()


# Close the browser
browser.close()