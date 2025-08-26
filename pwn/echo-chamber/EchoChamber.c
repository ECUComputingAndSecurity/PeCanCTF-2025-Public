#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *gets(char *);

int main() {
    char buf1[16] = "ccccccccccccccc";
    char buf2[16] = "bbbbbbbbbbbbbbb";
    puts("Welcome to the Echo Chamber");
    while(1==1){
	    fflush(stdout);
	    gets(buf2);
	    if(strcmp(buf1, "givemeflag") == 0){
	    	system("cat flag.txt");
	    } else{ 
	    	puts(buf2); 
	    }
    }
    return 0;
}
