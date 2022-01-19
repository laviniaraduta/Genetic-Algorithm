#Copyright Branzeu Mihnea, Raduta Lavinia, Nicoara Laura, Stan Andreea

# Genetic Algorithm
## Proiect realizat in cadrul cursului Python101 2021
## Echipa: Branzeu Mihnea, Raduta Lavinia, Nicoara Laura, Stan Andreea

### Functionalitate : Programul reprezinta un punct de pornire cand vine vorba de cautari in spatii complexe, poate infinite, unde rezultatul final este necunoscut (ceea ce determina incapacitatea de a verifica fiecare posibilitate de raspuns).

## Implementare : 
- class **DNA** : 
    -  **setFitness** - Metoda se ocupa cu aflarea fitness-ului ce reprezinta 
    **procentul aparitiei fiecarui caracter dintr-o fraza**.
        - spre exemplu, daca in cadrul frazei mele am 9 din 10 caractere corecte-un
        caracter este considerat corect daca acesta se afla pe aceeasi pozitie si este
        identic cu cel de la pozitia curenta din propozitia finala - spunem ca avem un
        fitness score de 90%.

    - **crossover** - Fiind date doua propozitii parinte se realizeaza o noua fraza
    formata din combinarea celor doi parinti.
        - o propozitie parinte este reprezentata de o fraza anterioara adaugata 
        intr-un vector de selectie numit **matingPool**, de un numar de ori setat
        in functie de procentul fitness obtinut pentru aceasta.

    - **mutate** - Pe baza unei probabilitati de mutatie data
    (numita **mutationRate**), metoda realizeaza o mutatie a ADN-ului copilului,
    prin generarea pe anumite pozitii a unui **caracter random** (practic, 
    metoda inlocuieste anumite caractere din fraza copil obtinuta anterior
    cu unele noi).

- class **Population** :
    - **naturalSelection** - Fiind data o populatie (multime constituita din
    toate frazele copil generate conform pasilor prezentati anterior),
    metoda adauga in vectorul de selectie matingPool fiecare componenta a
    populatiei de n ori (n calculat arbitrar, in functie de cel mai mare
    procent fitness obtinut de o fraza si procentul fitness al frazei
    curente).

    - **generate** - Metoda creeaza o noua generatie prin cresterea populatiei
    realizata prin adaugarea unui nou copil.

    - **getBest** - Fiind calculat **worldRecord** (ce reprezinta cel mai mare
    procent fitness obtinut de o fraza din populatie), metoda verifica daca
    fraza cu cel mai bun scor fitness este si cea cautata.
    In final, indiferent de rezultat, este returnat elementul populatiei cu
    cel mai bun procent fitness.

    - **getAllPhrases** - Metoda returneaza un string constituit din
    toate frazele ce se afla in populatie.
