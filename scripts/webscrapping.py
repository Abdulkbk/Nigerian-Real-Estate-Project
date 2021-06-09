import requests
from lxml import html
from csv import writer
# from config import links


def scrape(url_, filename, opentype, title_, state_, pages="1"):
    with open(filename, opentype, encoding='UTF8', newline="") as csv_file:
        csv_writer = writer(csv_file)
        # headers = ['bedrooms', 'bathrooms', 'toilets', 'parking_space', 'title', 'town', 'state', 'price']
        # csv_writer.writerow(headers)

        for p in range(int(pages)):
            link = url_ + "?page=" + str(p + 1)
            print(link)
            response = requests.get(link)
            contents = html.fromstring(response.content)
            listings = contents.xpath("//div[@itemprop='itemListElement']")

            for i in range(len(listings)):
                bedrooms = "None"
                bathrooms = "None"
                toilets = "None"
                parking_space = "None"
                town = listings[i].xpath(".//address/strong/text()")[0].split(",")[-2].strip()
                info = listings[i].xpath(".//li")
                price = float(listings[i].xpath(".//span[@class='price']/text()")[1].replace(",", ""))
                for j in range(len(info)):
                    if "Bedroom" in info[j].text_content():
                        bedrooms = int(info[j].text_content()[0])
                    if "Bathrooms" in info[j].text_content():
                        bathrooms = int(info[j].text_content()[0])
                    if "Toilets" in info[j].text_content():
                        toilets = int(info[j].text_content()[0])
                    if "Parking" in info[j].text_content():
                        parking_space = int(info[j].text_content()[0])

                # print([bedrooms, bathrooms, toilets, parking_space, title_, town, state_, price])
                csv_writer.writerow([bedrooms, bathrooms, toilets, parking_space, title_, town, state_, price])
                # link = url_


file_name = "../data/nigerian_real_estate.csv"
open_type = "a"
state = "Imo"
mid = "imo"

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/detached-duplexes/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Detached Duplex", state_=state, pages="6")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/semi-detached-duplexes/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Semi Detached Duplex", state_=state, pages="1")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/detached-bungalows/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Detached Bungalow", state_=state, pages="2")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/semi-detached-bungalows/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Semi Detached Bungalow", state_=state, pages="1")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/terraced-duplexes/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Terraced Duplexes", state_=state, pages="1")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/terraced-bungalows/" + mid + "/showtype",
       filename=file_name, opentype=open_type, title_="Terraced Bungalow", state_=state, pages="1")

scrape(url_="https://nigeriapropertycentre.com/for-sale/houses/block-of-flats/" + mid + "/showtype", filename=file_name,
       opentype=open_type, title_="Block of Flats", state_=state, pages="5")