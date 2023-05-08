from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from time import sleep

chrome_driver_path = "D:\Micael\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

def get_upgrades():
    upgrades = {}
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "buyTime machine")))
    upgrades["Time Machine"] = driver.find_element(By.ID, "buyTime machine")
    upgrades["Portal"] = driver.find_element(By.ID, "buyPortal")
    upgrades["Alchemy lab"] = driver.find_element(By.ID, "buyAlchemy lab")
    upgrades["Shipment"] = driver.find_element(By.ID, "buyShipment")
    upgrades["Mine"] = driver.find_element(By.ID, "buyMine")
    upgrades["Factory"] = driver.find_element(By.ID, "buyFactory")
    upgrades["Grandma"] = driver.find_element(By.ID, "buyGrandma")
    upgrades["Cursor"] = driver.find_element(By.ID, "buyCursor")
    return upgrades

def try_best_upgrade_2():
    upgrades = get_upgrades()
    for upgrade in upgrades.values():
        is_avaliable = upgrade.get_attribute("class")
        if is_avaliable != "grayed":
            upgrade.click()
            break

def click_cookie():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookie")))
    cookie = driver.find_element(By.ID, "cookie")
    while True:
        cookie.click()

# Cria uma thread separada para o clique no cookie
cookie_thread = threading.Thread(target=click_cookie)
cookie_thread.start()

# Executa a verificação de upgrades no thread principal
while True:
    sleep(5)
    try_best_upgrade_2()
