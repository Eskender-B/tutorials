#include <stdio.h>		// for printf()
#include <stdlib.h>		// for getenv()
#include <string.h>		// for strlen()
#include <stdlib.h>		// for exit(), malloc(), free()

int main (int argc, char *argv[]){

	/*
	Arguments and Environment variables
	*/

	//Name is stored in argv[0]
	printf("Name of the program: %s\n", argv[0]);
	
	//Print all of the  program's arguments
	for (int i = 1; i < argc; ++i){
		printf("Argument %d: %s\n", i, argv[i]);
	}

	//Access the envrionment variable named USER
	char* user = getenv("USER");
	printf("User of this computer: %s\n", user);

	//Before running this program in shell create an environment variable
	//$ export MY_ENV=value
	char* myEnv = getenv("MY_ENV");
	if(myEnv != NULL) printf("MY_ENV = %s\n", myEnv);



	
	/*
		- Reading and Writing to files
		- storing buffer data on stack and heap

		- Use these for stdout, stdin
			- int fputs (const char *s, FILE *stream)
			- char * fgets (char *s, int count, FILE *stream)

		- Use these for wrting reading to file
			- size_t fwrite (const void *data, size_t size, size_t count, FILE *stream)
			- size_t fread (void *data, size_t size, size_t count, FILE *stream)
	*/


	// buffer on stack
	char buffer_stack[1024];
	
	fputs("Enter line:\n", stdout);
	fgets(buffer_stack, 1024, stdin);
	
	FILE* f1 = fopen("file.txt", "w");
	fwrite(buffer_stack, 1, strlen(buffer_stack), f1); 
	fclose(f1);

	fputs("Written to file!\n", stdout);


	// buffer on heap
	char* buffer_heap = (char*) malloc(1024);


	FILE* f2 = fopen("file.txt", "r");
	fseek(f2, 0L, SEEK_END);
	size_t file_size = (size_t) ftell(f2);
	fseek(f2, 0L, SEEK_SET);

	size_t sz = fread(buffer_heap, 1, file_size, f2);
	buffer_heap[sz] = '\0';
	fputs("Recoverd from file:\n", stdout);
	fputs(buffer_heap, stdout);
	

	fclose(f2);
	free(buffer_heap);

	return 0;
}