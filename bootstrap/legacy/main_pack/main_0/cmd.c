#include <sys/ioctl.h>
#include <termios.h>
#include <stdio.h>
#include <stdlib.h>
// what is this?
// not working anyway. can you try something else? such as typing to yourself?
// subroutine?
// it is safe to directly detach screen.
void stackchar(char c)
{// what is this zero? -> stdin??
  if (ioctl(0, TIOCSTI, &c) < 0) {
    perror("ioctl");
    exit(1);
  }
}
int main(int argc, char *argv[])
{
  int i, j;
  char c;

  for (i = 1; i < argc; i++) {
    if (i > 1) stackchar(' ');
    for (j=0; (c = argv[i][j]); j++) {
    //   printf(c);
      stackchar(c);
    }
  }
  exit(0);
}