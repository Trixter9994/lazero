#include <stdio.h>

int standard(int a, int b){
  int c=a+b;
  return c;
}
int main(){
  int a=1;
  int b=2;
  int s=standard(a,b);
  // return s;
  printf("%d", s);
}