import requests
from bs4 import BeautifulSoup
from models.Export import Export

def scrapy():

    response =  requests.get('https://smiley.cool/es/emoji-list.php')
    page_parse = BeautifulSoup(response.content, "html.parser")
    results = page_parse.find_all("div", class_="emoji-theme-block")
    Export('.json', results)


if __name__ == "__main__":
    scrapy()