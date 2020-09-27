import logging

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient




def parse_data(list_urls):
    

    client = MongoClient()
    db = client["parse_habr"]
    collection = db["habr_python"]

    request_to_mongo = []

    count_parse_urls = 0
    for url in list_urls:

        count_parse_urls += 1

        try:
            result = requests.get(url)
            soup = BeautifulSoup(result.text, "html.parser")

            h1_block = soup.find("h1", {"class":"post__title post__title_full"})
            title_text = h1_block.find("span").text 

            wraper_block = soup.find("div", {"class":"post__wrapper"})
            post_date = wraper_block.find("span", {"class":"post__time"}).text

            ul_block = wraper_block.find("ul", {"class":"post__hubs post__hubs_full-post inline-list"})
            list_li = ul_block.find_all("li", {"class":"inline-list__item inline-list__item_hub"})

            intermediate_li = []
            for block_li in list_li:
                text = block_li.find("a").text 
                intermediate_li.append(text)

            direction = ", ".join(intermediate_li)

            document = {"title_text":title_text, "post_date":post_date, "direction":direction}
            request_to_mongo.append(document)

            if len(request_to_mongo) >= 10:
                collection.insert_many(request_to_mongo)
                request_to_mongo = []


        except Exception as ex:
            logging.error(ex)

    try:
        collection.insert_many(request_to_mongo)

    except Exception as ex:
        logging.error(ex)
    

    client.close()
    return 
        