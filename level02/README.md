ls -la:
on trouve un fichier
level02.pcap
quand on le cat tous et crypter du coup je vais regarder comment faire mais dans la video il parler d'un site appeler cloudshark pour les fichier pcap

dabord mettre sa vm en pont/bridged et pas NAT

ensuite je copy le fichier sur mon bureau avec ✗ scp -P 4242 level02@[ip]:/home/user/level02/level02.pcap level02.pcap

je n'ai aucun droit de lecture je fais donc un chmod 777

du coup j'ai trouver wireshack qui fera le traville de decryptage

je lui donne le fichier .pcap que j'ai copier et de ca j'ai les communication cas recu le fichier
de ca je fait click droit follow tcp

et jai le passowrd ecrit 
Password: ft_wandr...NDRel.L0L

je vais tester sans les point parsque ca me parait bizarre

bon bon bon ca ne marche pas les point doivent avoir une utiliter
je vais chercher quelle et leur sinification

ok j'ai chercher les obtion sur wiresharck et deja si on passe en UTF8 on a le mdp sans point mais surtout si on passe en hexa on voit que les points sont des 7f
et si on regarde sur internet 7F	01111111	DEL
donc 7f = del
alors si on refait le mdp
ft_wandr/del/del/del = ft_wa
ft_waNDRel/del = ft_waNDRe
ft_waNDReL0L

ca marche !!!!
mdp: ft_waNDReL0L