#include <iostream>

using namespace std;

int main()
{
	int x = 25, y = 50, z = 75;
	int *ptr;
	
	cout << "Here are the values pf x, y, and z:\n";
	cout << x << "   " << y << "   " << z << endl;
	
	ptr = &x;
	*ptr *= 2;
	
	ptr = &y;
	*ptr *= 2;
	
	ptr = &z;
	*ptr *= 2;
	
	cout << "Once again, here are the values pf x, y, and z:\n";
	cout << x << "   " << y << "   " << z << endl;
	
	return 0;
}
