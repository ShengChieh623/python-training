from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options() # 取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options) # 建立webdriver物件，傳入剛剛所下載的「瀏覽器驅動程式路徑」及「瀏覽器設定(chrome_options)」
chrome.get("https://www.wesexpo.com/exhibition") # 爬取網址