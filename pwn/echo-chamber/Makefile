CC = gcc
CFLAGS = -fno-stack-protector -no-pie -o EchoChamber
CFILES = EchoChamber.c

.PHONY all:
all:
	$(CC) $(CFILES) $(CFLAGS)
	
.PHONY: clean
clean:
	rm EchoChamber
