#include <iostream>

using namespace std;

class Node
{
	public:
		string name;
		int age;
		Node *next;
};

void printlist(Node *node)
{
	while(node != NULL){
		cout<< node->name << endl;
		cout<< node->age << endl;
		node = node -> next;
	}
}

int main()
{
	Node *head = NULL;
	Node *second = NULL;
	Node *third = NULL;
	
	head = new Node();
	second = new Node();
	third = new Node();
	
	head-> name = "Patrick";
	head-> age = 19;
	head-> next = second;
	
	second-> name = "Mediodia";
	second-> age = 17;
	second-> next = third;
	
	third-> name = "Villanueva";
	third-> age = 15;
	third-> next = NULL;
	
	printlist(head);
	
	return 0;
}




