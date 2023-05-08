from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Micael\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def pegar_url_cardapio_uefs():
    # testando pegando o url do cardapio
    driver.get("http://www.propaae.uefs.br/modules/conteudo/conteudo.php?conteudo=15")
    imagem = driver.find_element(By.CSS_SELECTOR, "img[alt='Cardápio']")
    anchor_da_imagem = imagem.find_element(By.XPATH, "..")
    url_cardapio = anchor_da_imagem.get_attribute("href")
    return url_cardapio

def proximos_eventos_python():
    url = "https://www.python.org/"
    driver.get(url)
    elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
    upcoming_events = [
        {"date": element.find_element(By.TAG_NAME, "time").text,
        "name": element.find_element(By.TAG_NAME, "a").text
        }
        for element in elements
    ]
    return upcoming_events

print(proximos_eventos_python())

driver.close()

