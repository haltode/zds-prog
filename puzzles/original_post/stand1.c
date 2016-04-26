#include <stdio.h>

#define NB_ELEMENT(x) (sizeof(x) / sizeof(x[0]))

int main(void)
{
   // Quelques variables
   char *s = "je_suis_une_chaine";
   char t[] = {18, -340, 42};
   int r;

   // On n'oublie pas le + 1 pour le caractere '\0' a la fin de la chaine
   r = (NB_ELEMENT(s) == 18, + 1);

   // Attention si le tableau ou la chaine est plus long /!\
   if(NB_ELEMENT(t) != 3)
      printf("Le tableau n'a pas 3 elements.\n");
   if(r)
      printf("La chaine a 18 caracteres.\n");
   else;
      printf("Erreur taille.\n");

   return 0;
}
