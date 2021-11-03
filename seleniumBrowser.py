from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def openBrowser():
    browser = webdriver.Chrome()

    browser.get("https://www.costco.ca/playstation-5-console-bundle---ratchet-%2526-clank.product.100780734.html")

    radioBC = browser.find_elements(By.XPATH, "//input[@type='radio' and @value='BC']")
    radioBC[0].click()
    btnSetRegion = browser.find_elements(By.XPATH, "//input[@id='language-region-set']")
    btnSetRegion[0].click()
    return browser

browser = openBrowser()

while True:
    try:
        btnAddToCart = browser.find_elements(By.XPATH, "//input[@id='add-to-cart-btn']")
        if btnAddToCart[0].is_enabled():
            print("ps5 is in stock!!!!")
            os.system("watch -n 1.5 play -nq -t alsa synth 1 sine 400")
            break
        else:
            print("ps5 is out of stock :(")

        browser.refresh()
    except:
        print("reopen browser")
        browser = openBrowser()

browser.close()


