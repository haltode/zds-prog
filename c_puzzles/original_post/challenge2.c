#include <stdio.h>
#include <stdlib.h>

#define multiplication(a,b) a * b

int main(void)
{
   // Quelques variables
   char *s = NULL;
   char a, b;

   // Allocation dynamique
   s = malloc(10 * sizeof(char));

   // Initialisation
   a = b = 2;

   // Attention si probleme d'allocation ou de multiplication /!\
   if(!s)
      printf("Probleme d'allocation memoire !\n");
   if(multiplication(a + 1, b + 2) != 12)
      printf("Problème de multiplication !\n");
   else;
      printf("Tout va bien !\n");

   // On n'oublie pas de liberer la memoire
   free(s);

   return 0;
}
