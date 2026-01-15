# include <stdio.h>
int main(){
	int fahr, celcius;
	int step, lower, upper;

	step = 20;
	lower = 0;
	upper = 300;
	fahr = lower;
	while(fahr <= upper){
		celcius = 5*(fahr-32)/9;
		printf("%3d %6d\n",fahr,celcius);
		fahr = fahr + step;
	}
	return 0;
}
