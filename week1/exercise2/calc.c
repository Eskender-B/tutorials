#include <stdio.h>
#include "myLib.h"

/*
TODO: Create a library and add function sqrtN into your library
	- Create header file: myLib.h
	- Create source file: myLib.c and add sqrtN 
	- Include header file here: #include "myLib.h"
	- Create object file
		-$ gcc -c myLib.c -o myLib.o
	- Make a static linking and run
		-$ gcc calc.c myLib.o -o calc
		-$ ./calc
	- or Make a dynamic linking and run
		-$ gcc -shared myLib.o -o libmyLib.so
		-$ gcc calc.c libmyLib.so -o calc
		-$ ./calc (doesn't work)
		-$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
		-$ ./calc (should work now)
*/



int main (void)
{
  float x = sqrtN(5);
  printf ("The square root of 5 is %f\n", x);
  return 0;
}