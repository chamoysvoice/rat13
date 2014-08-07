#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char* rat(char* message){
  char* cyphertext = (char *)malloc(sizeof(char) * strlen(message));
  int i;

  for(i = 0; i < strlen(message); i++){
    cyphertext[i] = (isalpha(message[i])) ? (((message[i] + 13 - 'a') % 26) + 'a') : message[i];
  }
  return cyphertext;
}

int main(int argv, char** args){
  puts(rat(args[1]));
  return 0;
}

