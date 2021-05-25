#include <stdio.h>
#include <unistd.h>	// for fork(), sleep()
#include <stdlib.h> // for exit()

int global_var = 111;


int factorial(int n){
	if(n==1) return 1;

	return n * factorial(n-1);
}


int main(int argc, char *argv[])
{

	pid_t childPid;
	int res;

	printf("Initial global_var=%d\n", global_var);

	switch (childPid = fork()) {
		
		case -1:
			printf("Error in fork()\n");
			exit(1);

		case 0:			// In child process

			printf("In child process: \n");
			res = factorial(5);		// Do some work
			printf("\t5!=%d\n", res);
			global_var *= 3;
			printf("\tChanged Global variable: global_var=%d\n", global_var);
			break;


		default:		// In parent process

			printf("In parent process: \n");
			res = factorial(10);		// Do some work
			printf("\t10!=%d\n", res);
			sleep(3);	// Make sure child finishes before parent
			break;
	}
	/* Give child a chance to execute */
	/* Both parent and child come here */

	if (childPid==0)
		printf("Child: global_var=%d\n", global_var);
	else
		printf("Parent: global_var=%d\n", global_var);

	return 0;
}