Titre : [Atelier] Challenges de programmation  
Sous-titre : Venez résoudre différents problèmes de programmation en C !


Salut les agrumes ! :)

Aujourd'hui je vous apporte des petits défis de programmation à résoudre en C.

[[question]]
| Pourquoi avoir choisi le C ?

A la base, j'avais rédigé ces défis pour un futur [défi de Clem](https://zestedesavoir.com/forums/sujet/3813/les-defis-de-clem/) mais après avoir eu quelques retours et sur une décision personnelle, j'ai transformé ce défi en *atelier* car il était déjà trop orienté vers le C (or les défis de Clem se veulent neutre en langage), et je préfère réaliser un bon atelier plutôt qu'un défi médiocre à cause d'un choix de langage. ;) D'autant plus, je ne pense pas que se limiter à un seul langage soit une mauvaise chose (cf le [Javaquarium](https://zestedesavoir.com/forums/sujet/447/javaquarium/) qui était au départ uniquement pour le Java), et au contraire un mélange entre choix du langage et langage spécifique permet d'explorer bien des idées.

Maintenant, place aux différents challenges qui sont présentés par ordre de difficulté.

## Qui a la plus petite ... solution ?!

Le sujet est simple, il faut réaliser un programme qui prend en entrée un nombre $N$ de lignes, $M$ de colonnes et qui affiche en sortie un rectangle de dimension $N \times M$ avec chaque ligne constituée soit de X (sur une ligne paire), soit de O (sur une ligne impaire).

**Exemple**

Entrée : 3 4  
Sortie :  
OOOO  
XXXX  
OOOO

Là où réside le véritable challenge est qu'il faut coder ce programme en utilisant le moins de caractères possible (absolument tout compte) ! On appelle cette pratique le *code golf* pour ceux que ça intéressent. ;)

## Akinator

Le but de ce deuxième défi est d'expliquer la sortie de ce programme, c'est-à-dire de deviner ce qu'il va afficher mais surtout pourquoi il va le faire. Cependant, il y a quelques contraintes :

- Interdit de copier/coller le code dans un éditeur.
- Interdit de compiler le code.
- Vous devez uniquement le lire ici.

![On a dit pas de copier/coller !](https://github.com/napnac/zds-prog/blob/master/c_puzzles/original_post/image_code_challenge2.png)

## NSA

Jusqu'à quel point pouvez-vous *exploiter* ce code comportant une (ou plusieurs ?) faille(s) de sécurité ?

```c
#include <stdio.h>
#include <string.h>

#define TAILLE_MAX 256

int main(int argc, char **argv)
{
   char buffer[TAILLE_MAX + 1];
   int top_secret = 0;
   
   if(argc <= 1) {
      printf("Veuillez indiquer une chaine en argument du programme !\n");
      return -1;
   }

   strcpy(buffer, argv[1]);

   printf("Vous avez entre : \n");
   printf(buffer);
   printf("\n\n");

   if(!strcmp(buffer, "code_secret"))
      top_secret = 1;

   if(top_secret)
      printf("Vous etes rentre dans la partie top secrete du programme !\n");

   return 0;
}
```

L'idée ici est, dans un premier temps, de repérer la/les faille(s), puis de chercher à l'/les exploiter pour créer des comportements non voulus (par exemple rentrer dans la partie secrète du programme, **mais pas que !**).

A vous de faire vos propres recherches sur la manière d'aborder le sujet. Mais pour ceux qui sont totalement perdus, je vous conseille de regarder du côté du [buffer overflow](https://fr.wikipedia.org/wiki/D%C3%A9passement_de_tampon) pour vous aider...

*Si vous avez réussi à trouver une faille facilement, essayez d'en chercher d'autres. Ca peut toujours être intéressant....*

## This is madness !

J'ai peut-être "un peu" forcé sur ce challenge...

Le défi est de comprendre comment fonctionne ce programme et donc d'expliquer comment il affiche sa sortie (je vous laisse l'exécuter pour voir le résultat) :

```c
char*main(int l,char*s,char*_,int r,int t){
return(l==7)?0:l==1&&r!=1?main(l,"wzqzmv{*##bv/{}qzv=*\
|v|:;r/az~v=*|ve*&#;r/m|#vbm*|#evb#evez@zm~v=*|;r/tbnzv=*\
|v$m=;r/@b=v{**e`=z;r/~zaavbva}zvb#ev'|m~v=*|lr/","r~{nb@:\
#wmq;*=&z`'$}t|vlea\ntgkaspnNrv,oywebhcimu !dl",1,t):r>1?
t>=3?*s=='/'?8:main(l,s,_,r,-9)?main(l,++s,_,r,3):
-4:t<0?*s==*_?putchar(*(_+26)):main(l,s,++_,r,-7):
!l?s:*s=='/'?main(++l,++s,_,r,2):main(l,++s,_,r,1):
r?main(0,main(0,s,"mqk@]0",2,1),_,2,12),
main(-l,main(-l,s,"qkK~z@",2,2),_,2,27),main(++l,s,_,r,t):8;}
```

Oui, ceci est un programme écrit entièrement en C (il est dit *obfusqué*), et non ce programme n'est pas dangereux. Je précise que pour compiler ce code sans soucis, il faut utiliser `gcc` sans aucun flags :

```bash
# Compile le programme
gcc code.c -o code
# Execute le programme
./code
```

Il se peut que je donne des indices si je vois que les recherches sur ce code n'avancent pas assez, en tout cas j'autorise à chercher à plusieurs pour celui-là ! :p

---

Le but de cet atelier n'est pas de tout réussir, mais de vous faire découvrir de nouvelles choses intéressantes à propos du C (que ce soit par vous-même ou avec les solutions des autres). N'hésitez pas à poster vos avancées, vos découvertes, vos recherches et réflexions mais veillez à bien utiliser les balises secrètes pour éviter tout *spoil*.

J'espère que les quatre challenges vous plairont, et bonne chance à tous ! :)
