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
