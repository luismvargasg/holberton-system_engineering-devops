#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * infinite_while - Funtion to wait infinite t until someone wants to kill Z.
 *
 * Return: Always 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program that creates 5 zombie processes.
 *
 * Return: Nothing.
 */

int main(void)
{
	int n, pid;

	for (n = 0; n < 5; n++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
