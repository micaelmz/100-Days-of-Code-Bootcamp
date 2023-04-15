from bs4 import BeautifulSoup
import requests

"""
https://myhttpheader.com/
é necessario pegar os headers desse site e passar alguns para o requets.get ao acessar o site da amazon pq se nao o retorno é um codigo 503 inves de 200, pq a amazon vai impedir 
vc acessar a pagina sem um header detectando q vc é robo e ta tentando acessar sem um navegador web, ja que os navegadores passam os headers automaticamente, podendo ate ter capcha
"""

# raw_content = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", 
#                            headers={
#                             "Content-Type":"text",
#                             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39",
#                             "Accept-Language":"pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
#                             })
# print(raw_content.status_code)

# soup = BeautifulSoup(raw_content.text, "html.parser")
# product_price = soup.find(name="span", class_="a-price-whole")
# print(product_price.text)


# -------------- RETRIEVE PRODUCTS FROM WISHLIST --------------
wishlist = "https://www.amazon.com.br/hz/wishlist/ls/1393HJNNV8PF7?ref_=wl_share"
raw_content = requests.get(wishlist, 
                           headers={
                            "Content-Type":"text",
                            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39",
                            "Accept-Language":"pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
                            })
print(raw_content.status_code)

soup = BeautifulSoup(raw_content.text, 'html.parser')
list_of_itens = soup.select("h2.a-size-base > a.a-link-normal")
list_of_itens_id = [item.get("href").split("/")[2] for item in list_of_itens]

#price_history_tracker = "https://camelcamelcamel.com/product/"
price_history_tracker = "https://keepa.com/#!product/12-"


raw_content = requests.get("https://keepa.com/#!product/12-B07SLPYV7S", 
                           headers={
                            "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
"ACCEPT-ENCODING": "gzip, deflate, br",
"ACCEPT-LANGUAGE": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
"CONTENT-LENGTH": "",
"CONTENT-TYPE": "",
"DEVICE-MEMORY": "4",
"DOWNLINK": "2.05",
"DPR": "1.5",
"ECT": "4g",
"REFERER": "https://www.google.com/",
"RTT": "250",
"SEC-CH-PREFERS-COLOR-SCHEME": "dark",
"SEC-CH-PREFERS-REDUCED-MOTION": "no-preference",
"SEC-CH-UA": '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
"SEC-CH-UA-ARCH": '"x86"',
"SEC-CH-UA-FULL-VERSION": '"112.0.1722.39"',
"SEC-CH-UA-MOBILE": "?0",
"SEC-CH-UA-MODEL": "",
"SEC-CH-UA-PLATFORM": '"Windows"',
"SEC-CH-UA-PLATFORM-VERSION": '"15.0.0"',
"SEC-FETCH-DEST": "document",
"SEC-FETCH-MODE": "navigate",
"SEC-FETCH-SITE": "cross-site",
"SEC-FETCH-USER": "?1",
"UPGRADE-INSECURE-REQUESTS": "1",
"USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39",
"VIEWPORT-WIDTH": "581"
                            })
print(raw_content.status_code)
print(raw_content.text)
soup = BeautifulSoup(raw_content.text, 'html.parser')
print(soup.find_all(class_="tracking__suggestion-item"))
