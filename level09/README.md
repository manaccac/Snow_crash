ls -la
ex level09
et fichier token

level09@SnowCrash:~$ cat token
f4kmm6p|=�p�n��DB�Du{��
level09@SnowCrash:~$ ./level09 token
tpmhr

quand on utilise ltrace on trouve rien

donc on va tester des chose avec l'exec
./level09 00000000000
0123456789:
bon ok je pense qu'on peut faire un truc avec ca car chaque charactere en plus on ajoute le nombre de carac avent

ex ./level09 00000
0 + 0 = 0
0 + 1 = 1
0 + 2 = 2
0 + 3 = 3
0 + 4 = 4

on peut try un script avec cette idee
on va le copier dans notre machine pour plus de faciliter 
scp -P 4242 level09@[ip]:/home/user/level09/token .

ensuite on ecrit du code en phyton parsqu'on nous dit python scripting dans la video

il faut juste enlever le nombre i qui augmente a chaque fois qu'on avance dans la liste

ca nous donne donc:
Before f4kmm6p|=�p�n��DB�Du{��

After f3iji1ju5yuevaus41q1afiuq

on su flag09
et hop
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z