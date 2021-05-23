// TODO 1: Add stdio library
//	- #include <stdio.h>
#include <stdio.h>



int main(int argc, char const *argv[])
{
	/* TODO 2:
	1. Read from standard input
		- char name[10];
		- printf("Name: ");
		- scanf("%s", name);
	2. Print to standard output 
		- printf("Hello %s\n", name);
	*/

	char name[10];
	printf("Name: ");
	scanf("%s", name);
	printf("Hello %s\n", name);

	return 0;
}