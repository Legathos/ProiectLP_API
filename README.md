# ProiectLP_API
Proiectul pentru Limbaje de programare.

Echipa: 11-E1
Studenti: BORBELY G. GERCHARDT-NIKOLAS, CĂPRAR M. ALBERT
Tema proiect: D1-T1 | Dezvoltare API

Cerinta: Dezvoltați un API ce interacționează cu un fișier de tip JSON.


Sources:

    https://github.com/DataLabUPT/pyLab.git
    
    https://www.youtube.com/@Indently
    
    https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
    
    https://stackoverflow.com/questions/61990522/how-to-correctly-download-a-json-file-from-github-using-python
    

This python program downloads a json file from a github repository (given the path to the repository) 
and creates a Flask app that is hosted on a local development server.

Functionality:

      http:/localhost/ -> returns the ful json file 
      
      http:/localhost/cauta/title/word -> returns a list of all titles containing "word"
      
      http:/localhost/title -> returns a list of all the titles in the json file
      
