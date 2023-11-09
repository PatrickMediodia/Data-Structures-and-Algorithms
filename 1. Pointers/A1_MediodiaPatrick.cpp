#include <iostream>

using namespace std;

//using pointers as parameters to use for arithmetic swap of two nubmer values
int swapValue(int* ptr1, int* ptr2){
	*ptr1 = *ptr1 + *ptr2;
	*ptr2 = *ptr1 - *ptr2;
	*ptr1 = *ptr1 - *ptr2;
}

int main()
{
	int num1, num2;
	
	cout << "Enter value for first number: ";
	cin >> num1;
	
	cout << "Enter value for second number: ";
	cin >> num2;
	
	cout << "\nValues before swaping the two numbers: \n" << endl;
	cout << "First number: " << num1 << endl;
	cout << "Second number: " << num2 << endl;
	
	//num1 and num2 address-of as arguments
	swapValue(&num1,&num2);
	
	cout << "\nValues after swaping the two numbers: \n" << endl;
	cout << "First number: " << num1 << endl;
	cout << "Second number: " << num2 << endl;
}







