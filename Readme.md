# Twitch Makes Art (https://github.com/tjaz-brelih/TwitchMakesArt)

## Sestavni deli

Projekt je sestavljen iz 4 datotek:

1. Program.py
2. IRCBot.py
3. BoundingBox.py
4. AnarchyQueue.py

### Program.py

V glavnini programa definiramo vse potrebne spremenljivke.
Program je razdeljen na 2 niti. 
Prva nit skrbi za jemanje ukazov iz vrste in premikanje miške, druga nit pa skrbi za IRC odjemalca.

V začetku je bila planirana tudi 3. nit, ki bi skrbela za to, da je okno slikarja vedno v fokusu. 
Na žalost je programska koda za to dejavnost še nekoliko hroščata, zato je zagon te niti zakomentiran.

### IRCBot.py

V tej datoteki se nahaja definicija razreda in potrebne "callback" funkcije. 
Definirane funkcije se kličejo ob ustreznem dogodku.
Ob sprejemu se sporočilo filtrira.
V kolikor filtrirano sporočilo ustreza kateremu izmed ukazov ga dodamo v vrsto.

### BoundingBox.py

Definicija območij, v katerih se lahko nahaja miškin kurzor.
V kolikor miškin kurzor poskuša zapustiti katerega izmed območij, ga program vrne na najbližjo mejo.

### AnarchyQueue.py

Definira vrsto, v katerega se vstavljajo ukazi.
