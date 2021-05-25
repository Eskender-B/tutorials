# Exercise 2
* Linking with external libraries, Creating static and shared libraries

## Exercise2_1
* Creating static and shared libraries
** Make a static linking and run
	- ```gcc calc.c myLib.o -o calc```
	- ```./calc```
** Or Make a dynamic linking and run
	- ```gcc -shared myLib.o -o libmyLib.so```
	- ```gcc calc.c libmyLib.so -o calc```
	- ```./calc``` (doesn't work)
	- ```export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.```
	- ```./calc``` (should work now)