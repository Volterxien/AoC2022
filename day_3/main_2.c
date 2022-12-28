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

int compare_string(char* str, char* new_str,char* string_3)
{
	for(int i = 0; i < strlen(str);i++)
	{
		for(int j = 0; j<strlen(new_str);j++)
		{
			if(str[i] == new_str[j])
			{
				for(int z=0; z<strlen(string_3);z++)
				{
					if(new_str[j]==string_3[z])
					{
						return (isupper(str[i])?str[i]-'A'+27:str[i]-'a'+1);
					}
				}
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
	char* str[3];
	int count=0;
	int counter=0;

	while(fgets(buf, 256, fd) != NULL)
	{

		str[counter]=calloc(strlen(buf), sizeof(char));
		strcpy(str[counter],buf);

//		cut_string(str, new_str, strlen(str)/2);


		counter++;
		if(counter%3==0)
		{
			count = count + compare_string(str[0], str[1], str[2]);
			free(str[0]);
			free(str[1]);
			free(str[2]);
			counter=0;
		}
	}
	printf("prio = %d\n", count);
}


