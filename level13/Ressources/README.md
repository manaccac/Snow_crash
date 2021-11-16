ls -la
ex level13

je le lance et il me dit 
UID 2013 started us but we we expect 4242
si on se souviens des premier flag
uid etait la quand on tap id:
uid=2013(level13) gid=2013(level13) groups=2013(level13),100(users)

je pense qu'on nous demande un uid de 4242 au lieu de 2013
bon du coup j'ai trouver une technique de debug de linux
gdb ensuite je vais tester des commande et voir ce qu'on peut faire avec

bon j'ai trouver un truc pas mal pour voir ce qui constitue notre ex 
disas main
Renvoie le code assembleur correspondant aux instructions hexadécimales du binaire
et dans ce qu'il nous renvoi il y a un seul cmp qui dois surment cmp notre uid avec 4242
0x0804859a <+14>:    cmp    $0x1092,%eax

ok ok donc je me dit que si je stop le progame avent la verification et le jump apres ca devrai le faire je vais mettre un:
break main 13
car la cmp ce fait a 14

je le run et 
ca marche pas je me suis tromper de syntax

break *main + 13
Breakpoint 3 at 0x8048599

ok ca marche maintenant je jump just apres
jump *0x080485a1
ca marche pas je vais test plus loin

ok apres avoir avancer un peu j'ai lu 2 seconde ce qu'il y avait d'ecrit et j'ai compris ou je devais jump
et hop
(gdb) jump *0x080485cb
Continuing at 0x80485cb.
your token is 2A31L79asukciNyi8uppkEuSx
[Inferior 1 (process 17088) exited with code 050]

le token pour su flag13
ok ca marche pas c le flag13 deja
2A31L79asukciNyi8uppkEuSx