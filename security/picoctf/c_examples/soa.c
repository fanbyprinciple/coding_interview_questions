# include <stdio.h>
# define BUFSIZE 4

void win() {
    puts("If aI am printed, I am hacked !");
}

void vuln(){
    puts("Input a string and it will be printed:");
    char buf[BUFSIZE];
    gets(buf);
    puts(buf);
    fflush(stdout);
}

int main(int argc, char **argv){
    vuln();
    return 0;
}