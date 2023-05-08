from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "D:\Micael\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get(url)
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys(f"Python {Keys.ENTER}")

url = ""
driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Micael")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Muniz")

email = driver.find_element(By.NAME, "email")
email.send_keys("example@micaelmuniz.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
