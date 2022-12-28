#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>



void cut_string(char* str, char* new_str, int index)
{
	for(int i=0; i<index; i++)
	{
		new_str[i] = str[i];
	}

	char* temp=malloc(index);
	for(int i=0, j=index; i<index; i++,j++)
	{
		temp[i]=str[j];
	}
	strcpy(str, temp);
	free(temp);
}

int compare_string(char* str, char* new_str)
{
	for(int i = 0; i < strlen(new_str);i++)
	{
		for(int j = 0; j<strlen(new_str);j++)
		{
			if(str[i] == new_str[j])
			{
				return (isupper(str[i])?str[i]-'A'+27:str[i]-'a'+1);
			}


		}
	}
}

int
main(int argc, char** argv)
{
	FILE* fd;
	fd=fopen(argv[1], "r");
	char buf[256];
	char* str;
	int count=0;
	int counter=0;

	while(fgets(buf, 256, fd) != NULL)
	{
		str=calloc(strlen(buf), sizeof(char));
		strcpy(str,buf);

		char* new_str = calloc(strlen(str)/2, sizeof(char));
		cut_string(str, new_str, strlen(str)/2);

		count = count + compare_string(str,new_str);

		free(str);
		free(new_str);
	}
	printf("prio = %d\n", count);
}


