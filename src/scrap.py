import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.babelio.com/livres/Orwell-1984/2961/critiques?a=a&pageN='

def scrap_babelio():

    with open('reviews.txt', 'w') as f:

        for page in range(1,11):

            r = requests.get(url + str(page))

            soup = bs(r.text, 'html')

            review = soup.find_all('div', class_ ="cri_corps_critique shrinkable text br_150_de_hauteur")

            f.write(str(review))


if __name__ == "__main__":
    scrap_babelio()
