import requests
from bs4 import BeautifulSoup


def scrapy():


    response =  requests.get('https://smiley.cool/es/emoji-list.php')
    
    page_parse = BeautifulSoup(response.content, "html.parser")
    results = page_parse.find_all("div", class_="emoji-theme-block")
    emojis =''
    for e in results:
        emojin_list = e.find("div",class_="emoji-list")
        emojis+= "\n"
        for emojin in emojin_list.find_all("span", class_="icone"):

            emojis += " " + emojin.get_text()

    f = open("emojis.txt", "w")

    f.write(emojis)

    f.close()

if __name__ == "__main__":
    scrapy()