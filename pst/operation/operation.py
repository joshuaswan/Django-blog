import time
from selenium import webdriver

def maximize():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    print("maximize the browser")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()

maximize()

def setSize():
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com")
    print("set the size of the browser:width-480,height800")
    driver.set_window_size(480,800)
    time.sleep(5)
    driver.quit()

# setSize()

def backAndForward():
    driver = webdriver.Firefox()

    first_url = 'https://www.baidu.com'
    print("now access %s" %(first_url))
    driver.get(first_url)

    second_url = 'https://news.baidu.com'
    print("now access %s" %(second_url))
    driver.get(second_url)

    print("back to %s" %(first_url))
    driver.back()

    print("forward to %s" %(second_url))
    driver.forward()

    driver.quit()

# backAndForward()

