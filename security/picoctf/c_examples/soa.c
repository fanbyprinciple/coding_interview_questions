# include <stdio.h>
# define BUFSIZE 4

//0x555555555189
void win() {
    puts("If aI am printed, I am hacked !");
}

void vuln(){
    puts("Input a string and it will be printed:");
    char buf[BUFSIZE]; //stack
    gets(buf); //0x00000000000011c4
    /* 
     0x00000000000011c9 <+41>:    lea    -0x4(%rbp),%rax
     0x00000000000011cd <+45>:    mov    %rax,%rdi
    */
    puts(buf);
    fflush(stdout);
}

int main(int argc, char **argv){
    vuln();
    return 0;
}