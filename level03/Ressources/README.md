classique ls -la
on voit un fichier level03

on cat ce fichier et la moitier et crypter
mais je viens de remarquer que c un executable quand je le lance il me dit exploit me

je vais regarder ce que je peux faire
bon ca ma l'air bien chaud tous ca
on me parle de binary analise je vais voir ce qu'on peut trouver

ok j'ai trouver des chose a tester
je fait ltrace de l'executable et j'obtien les fonction utiliser
il utilise juste echo: "system("/usr/bin/env echo Exploit me"Exploit me"

je vais chercher si je peux pas manipuler ce echo

j'ai fait des recherche et enfaite j'ai compris que la fonction peut me permettre d'utiliser getflag
il faut juste que je change la destination du echo don't je n'est pas le droit de lecture dans un echo que je controle

on ajoute donc la commande getflag a echo mais vue qu'on peut pas manipuller le env on le fait dans le tmp
donc echo "getflag" > /tmp/echo
ensuite il nous faut les droit donc
chmod 777 /tmp/echo
et pour finir
./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
 