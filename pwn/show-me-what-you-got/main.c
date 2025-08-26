#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void win() {
  FILE* fp = fopen("flag.txt", "r");

  char flag[64] = {0};

  if (!fp) {
    perror("Failed to open \"flag.txt\".");
    exit(EXIT_FAILURE);
  }

  fread(flag, 1, 64, fp);
  printf("I like what you GOT! Take this: %s.\n", flag);

  exit(EXIT_SUCCESS);
}

int main() {
  uint64_t where_you_got;
  uint64_t what_you_got;

  setbuf(stdout, NULL);

  puts("Show me what you GOT!");
  scanf("%lu", &where_you_got);

  puts("Show me what you GOT! I want to see what you GOT!");
  scanf("%lu", &what_you_got);

  *(uint64_t*)where_you_got = what_you_got;

  puts("Goodbye!");
}
