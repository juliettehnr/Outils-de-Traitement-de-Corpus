import os
import re

fichier = './reviews.txt'

def clean_reviews(fichier):

    with open(fichier, "r", encoding='utf-8') as f:

        all_reviews = []

        texte = f.read()

        reviews = re.findall(r'<div class="cri_corps_critique shrinkable text br_150_de_hauteur" (.*?)</div>', texte, re.S)

        for review in reviews:

            txt_clean = str(re.sub(r'style="margin-bottom:3px;">', r'', review))
            txt_clean = str(re.sub(r'<a class=(.+) href=(.+)">', r'', txt_clean))
            txt_clean = str(re.sub(r'<a href="http(.+)">', r'', txt_clean))
            txt_clean = str(re.sub(r'id="(.+)"', r'', txt_clean))
            txt_clean = str(re.sub(r'\n', r'', txt_clean))
            txt_clean = str(re.sub(r'</a>', r'', txt_clean))
            txt_clean = str(re.sub(r'\t', r'', txt_clean))
            txt_clean = str(re.sub(r'<br/>', r'', txt_clean))
            txt_clean = str(re.sub(r"\xa0", r'', txt_clean))
            txt_clean = str(re.sub(r"\x97", r'', txt_clean))
            txt_clean = str(re.sub(r"\x93", r'', txt_clean))
            txt_clean = str(re.sub(r"\x85", r'', txt_clean))

            all_reviews.append(txt_clean)

    print(all_reviews)


if __name__ == "__main__":
    clean_reviews(fichier)
