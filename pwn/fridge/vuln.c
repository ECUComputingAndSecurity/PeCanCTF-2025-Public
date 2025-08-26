#include <stdio.h>
#include <stdlib.h>

const char* config_filepath = "config.txt";

const char* open_message =
    "---------FridgeNet---------\n"
    "FridgeNet v0.3.7\n"
    "\n"
    "Changelog:\n"
    "- Fixed typo in welcome message\n"
    "- Fixed issue that allowed bad actors to get /bin/sh";

const char* options_message =
    "\n\nType:\n"
    "\t1\tDisplay fridge contents\n"
    "\t2\tSet fridge welcome message\n"
    "\t3\tExit\n";

void print_food() {
    puts("Food currently in fridge:");
    system("ls -m food_dir");
}

void set_welcome_message() {
    char buf[32];
    puts("New welcome message (up to 32 chars):");

    gets(buf);

    FILE* conf = fopen(config_filepath, "w");

    if (conf == NULL) {
        puts("Unable to open config file."); // This shouldn't happen
        exit(1);
    }

    fprintf(conf, "welcome_msg: %s", buf);
    fclose(conf);
}

int main() {
    puts(open_message);

    while (1) {
        puts(options_message);
        printf("> ");
        fflush(stdout);

        char choice = getchar();
        while (getchar() != '\n');

        switch (choice) {
            case '1':
                print_food();
                break;
            case '2':
                set_welcome_message();
                break;
            case '3':
                puts("Bye!");
                return 0;
            default:
                puts("Invalid option.");
                break;
        }
    }


    return 0;
}
