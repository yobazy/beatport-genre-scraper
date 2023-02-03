from selenium import webdriver

PATH = "../chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.beatport.com/")