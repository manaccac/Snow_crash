ls -la
rien
id
uid=2014(level14) gid=2014(level14) groups=2014(level14),100(users)

ind / -user flag14 2> /dev/null
rien

cat /etc/passwd
flag14:x:3014:3014::/home/flag/flag14:/bin/bash

j'ai tester plein de chose et j'avoue ne pas trop trouver

je vais try ce que j'ai vue au flag 13 gbd mais sur getflag la seul ex qu'on a a dispo

ok il y a 1413 ligne ca va etre plus dur

bon apres pas mal de temps de recherche le ptrace bloque du coup je vais break avent et apres je jump avent la fin pour avoir le token

du coup je break avent
   0x08048982 <+60>:    movl   $0x0,(%esp)
   0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
donc je 
break *0x08048982
ensuite je run
et il faut que je stop apres un jump alors le quelle j'en ai aucune idee on va utiliser une technique appeler le je try jusqu'a que ca marche
bien connuer des plus grand dev

0x08048e86 <+1344>:  jmp    0x8048ead <main+1383> marche pas
0x08048e44 <+1278>:  jmp    0x8048ead <main+1383> marche pas
...
bon c long mais j'ai trouver un truc fou l'endroit ou est cmp si c le bon flag
   0x08048b33 <+493>:   je     0x8048bf3 <main+685>
   0x08048b39 <+499>:   cmp    $0xbb8,%eax
   0x08048b3e <+504>:   ja     0x8048c17 <main+721>
   0x08048b44 <+510>:   test   %eax,%eax
   0x08048b46 <+512>:   je     0x8048bc6 <main+640>
   0x08048b48 <+514>:   jmp    0x8048e06 <main+1216>
   0x08048b4d <+519>:   cmp    $0xbbc,%eax
   0x08048b52 <+524>:   je     0x8048c83 <main+829>
   0x08048b58 <+530>:   cmp    $0xbbc,%eax
   0x08048b5d <+535>:   ja     0x8048ca7 <main+865>
   0x08048b63 <+541>:   jmp    0x8048c5f <main+793>
   0x08048b68 <+546>:   cmp    $0xbc2,%eax
   0x08048b6d <+551>:   je     0x8048d5b <main+1045>
   0x08048b73 <+557>:   cmp    $0xbc2,%eax
   0x08048b78 <+562>:   ja     0x8048b95 <main+591>
   0x08048b7a <+564>:   cmp    $0xbc0,%eax
   0x08048b7f <+569>:   je     0x8048d13 <main+973>
   0x08048b85 <+575>:   cmp    $0xbc0,%eax
   0x08048b8a <+580>:   ja     0x8048d37 <main+1009>
   0x08048b90 <+586>:   jmp    0x8048cef <main+937>
   0x08048b95 <+591>:   cmp    $0xbc4,%eax
   0x08048b9a <+596>:   je     0x8048da3 <main+1117>
   0x08048ba0 <+602>:   cmp    $0xbc4,%eax
   0x08048ba5 <+607>:   jb     0x8048d7f <main+1081>
   0x08048bab <+613>:   cmp    $0xbc5,%eax
   0x08048bb0 <+618>:   je     0x8048dc4 <main+1150>
   0x08048bb6 <+624>:   cmp    $0xbc6,%eax
   0x08048bbb <+629>:   je     0x8048de5 <main+1183>
   0x08048bc1 <+635>:   jmp    0x8048e06 <main+1216>
   0x08048bc6 <+640>:   mov    0x804b060,%eax

je vais donc try en partant de la fin
0x08048bc1 <+635>:   jmp    0x8048e06 <main+1216> marche pas

0x08048bbb <+629>:   je     0x8048de5 <main+1183> MARCHE
le jump *0x8048de5
marche bon c assez comprehensible on voit que c un je donc en fonction d'une condition si on la check pas il va etre donc nous donner direct le token
Continuing at 0x8048de5.
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
[Inferior 1 (process 2036) exited normally]

level14@SnowCrash:~$ su flag14
Password: 
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)

flag14@SnowCrash:~$ getflag
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ

LET'S GO 
