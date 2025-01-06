무공해_데이터_추출.py

from selenium import webdriver
from selenium.webdriver.common.By import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do")
time.sleep(1)

select_box = driver.find_element(By.ID, "year1")
select_box.click()
time.sleep(3)

select = select('year1')
select.select_by_value("option value")
time.sleep(3)

driver.quit()

data_entry = driver.find_elements(By.CSS_SELECTOR, 'thead') # 각 head 가져오기
data_entry = data_entry.text
print(data_entry[0], data_entry[1], data_entry[2]) # 