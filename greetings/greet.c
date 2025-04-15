#include <stdio.h>

int main(){
  char userName[20];
  printf("What is you name? ");
  scanf("%s", userName);
  printf("Hi there, %s \n", userName);
  return(0);
} //end main