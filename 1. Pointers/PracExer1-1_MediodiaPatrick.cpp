#include <iostream>

using namespace std;

int main()
{
	char ch = 'C';
	int integer = 1;
	float real = 10.4f;
	
	cout<<"Value of character = "<<ch<< ", Address of character = "<<&ch<<endl; 
	cout<<"Value of integer = "<<integer<<", Address of integer = " <<&integer<<endl;
	cout<<"Value of real = "<<real<<", Address of real = "<<&real<<endl;
	
	return 0;
}

