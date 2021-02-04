from bs4 import BeautifulSoup
from selenium import webdriver
import winsound
import requests
import time


## CONSTANTS: ##
page = "https://cdon.se/spel/playstation-5-release-2021-54876367" ## Full
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
          }

## Start driver
driver = webdriver.Chrome("./chromedriver.exe")

## Check with requests
while 1:
    try:
        r = requests.get(page, headers=headers)

        soup = BeautifulSoup(r.text, 'html.parser')

        if soup.find_all(class_='buy-area__buy-button-skeleton')[0]['title'] == "Den här produkten är tyvärr inte köpbar för tillfället.":
            print("Slutsåld")
            time.sleep(0.1)
            continue
        else:
            break
    except Exception as err:
        print(err)

    time.sleep(0.1)



## Get page and click button
driver.get(page)

add_to_cart_button = driver.find_element_by_css_selector("button.buy-area__buy-button")

driver.execute_script("arguments[0].click();", add_to_cart_button)


time.sleep(0.3)

# Go to cart
go_to_cart_button = driver.find_element_by_css_selector("a.cart-pop-up__checkout-link")

driver.execute_script("arguments[0].click();", go_to_cart_button)

# Sound
frequency = 2000  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
