# Solutions

## Challenge 1

Pas de solution à faire.

## Challenge 2

La sortie du programme est :

```
Probleme d'allocation memoire !
Probleme de multiplication !
Tout va bien !
```

- `Probleme d'allocation memoire !` : si on enlève le commentaire au dessus du `if`, le `printf` n'est pas exécuté ! En effet, le commentaire se finit avec le caractère '\', et en C cela annonce un commentaire **multiligne**. Le `if` est alors commenté mais la coloration syntaxique ne le montre pas (j'utilise le prétexte de ne pas vouloir de copier/coller pour décider de la coloration syntaxique). C'est d'ailleurs pourquoi il est interdit de le copier/coller dans un éditeur car sinon l'astuce est flagrante.
- `Probleme de multiplication !` : c'est un problème assez connu des macros, qu'on appelle *effet de bord*. En effet, si on remplace le contenu de la condition par notre macro, on a : `a + 1 * b + 2` ce qui n'est pas ce à quoi on s'attendait (on espérait plutôt `(a + 1) * (b + 2)`). Le résultat n'est donc pas 12. Pour éviter ce genre de situation, il faut mettre des parenthèses dans la macro de cette façon : `multiplication(a,b) (a) * (b)`.
- `Tout va bien !` : sans doute le piège le plus flagrant, car il y a un ';' juste après le `else` ce qui va créer un bloc vide. Le `printf` est alors **toujours** exécuté.

## Challenge 3

Pas de solution à faire.

## Challenge 4

Inspiré de http://research.microsoft.com/en-us/um/people/tball/papers/XmasGift/

Ce que j'ai fait :

Noter les chaines à afficher ("Never gonna ", "give you up,", "let you down,", "run around and desert you,", "make you cry,", "say goodbye,", "tell a lie and hurt you!").

Compter le nombre de lettres utilisées pour afficher toutes ces chaines (22 + espace + virgule + point d'exclamation + retour à la ligne = 26).

Séparation des chaines par '/' : 

```c
char *start = "Never gonna /give you up,\n/let you down,\n/run around and desert you,\n/make you cry,\n/say goodbye,\n/tell a lie and hurt you!/";
```

Création de l'encodage : 

```c
char *translation = "r~{nb@:#wmq;*=&z`'$}t|vlea\ntgkaspnNrv,oywebhcimu !dl";
```

1. J'ai mélangé les 26 lettres à utiliser : \ntgkaspnNrv,oywebhcimu !dl
2. J'ai choisi 26 autres lettres au hasard sur mon clavier, que j'ai mélangé : r~{nb@:#wmq;*=&z\`'$}t|vlea
3. J'ai écrit une fonction pour convertir ma chaine de départ avec l'encodage :

```
void conversion(void)
{
   int i, j;

   for(i = 0; i < strlen(start); ++i) {
      if(start[i] == '/')
         printf("/");
      else
         for(int j = 26; j < strlen(translation); ++j)
            if(translation[j] == start[i])
               printf("%c", translation[j - 26]);
   }
}
```

J'ai obtenu la chaine suivante : 

```c
char *strings = "wzqzmv{*##bv/{}qzv=*|v|:;r/az~v=*|ve*&#;r/m|#vbm*|#evb#evez@zm~v=*|;r/tbnzv=*|v$m=;r/@b=v{**e`=z;r/~zaavbva}zvb#ev'|m~v=*|lr/";
```

J'ai recopié le programme (les parties dont j'avais besoin, c'est-à-dire tout sauf `inner_loop`, et `outer_loop`).

Pour faire fonctionner le programme, je pouvais faire :

```c
print_string(0); // Never gonna ...
print_string(-1); // give you up,
print_string(0);
print_string(-2); // let you down,
print_string(0);
print_string(-3); // run around and desert you,
print_string(0);
print_string(-4); // make you cry,
print_string(0);
print_string(-5); // say goodbye,
print_string(0);
print_string(-6); // tell a lie and hurt you!
```

Maintenant, il faut tout compresser dans la fonction `main`, pour cela j'utilise la récursion.

#### Compresser `translate_and_put_char` dans `output_chars`

J'utilise une variable `t` qui me permet de déterminer quand je suis dans la fonction `output_chars` (t > 0) ou quand je suis dans `translate_and_put_char` (t <= 0). Du coup, je peux utiliser ce paramètre pour faire des appels récursifs avec une certaine valeur et ainsi compresser les deux fonctions ensemble.

On passe de :

```c
void translate_and_put_char(char c, char *trans)
{
   if(c == *trans)
      putchar(trans[26]);
   else
      translate_and_put_char(c, trans + 1);
}

void output_chars(char *s)
{
   if(*s == '/')
      return;
   translate_and_put_char(*s, translation);
   output_chars(s + 1);
}
```

A :

```c
void output_chars(char *s, char *trans, int t)
{
   if(t > 0) {
      if(*s == '/')
         return;
      output_chars(s, translation, -9);
      output_chars(s + 1, translation, 3);
   }
   else {
      if(*s == *trans)
         putchar(trans[26]);
      else
         output_chars(s, trans + 1, -7);
   }
}
```

J'en profite pour enlever la fonction `print_string` en la remplaçant juste par son contenu.

J'en profite pour réaliser des appels récursifs dans le `main` afin de ne plus avoir à appeler `print_string` à la main. Pour cela, j'utilise le premier paramètre de la fonction `main` (qui est initialisé à 1 car il correspond au nombre de paramètres du programme lorsque vous le lancez), et dès qu'il arrive à 7 j'arrête les appels récursifs. Au passage, je remplace la fonction `print_string` par son contenu, on obtient donc la fonction `main` suivante :

```c
int main(int index, char *string)
{
   if(index == 7)
      return 0;

   output_chars(skip_n_strings(0, strings), translation, 12);
   output_chars(skip_n_strings(-index, strings), translation, 27);
   main(++index, string);
}
```

#### Compresser `skip_n_strings` dans `output_chars`

Je réutilise l'astuce de la variable en plus pour me permettre de gérer un nouveau cas : celui où on est dans la fonction `skip_n_strings`. Notre fonction `output_chars` ressemble désormais à ça :

```c
char *output_chars(int n, char *s, char *trans, int t)
{
   if(t >= 3) {
      if(*s == '/')
         return "";
      output_chars(n, s, trans, -9);
      output_chars(n, s + 1, trans, 3);
   }
   else if(t < 0) {
      if(*s == *trans)
         putchar(trans[26]);
      else
         output_chars(n, s, trans + 1, -7);
   }
   else {
      if(n == 0)
         return s;
      if(*s == '/')
         return output_chars(n + 1, s + 1, trans, 2);
      else
         return output_chars(n, s + 1, trans, 1);
   }
}
```

Il faut aussi remplacer les appels dans le `main` à la fonction `skip_n_strings` :

```c
int main(int index, char *string)
{
   if(index == 7)
      return 0;

   output_chars(0, output_chars(0, strings, translation, 1), translation, 12);
   output_chars(-index, output_chars(-index, strings, translation, 2), translation, 27);
   main(++index, string);
}
```

#### Compresser `output_chars` dans `main`

Ca commence à se compliquer, car il y a des appels récursifs un peu dans tous les sens et des variables qui ne servent quasiment à rien aussi. Encore une fois, je réutilise l'astuce de la variable en plus mais en faisant quelques changements pour incorporer notre fonction `output_chars` dans le `main` :

```c
char *main(int index, char *s, char *trans, int r, int t)
{
   if(index == 7)
      return 0;
   if(index == 1 && r != 1)
      main(index, strings, translation, 1, t);

   if(r > 1) {
      if(t >= 3) {
         if(*s == '/')
            return "";
         main(index, s, trans, r, -9);
         main(index, s + 1, trans, r, 3);
      }
      else if(t < 0) {
         if(*s == *trans)
            putchar(trans[26]);
         else
            main(index, s, trans + 1, r, -7);
      }
      else {
         if(index == 0)
            return s;
         if(*s == '/')
            return main(index + 1, s + 1, trans, r, 2);
         else
            return main(index, s + 1, trans, r, 1);
      }
   }

   if(r == 1) {
      main(0, main(0, s, "", 2, 1), trans, 2, 12);
      main(-index, main(-index, s, "", 2, 2), trans, 2, 27);
      main(++index, s, trans, r, t);
   }
}
```

J'ai profité de la compression pour n'utiliser `strings` et `translation` une seule fois (car je sais que je vais les remplacer plus tard par leurs contenus et donc je veux éviter d'avoir des variables). Pour le faire j'ai rajouté une condition `if(index == 1 && r != 1)` qui détermine si c'est le tout premier tour ou non.

#### Obfuscation

Maintenant la partie vraiment sympa et drôle : l'obfuscation du code. Impossible de dire en détail toutes les opérations que j'ai réalisées mais voici une liste contenant la plupart des choses :

- Toutes les conditions sont transformées en ternaires (le plus gros du travail)
- Ajout de valeurs fictives et qui ne servent à rien
- Suppression des choses inutiles (ex : `#include <stdio.h>`)
- Remplacement des variables `strings` et `translation` par leurs contenus
- Renommage de quelques variables
- Suppression des espaces/retours à la ligne
