from selenium import webdriver
from time import sleep
d = webdriver.Chrome()
d.get("file:///Users/aviel.buskila/Downloads/tip_calc%202/index.html")
d.find_element(by="id", value="billamt").send_keys("100")
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
d.find_element(by="id", value="peopleamt").send_keys("5")
d.find_element(by="id", value="musicamt").send_keys("2")
sleep(10)