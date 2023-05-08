from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Micael\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")
cookie_per_second = driver.find_element(By.ID, "cps")

# upgrade = {
#     "Time Machine": driver.find_element(By.ID, "buyTime machine"),
#     "Portal": driver.find_element(By.ID, "buyPortal"),
#     "Alchemy lab": driver.find_element(By.ID, "buyAlchemy lab"),
#     "Shipment": driver.find_element(By.ID, "buyShipment"),
#     "Mine": driver.find_element(By.ID, "buyMine"),
#     "Factory": driver.find_element(By.ID, "buyFactory"),
#     "Grandma": driver.find_element(By.ID, "buyGrandma"),
#     "Cursor": driver.find_element(By.ID, "buyCursor")
# }
upgrades = [
    {"upgrade": driver.find_element(By.ID, "buyTime machine"), "price": }
]



while True:
    cookie.click()
