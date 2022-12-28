#include <stdio.h>

int
main(int argc, char** argv)
{
	FILE* fd;
	char buf[256];
	unsigned int cal1=0;
	unsigned int cal2=0;
	unsigned int cal3=0;
	unsigned int tempcal=0;

	fd=fopen(argv[1], "r");
	while(fgets(buf, 256, fd)!=NULL)
	{
		if(buf[0] == '\n')
		{
			if(tempcal>cal1)
			{
				cal3=cal2;
				cal2=cal1;
				cal1=tempcal;

			}
			else if(tempcal>cal2)
			{
				cal3=cal2;
				cal2=tempcal;
			}
			else if(tempcal>cal3)
			{	
				cal3=tempcal;
			}
			tempcal=0;
		}

		unsigned int temp=0;	
		for(int i = 0; buf[i] != '\n' && buf[i] != '\0'; i++)
		{
			temp=temp*10 + buf[i]-'0';
		}
		tempcal=tempcal+temp;


	}
	printf("cal1 %u, cal2 %u, cal3 %u\n", cal1, cal2, cal3);
	printf("cal: %u\n", cal1+cal2+cal3);
}









