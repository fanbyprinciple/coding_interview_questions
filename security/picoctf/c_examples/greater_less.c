# include <stdio.h>
int main(){
    int i;
    printf("Enter a value : ");
    scanf("%d", &i);
    if(i>5){
        printf("Greater than 5");
    } else {
        printf("Less or equal than 5\n");
    }
    return 0;
}