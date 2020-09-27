import requests
import logging 

from bs4 import BeautifulSoup



def parse_urls(query):
    print(f"query search = {query}\n")
    list_urls = []

    count_page = 1
    while True:

        try:
            main_url = f"https://habr.com/ru/search/page{count_page}/?q={query}&target_type=posts&flow=&order_by=relevance"
            result = requests.get(main_url)
            soup = BeautifulSoup(result.text, "html.parser")


            page_body = soup.find("div", {"class":"page__body"})
            list_li = page_body.find_all("li", {"class":"content-list__item"})

            for block in list_li:
                h_block = block.find("h2", {"class", "post__title"})
                link = h_block.find("a").get("href")

                print(f"{count_page} -- {link}")

                list_urls.append(link)


            count_page += 1
            
        except Exception as ex:
            logging.error(ex)

    
    return list_urls
    

