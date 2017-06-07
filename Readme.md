# Twitch Makes Art

## Sestavni deli

Projekt je sestavljen iz 4 datotek:

1. Program.py - glavni del projekta
2. IRCBot.py - IRC odjemalec, ki se poveže na strežnik Twitch chata in zatem na ustrezen kanal. Sprejeta sporoèila prefilitrira in jih vstavi v vrsto.
3. BoundingBox.py - razred, kjer lahko definiramo veljavna obmoèja miškinega kurzorja. Podprta oblika so samo pravokotniki.
4. AnarchyQueue.py - razred, kjer definiramo vrsto, v katero se vstavljajo ukazi.

### Program.py

V glavnini programa definiramo vse potrebne spremenljivke.
Program je razdeljen na 2 niti. Prva nit skrbi za premikanje miške, druga nit pa skrbi za IRC odjemalca.

V zaèetku je bila planirana tudi 3. nit, ki bi skrbela za to, da je okno slikarja vedno v fokusu. Na žalost je programska koda za to dejavnost še nekoliko hrošèata.