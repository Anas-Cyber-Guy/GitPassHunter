from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
import time
the_key = Service(r"C:\Developer/chromedriver.exe")
Repos = []
last_link = [] #This list to include the main python file so that we can open it.
scrape = input("what Github page would you like to scrape? ")
driver = webdriver.Chrome(service=the_key, options=options)
# driver = webdriver.Chrome(service=the_key)
driver.get(f"{scrape}")
time.sleep(2)
####################################################################################
def click_the_raw_button(raw):
    raw_button = driver.find_element(By.XPATH, '//*[@id="repos-sticky-header"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a/span/span')
    raw_button.click()
    time.sleep(3)
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"Password found {raw}" )
    else: 
        print("Nope, nothing there")

#####################################################################################3
def second_page(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    for a in res2:   
        if "py" in a.text:
            last_link.append(f"{next_page}/blob/main/{a.text}")
            for c in last_link:
                driver.get(f"{c}")
                time.sleep(2)
            click_the_raw_button(c)
######################################################################################
res = driver.find_elements(By.CLASS_NAME, "repo")
for i in res:
    Repos.append(f"{scrape}/{i.text}")
for e in Repos:
    second_page(e)

driver.quit()