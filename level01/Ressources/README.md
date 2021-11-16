ls -la:
toujours rien

id:
level01

find / -user level01 2> /dev/null
trop de chose

find / -user flag01 2> /dev/null
rien

j'ai chercher comment trouver un mdp sous l'inux je suis tomber sur des gens qui parler de deux dossier /etc/passwd ou /etc/shadow

je vais try

bingo je vois tous les flag et le flag01 et le seul a avoir un code visible:
42hDRfypTqqnw

je try le mdp

ca ne marche pas car il parait que c un password hash et c aussi un fichier je suis con

dans la video 42 il a parler de John

je tape john /etc/passwd sur internet et je recherche

bon apres de long recherche et de test il faut que je cree un fichier avec la ligne qui nous interesse pour apres utiliser john

je le fais sur ma machine et pas sur la vm car tous es bloquer
en faisant john --show test.txt on obtien

flag01:abcdefg:3001:3001::/home/flag/flag01:/bin/bash

abcdefg est donc le mdp