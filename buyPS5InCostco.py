from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

productLink = "https://www.costco.ca/playstation-5-console-bundle---ratchet-%2526-clank.product.100780734.html"
email = "siyang.msy@gmail.com"
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

    radioBC = browser.find_elements(By.XPATH, "//input[@type='radio' and @value='BC']")
    radioBC[0].click()
    btnSetRegion = browser.find_elements(By.XPATH, "//input[@id='language-region-set']")
    btnSetRegion[0].click()


    # login
    loginLink = browser.find_elements(By.XPATH, "//*[@id='header_sign_in']")
    loginLink[0].click()

    emailAddr = browser.find_elements(By.XPATH, "//input[@id='signInName']")
    emailAddr[0].send_keys(email)
    pw = browser.find_elements(By.XPATH, "//input[@id='password']")
    pw[0].send_keys(pswd)
    signInBtn = browser.find_elements(By.XPATH, "//button[@id='next']")
    signInBtn[0].click()

    continueShopping = browser.find_elements(By.XPATH, "//*[@id='verify-membership']/div[2]/div/div/div/div/div[3]/input")
    continueShopping[0].click()

    return browser

def refreshAndBuy():
    browser = openBrowser()

    while True:
        try:
            btnAddToCart = browser.find_elements(By.XPATH, "//input[@id='add-to-cart-btn']")
            if btnAddToCart[0].is_enabled():
                print("Costco: ps5 is in stock!!!!")

                btnAddToCart[0].click()

                #time.sleep(2)
                wait = WebDriverWait(browser, 60)
                viewCart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='costcoModalText']/div[2]/div[2]/a/button")))
                viewCart.click()

                checkOut = browser.find_elements(By.XPATH, "//input[@id='shopCartCheckoutSubmitButton']")
                browser.execute_script("arguments[0].scrollIntoView();", checkOut[0])
                browser.execute_script("arguments[0].click();", checkOut[0])
                #checkOut[0].click() will have the error : Element is not clickable at point

                #input of cvv is hidden in iFrame
                secCodeIFrame = browser.find_element(By.XPATH, "//*[@id='cc_cvv_div']/iframe")
                browser.switch_to.frame(secCodeIFrame)
                secCode = browser.find_element(By.XPATH, "//*[@id='securityCode']")
                secCode.send_keys(cvvCode)
                browser.switch_to.default_content()

                # !!! for empty cart
                shippingOptions = browser.find_elements(By.XPATH, "//input[@value='Continue to Shipping Options']")
                shippingOptions[0].click()

                placeOrder = browser.find_elements(By.XPATH, "//input[@value='Place Order']")
                placeOrder[0].click()

                os.system("watch -n 1.5 play -nq -t alsa synth 1 sine 400")
                break
            else:
                print("Costco: ps5 is out of stock :(")

            browser.refresh()
        except Exception as e:
            print(e)
            print("reopen browser")
            browser = openBrowser()

    browser.close()


refreshAndBuy()

