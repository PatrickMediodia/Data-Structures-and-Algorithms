#include <iostream>

using namespace std;

int main()
{
	int numbers[5];
	
	cout << "Enter five numbers: ";
	for (int count = 0; count <5; count++)
		cin >> *(numbers + count);
	
	cout << "Here are the numbers you entered:\n";
	for (int count = 0; count <5; count++) 
		cout << *(numbers + count)<< " ";
	
	cout << endl;
	
	return 0;
}
