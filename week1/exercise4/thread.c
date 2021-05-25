#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int global_var = 111;

int factorial(int n){
	if(n==1) return 1;

	return n * factorial(n-1);
}

void* threadFunc(void *arg){

	printf("In thread: \n");
	int res = factorial(5);		// Do some work
	printf("\t5!=%d\n", res);
	global_var *= 3;
	printf("\tChanged Global variable: global_var=%d\n", global_var);

	return NULL;
}


int main(int argc, char *argv[]){

	printf("Initial global_var=%d\n", global_var);

	pthread_t t1;

	int s;
	s = pthread_create(&t1, NULL, threadFunc, NULL);
	if (s != 0){
		printf("Error: pthread_create()\n");
		exit(1);
	}


	printf("In parent process: \n");
	int res = factorial(10);		// Do some work
	printf("\t10!=%d\n", res);


	s = pthread_join(t1, NULL);
	if (s != 0){
		printf("Error: pthread_join()\n");
		exit(1);
	}

	printf("Final global_var=%d\n", global_var);

	return 0;
}