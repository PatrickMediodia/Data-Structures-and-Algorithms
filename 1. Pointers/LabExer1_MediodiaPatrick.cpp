#include <iostream>

using namespace std;

int main()
{
	int numbers[5];
	int lowest, highest;
	
	//get input from user
	cout << "Enter five numbers:\n" << endl ;
	
	for (int count = 0; count <5; count++) {
		cout << "Number[" << count+1 << "]: ";
		cin >> *(numbers + count);
	}
	
	//declare highest and lowest value to start of array
	lowest = *numbers;
	highest = *numbers;
	
	//iterate through the array contents by using pointers
	for (int count = 0; count <5; count++){
		//check if current array pointer is higher than highest variable
		if (*(numbers + count) > highest)
			highest = *(numbers + count);
					
		//check if current array pointer is lower than lowest variable
		if (*(numbers + count) < lowest)
			lowest = *(numbers + count);
	}
	
	//display lowest and highest number
	cout << "\nThe lowest out of the five numbers eneterd is " << lowest << " with the address " << &lowest << endl;
	cout << "The highest out of the five numbers eneterd is " << highest << " with the address " << &highest << endl;
	
	return 0;
}
