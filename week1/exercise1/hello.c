// TODO 1: Add unistd.h header for read()/write()
//	- #include <unistd.h>
#include <unistd.h>

void myScanLine(char* line){
	size_t sz;
	int found = 0;
	int cnt = 0;

	char buff[100];

	while(!found){
		/*
		// TODO 2: use read() low level function to read from standard input
			- standard input has a file descriptor of 0
			- size_t read (int fd, void* buf, size_t cnt);
		*/
		sz = read(0, buff, 100);

		for (int i = 0; i < sz; ++i)
		{
			if (buff[i] != '\n') line[cnt++] = buff[i];
			else {found = 1; break;} 
		}
		
	}
	line[cnt] = '\0';
}

void myPrintLine(char* string){
	size_t cnt = 0;
	char buff[100];
	while(string[cnt] != '\0'){
		buff[cnt] = string[cnt];
		cnt++;
	}
	buff[cnt++] = '\n';

	/* TODO 3: Use write() low level function to write to standart output
		- standard output has a file descriptor of 1
		- size_t write (int fd, void* buf, size_t cnt);

	*/
	write(1, buff, cnt);

}



int main(int argc, char const *argv[])
{

	char name[10];
	

	char prompt[] = "Name:";
	//char prompt[] = {'N', 'a', 'm', 'e', ':', '\0'};
	myPrintLine(prompt);
	myScanLine(name);
	myPrintLine(name);


	return 0;
}