#include <stdio.h>

int compare(int a, int b){
  return a == b;
}

int main(){
  int a = 0;
  int b = 0;
  int c = 0;
  printf("give out your number:");
  scanf("%d", &a);
  while (1){
    if
     ( c == 0 ){ printf("give out your number:");scanf("%d", &b);
     if
      (compare(a, b)) {printf("Found duplicate!\n");
    c = 0;}
    else {c = 1;}}
    else if
      (c == 1 ){printf("give out your number:");scanf("%d", &a);if
      (compare(a, b)) {printf("Found duplicate!\n");
    c = 1;}
    else {c = 0;}}
  }
}