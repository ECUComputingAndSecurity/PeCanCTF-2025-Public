CC = gcc
CFLAGS = -z norelro -no-pie -o chall
CFILES = main.c

.PHONY: all
all:
	$(CC) $(CFILES) $(CFLAGS)

.PHONY: clean
clean:
	rm chall
