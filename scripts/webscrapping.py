from lxml import html
import requests as req
import selenium as sel

URL = "https://nigeriapropertycentre.com/for-sale/houses/detached-duplexes/lagos/showtype"
response = req.get(URL)

tree = html.fromstring(response.content)
XPATH = "/html/body/div[1]/section/div/div/div/div[1]/div[3]"
root = tree.xpath(XPATH)[0]

divs = root.xpath('.//@itemprop')

print(divs)
