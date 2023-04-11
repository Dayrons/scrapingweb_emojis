import json


class Export:
   
    def __init__(self, file:str, results) -> None:
        if file == '.txt':
            self.export_txt(results)
        if file == '.json':
            self.export_json(results)
       


    def export_txt(self,results):
        emojis =''
        for e in results:
            emojin_list = e.find("div",class_="emoji-list")
            emojis+= "\n"
            for emojin in emojin_list.find_all("span", class_="icone"):

                emojis += " " + emojin.get_text()

        f = open("emojis.txt", "w")
        f.write(emojis)
        f.close()

    def export_json(self,results):
        emojis ={}
        for e in results:
            emojin_list = e.find("div",class_="emoji-list")
            title = e.find('h3').get_text()
          
            emojis[title] = []
            for emojin in emojin_list.find_all("span", class_="icone"):

                emojis[title].append(f"{emojin.get_text()}")


        with open('emojis.json', 'w') as file:
            json.dump(emojis, file, indent=4, ensure_ascii=False)
        