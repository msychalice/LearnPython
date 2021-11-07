from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

productLink = "https://www.bestbuy.ca/en-ca/product/playstation-5-console/15689336"
email = "matthew.ma.groupt@gmail.com"
pswd = ""
cvvCode = ""

def openBrowser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Chrome(options=options) # hide bot detection
    browser.maximize_window()
    # An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available.
    browser.implicitly_wait(60)

    browser.get(productLink)


    # login
    loginLink = browser.find_elements(By.XPATH, "//*[@id='root']/div/header/div/div/div[1]/div[2]/div[2]/div[1]/a")
    browser.execute_script("arguments[0].scrollIntoView();", loginLink[0])
    browser.execute_script("arguments[0].click();", loginLink[0])

    emailAddr = browser.find_elements(By.XPATH, "//*[@id='username']")
    browser.execute_script("arguments[0].scrollIntoView();", emailAddr[0])
    emailAddr[0].send_keys(email)
    #browser.execute_script("arguments[0].send_keys(\'" + email + "\');", emailAddr[0])
    pw = browser.find_elements(By.XPATH, "//*[@id='password']")
    browser.execute_script("arguments[0].scrollIntoView();", pw[0])
    pw[0].send_keys(pswd)
    #browser.execute_script("arguments[0].send_keys(" + pswd + ");", pw[0])
    wait = WebDriverWait(browser, 60)
    signInBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='signIn']/div/button")))
    signInBtn.click()

    return browser

def refreshAndBuy():
    browser = openBrowser()

    while True:
        try:
            btnAddToCart = browser.find_elements(By.XPATH, "//*[@id='test']/button")
            if btnAddToCart[0].is_enabled():
                print("Bestbuy: ps5 is in stock!!!!")

                browser.execute_script("arguments[0].scrollIntoView();", btnAddToCart[0])
                browser.execute_script("arguments[0].click();", btnAddToCart[0])

                checkOut = browser.find_elements(By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[3]/div/div/a[1]")
                browser.execute_script("arguments[0].scrollIntoView();", checkOut[0])
                browser.execute_script("arguments[0].click();", checkOut[0])
                #checkOut[0].click() will have the error : Element is not clickable at point

                continueCheckout = browser.find_elements(By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/section/div/main/section/section[2]/div[3]/div/a")
                browser.execute_script("arguments[0].scrollIntoView();", continueCheckout[0])
                browser.execute_script("arguments[0].click();", continueCheckout[0])

                secCode = browser.find_elements(By.XPATH, "//*[@id='cvv']")
                browser.execute_script("arguments[0].scrollIntoView();", secCode[0])
                secCode[0].send_keys(cvvCode)

                wait = WebDriverWait(browser, 60)
                placeOrder = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='posElement']/section/section[1]/button")))
                browser.execute_script("arguments[0].scrollIntoView();", placeOrder)
                placeOrder.click()

                os.system("watch -n 1.5 play -nq -t alsa synth 1 sine 400")
                break
            else:
                print("Bestbuy: ps5 is out of stock :(")
                time.sleep(5)

            browser.refresh()
        except Exception as e:
            print(e)
            print("reopen browser")
            browser = openBrowser()

    browser.close()


refreshAndBuy()

