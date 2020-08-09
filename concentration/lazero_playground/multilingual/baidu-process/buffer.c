#include <stdio.h>
int main()
{
    FILE * fp;
    char buffer[1024];
    fp = popen("ls -l", "r");
    // modification starts here.
    while (fgets(buffer, sizeof(buffer), fp)!=NULL){
    printf("%s", buffer);}
    pclose(fp);
}
