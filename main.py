"""
Echipa: 11-E1
Studenti: BORBELY G. GERCHARDT-NIKOLAS, CĂPRAR M. ALBERT
Tema proiect: D1-T1 | Dezvoltare API

Cerinta: Dezvoltați un API ce interacționează cu un fișier de tip JSON.

Sources:
    https://github.com/DataLabUPT/pyLab.git
    https://www.youtube.com/@Indently
    https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
    https://stackoverflow.com/questions/61990522/how-to-correctly-download-a-json-file-from-github-using-python
"""

import requests
import json
import os
from flask import *

# link catre repo-ul de github
url = "https://github.com/dotnet-presentations/ContosoCrafts/blob/master/src/wwwroot/data/products.json"


def changeURL(giturl):
    """
    :param giturl:
    :return: rawURL
    functia primeste url-ul catre repository-ul de pe github
    si il transforma intr-un raw-URL direct catre fisierul de tip json
    """
    # inlocuim parti din url pentru a putea fi transformat in rawURL
    rawURL = giturl.replace("github.com", "raw.githubusercontent.com")
    rawURL = rawURL.replace("/blob/", "/")
    return rawURL


# apelam functia de mai sus pentru a schimba url-ul
url = changeURL(url)
# facem un request sa primim obiectul de tip response
getResponse = requests.get(url)
# preluam partea de content din obiectul response
urlContent = getResponse.content
# incarcam obiectele json in lista jsondata
jsondata = json.loads(urlContent)

# se verifica daca exista directory-ul localFile si fisierul date.json
# daca nu exista vor fi create
if not os.path.isdir("localFile"):
    os.mkdir("localFile")
# jsondata va fi descarcat in fisierul facut mai sus
with open("localFile/date.json", "w") as i:
    json.dump(jsondata, i, indent=2)

# se creaza o instanta Flask (folosim "__name__" pentru ca avem doar un modul"
app = Flask(__name__)


# creare functie pentru adresa http:localhost/ ( home )
@app.route("/")
def homePage():
    """
    functia va afisa toate obiectele json
    :return: JSONdata
    """
    with open("localFile/date.json", "r") as j:
        JSONdata = json.load(j)
    return JSONdata


# creare functie pentru adresa http:localhost/cauta/title/cuvantCautat
@app.route("/cauta/title/<cuvantCautat>")
def searchByTitle(cuvantCautat):
    """
    :param cuvantCautat: user input
    :return: titluri - o lista cu titlurile care contin cuvantul respectiv

    se itereaza prin fisierul json local in sectiunea "Title" si daca o parte din titlu cosrespunde cu
    acel cuvantCautat acesta va fi adaugat la lista titluri
    """
    with open("localFile/date.json", "r") as k:
        JSONdata = json.load(k)
        titluri = list()
        for obj in JSONdata:
            if cuvantCautat in obj["Title"]:
                titluri.append(obj)
    return titluri


# creare functie pentru adresa http:localhost/title
@app.route("/title/")
def showAllTitles():
    """
    :return: titluriTotal - o lista cu toate titlurile
    se itereaza prin fisierul json local si se adauga toate titlurile intr-o lista care este returnata de functie
    """
    with open("localFile/date.json", "r") as file:
        JSONdata = json.load(file)
    titluriTotal = list()
    for obj in JSONdata:
        titluriTotal.append(obj["Title"])
    return titluriTotal


# se porneste aplicatia Flask pe un server local
app.run()
