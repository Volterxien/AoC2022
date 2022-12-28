#include <stdio.h>
#include <string.h>

int
main(int argc, char** argv)
{
	FILE* fd;
	fd = fopen(argv[1], "r");
	char buf[256];
	char c1,c2,c3,c4;
	unsigned int score=0;
	unsigned int arr1[3][3]={{4,8,3}, {1,5,9},{7,2,6}};
	unsigned int arr2[3][3]={{3,4,8},{1,5,9},{2,6,7}};

	while(fgets(buf, 256, fd) != NULL)
	{
		
		sscanf(buf,"%c%c%c%c", &c1,&c2,&c3,&c4);
		if(c1=='\n')
			break;
		if(strcmp(argv[2], "1")==0)
		{
			score=score+arr1[c1-'A'][c3-'X'];
		}
		if(strcmp(argv[2], "2")==0)
		{
			score=score+arr2[c1-'A'][c3-'X'];	
		}

	}
	printf("score: %u\n", score);
}

