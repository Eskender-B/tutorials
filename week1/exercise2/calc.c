#include <stdio.h>

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


// Function to find the square-root of N
float sqrtN(int number)
{
	int start = 0, end = number;
	int mid;
	float ans;

	// To find integral part of square
	// root of number
	while (start <= end) {

		mid = (start + end) / 2;

		// If number is perfect square
		// then break
		if (mid * mid == number) {
			ans = mid;
			break;
		}

		// Increment start if integral
		// part lies on right side
		// of the mid
		if (mid * mid < number) {
			ans=start;
			//then start should be changed
			start = mid + 1;
		}

		else {
			end = mid - 1;
		}
	}

	// To find the fractional part
	// of square root upto 5 decimal
	float increment = 0.1;
	for (int i = 0; i < 5; i++) {
		while (ans * ans <= number) {
			ans += increment;
		}

		// Loop terminates,
		// when ans * ans > number
		ans = ans - increment;
		increment = increment / 10;
	}
	return ans;
}

int main (void)
{
  float x = sqrtN(5);
  printf ("The square root of 5 is %f\n", x);
  return 0;
}