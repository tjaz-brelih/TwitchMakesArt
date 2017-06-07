# Twitch Makes Art

## Sestavni deli

Projekt je sestavljen iz 4 datotek:

1. Program.py - glavni del projekta
2. IRCBot.py - IRC odjemalec, ki se pove�e na stre�nik Twitch chata in zatem na ustrezen kanal. Sprejeta sporo�ila prefilitrira in jih vstavi v vrsto.
3. BoundingBox.py - razred, kjer lahko definiramo veljavna obmo�ja mi�kinega kurzorja. Podprta oblika so samo pravokotniki.
4. AnarchyQueue.py - razred, kjer definiramo vrsto, v katero se vstavljajo ukazi.

### Program.py

V glavnini programa definiramo vse potrebne spremenljivke.
Program je razdeljen na 2 niti. Prva nit skrbi za premikanje mi�ke, druga nit pa skrbi za IRC odjemalca.

V za�etku je bila planirana tudi 3. nit, ki bi skrbela za to, da je okno slikarja vedno v fokusu. Na �alost je programska koda za to dejavnost �e nekoliko hro��ata.