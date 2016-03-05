#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TRAININGSIZE 100000

//outputs 0 if nobody has won, outputs 1 if X has won, outputs 2 if O has won.
int gamestatus(int *array) {
	int i, j;
	for (i = 0; i <= 2; ++i) {
		if (array[3*i] == 1 && array[3*i + 1] == 1 && array[3*i + 2] == 1) {
			return 1;
		}
		if (array[3*i] == 2 && array[3*i + 1] == 2 && array[3*i + 2] == 2) {
			return 2;
		}
	}
	for (i = 0; i <= 2; ++i) {
		if (array[i] == 1 && array[i + 3] == 1 && array[i + 6] == 1) {
			return 1;
		}
		if (array[i] == 2 && array[i+3] == 2 && array[i + 6] == 2) {
			return 2;
		}
	}
	if (array[0] == 1 && array[4] == 1 && array[8] == 1) {
		return 1;
	}
	if (array[0] == 2 && array[4] == 2 && array[8] == 2) {
		return 2;
	}
	if (array[2] == 1 && array[4] == 1 && array[6] == 1) {
		return 1;
	}
	if (array[2] == 2 && array[4] == 2 && array[6] == 2) {
		return 2;
	}
	return 0;
}


void printboard(int *array) {
	int i;
	for (i = 0; i < 9; ++i) {
		if (array[i] == 1) {
			printf("X");
		}
		if (array[i] == 0) {
			printf("_");
		}
		if (array[i] == 2) {
			printf("O");
		}
		if (i % 3 == 2) {
			printf("\n");
		}
	}
}


int main(int argc, char **argv)
{
	int gamesmatrix[TRAININGSIZE][9];
	int results[TRAININGSIZE];
	//results contains 1 if X wins, 2 if O wins, and 0 if it's a tie
	int array[9];
	int i, j;
	for (i = 0; i < TRAININGSIZE; ++i) {
		for (j = 0; j < 9; ++j) {
			gamesmatrix[i][j] = 0;
		}
	}
	for (i = 0; i < TRAININGSIZE; ++i) {
		results[i] = 3;
	}
	srand(time(NULL));

	for (j = 0; j < TRAININGSIZE; ++j) {
		for (i = 0; i < 9; ++i) {
			array[i] = 0;
		}
		int end = 0;
		int input;
		int turn = 0;
		int status = 0;
		int initial;
		while (end == 0) {
			if (turn == 9) {
				printf("The game is a tie!\n");
				results[j] = 0;
				break;
			}
		/*scaninput:
			printf("What square?\n");
			scanf("%d", &input);
			if (array[input -1] != 0) {
				printf("Not a possible move\n");
				printboard(array);
				goto scaninput;
			}

			array[input - 1] = 1;
			gamesmatrix[j][turn] = input;
			++turn;
			printboard(array);
			status = gamestatus(array);
			if (status == 1) {
				printf("X wins!\n");
				results[j] = 1;
				break;
			}
			if (status == 2) {
				printf("O wins!\n");
				results[j] = 2;
				break;
			}*/

			initial = rand() % 9;
			while (array[initial] != 0) {
				initial = rand() % 9;
			}
			//printf("Computer plays %d\n", initial + 1);
			gamesmatrix[j][turn] = initial + 1;
			array[initial] = 1;
			++turn;
			//printboard(array);
			status = gamestatus(array);
			if (status == 1) {
				//printf("X wins!\n");
				results[j] = 1;
				break;
			}
			if (status == 2) {
				//printf("O wins!\n");
				results[j] = 2;
				break;
			}	

			if (turn == 9) {
				//printf("The game is a tie!\n");
				results[j] = 0;
				break;
			}
			initial = rand() % 9;
			while (array[initial] != 0) {
				initial = rand() % 9;
			}
			//printf("Computer plays %d\n", initial + 1);
			gamesmatrix[j][turn] = initial+1;
			array[initial] = 2;
			++turn;
			//printboard(array);
			status = gamestatus(array);
			if (status == 1) {
				//printf("X wins!\n");
				results[j] = 1;
				break;
			}
			if (status == 2) {
				//printf("O wins!\n");
				results[j] = 2;
				break;
			}	
		}
	}
	for (i = 0; i < TRAININGSIZE; ++i) {
		for (j = 0; j < 9; ++j) {
			printf("%d", gamesmatrix[i][j]);
		}
		printf("\t%d\n", results[i]);
	}
}





