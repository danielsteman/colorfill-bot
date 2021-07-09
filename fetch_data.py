from selenium import webdriver
import time

# Define PATH to chromedriver.exe in Chrome method
browser=webdriver.Chrome('chromedriver.exe')

browser.get("https://asr.axonify.com/training/index.html#index")
html = browser.page_source
time.sleep(2)
print(html)