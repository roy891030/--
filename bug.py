from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "/home/roy/桌面/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.dcard.tw/f")

# title = driver.title  # 取得標題


# 取得標籤

search = driver.find_element_by_name("query")  # 根據標籤的name做爬取
search.clear()  # 怕有預設文字，所以先清空欄位
search.send_keys("比特幣")  # 幫我在選定標籤欄中輸入比特幣
search.send_keys(Keys.RETURN)

# 等頁面跳轉
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "sc-3yr054-1")))


# 找文章標題tag
titles = driver.find_elements_by_class_name("tgn9uw-3 cUGTXH")
for title in titles:
    print(title.text)

# link = driver.find_element_by_link_text("#分享 Defi新手教學")
# link.click()

# driver.back()  # 回到上一頁
# driver.forward()  # 回到下一頁

time.sleep(5)
driver.quit()
