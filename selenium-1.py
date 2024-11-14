import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

#定義編碼
sys.stdout.reconfigure(encoding='utf-8')

#初始化webdriver
driver = webdriver.Chrome()
#driver = webdriver.Chrome(Options=options)


#打開網頁
url = "https://www.google.com"
driver.get(url)

#等3秒
time.sleep(3)

#定位元素
elem = driver.find_element(By.NAME, "q")

#搜尋框輸入文字
elem.send_keys("How to learn selenium")

time.sleep(2)

#按下搜尋
elem.send_keys(Keys.RETURN)

#獲取搜尋文字結果
try:
    search_result = driver.find_element(By.ID, "search").text
    print("搜尋結果",search_result)
except NoSuchElementException:
    print("搜索结果未找到")

#點擊第一個搜尋結果
#elem = driver.find_element(By.CLASS_NAME, "LC20lb MBeuO DKV0Md")
elem = driver.find_element(By.TAG_NAME, "h3")
elem.click()

time.sleep(6)

#上一頁
driver.back()
time.sleep(1)


elem = driver.find_element(By.NAME, "q")
elem.clear()

time.sleep(1)

#下一頁
driver.forward()

#關閉
driver.quit()