#include <stdio.h>
#include <stdlib.h>

char *gets(char *s);
int main(){
  char str[12];
  gets(str);
  printf("%s",str);
  return 0;
}
