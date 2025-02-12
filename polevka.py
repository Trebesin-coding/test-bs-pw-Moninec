from bs4 import BeautifulSoup
import requests
import json


def main():

    url = "https://js-trebesin.github.io/bsoup-exam/"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser") #Pomocí krásné polévky scrapujeme content ze zadaného url, html.parser je předpřipravené procházeníá html

    food = soup.find_all("h2")

    good_food = [food[0].text, food[1].text, food[2].text, food[3].text]

    print(good_food)

    with open("recept.json", mode="w") as file:
        json.dump(good_food, file, indent=4, ensure_ascii=False)



    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá


if __name__ == "__main__":
    main()