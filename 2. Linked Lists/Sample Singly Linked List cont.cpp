#include <iostream>

using namespace std;

class Node
{
	public:
		string studName;
		int testScore;
		Node *next;
};

//print average test score
void viewAvgTestScore(double testScoreAvg, int index)
{
	if (testScoreAvg != 0 && index !=0)
	{
		testScoreAvg /= index;
		cout << "\nTest Score Average: " << testScoreAvg << "\n";	
	}
}

//print linked list data
void printlist(Node *node)
{
	double testScoreAvg = 0, index = 0;
	
	if (node == NULL)
		cout << "\nThe list is empty\n";
		
	while(node != NULL)
	{
		cout<< "\nStudent Name: " <<node->studName << endl;
		cout<< "Test Score: "<< node->testScore << endl;
		
		testScoreAvg += node->testScore;
		index++;
		
		node = node -> next;
	}
	viewAvgTestScore(testScoreAvg,index);
	
	cout << "\n";
}

//get data from user
void getData(Node *&node)
{
	node = new Node();
	
	cout << "\nEnter Student Name: ";
	cin >> node->studName;
	
	cout << "Enter Test Score: ";
	cin >> node->testScore;
	
	node->next = NULL;
}

//insert at start of list
void insertStart(Node *&node, Node *&head)
{
	if (head == NULL)
		head = node;
	else
	{
		node->next = head;
		head = node;
	}
}

//insert at last position of list
void insertEnd(Node *&node, Node *&head)
{
	if (head == NULL)
		head = node;
	else
	{
		Node *lastNode = head;
		
		while (lastNode->next != NULL)
			lastNode = lastNode->next;
			
		lastNode->next = node;
	}
}

//insert node at any position in list
void insert(Node *&node, Node *&head, int pos)
{
	if (head ==NULL)
		head = node;
	else
	{
		if (pos==1){
			node-> next = head;
			head = node;
		}
		else
		{
			Node *prevNode = head;
			while( prevNode -> next != NULL && pos > 2)
			{
				prevNode = prevNode -> next;
				pos--;
			}
			node->next = prevNode-> next;
			prevNode->next = node;
		}		
	} 
}

//delete at beginning of the list
void delNodeStart(Node *&head)
{
	if (head == NULL)
		cout << "The list is empty";
	else
	{
		Node *nodeToDel = head;
		head = head->next;
		delete nodeToDel;
	}
}

//delete at the end of the list
void delNodeEnd(Node *&head)
{
	if (head == NULL)
		cout << "\nThe list is empty\n";
	else
	{
		Node *nodeToDel = head;
		Node *prevNode;
		while (nodeToDel->next != NULL)
		{
			prevNode = nodeToDel;
			nodeToDel = nodeToDel->next;
		}
		if (nodeToDel == head)
			head = NULL;
		else
			prevNode->next = NULL;
		
		delete nodeToDel;
	}
}

//delete any node in the list using position
void delNode(Node *&head, int pos)
{
	if (head == NULL)
		cout << "\nThe list is empty\n";
	else
	{
		Node *nodeToDel;
		if (pos == 1)
		{
			nodeToDel = head;
			head = head->next;
		}
		else
		{
			nodeToDel = head;
			Node *prevNode;
			
			while (nodeToDel != NULL && pos > 1)
			{
				prevNode = nodeToDel;
				nodeToDel = nodeToDel->next;
				pos--;
			}
			if (nodeToDel == head)
			{
				cout <<"Not Found";
				return;
			}				
			else
				prevNode->next = nodeToDel->next;
		}
		delete nodeToDel;
	}
}

int main()
{
	Node *head = NULL;
	Node *newNode = NULL;
	
	char choice, selection;
	int pos; 
	bool running = true;
	
	while(running)
	{
		
		cout << "Singly Linked List Operations Menu\n" << "1. Insert at the beginning\n" << "2. Insert at the end\n";
		cout << "3. Insert at a given position\n" << "4. Delete head\n" << "5. Delete Tail (last node)\n";
		cout << "6. Delete node at given position\n" << "7. Exit\n" << "\nChoice: "; 
		cin >> selection;
		
		switch(selection)
		{
			case '1': 
				getData(newNode);
				insertStart(newNode, head); break;
				
			case '2':
				getData(newNode);
				insertEnd(newNode, head); break;
			
			case '3':
				getData(newNode);
				cout << "Enter position that you want to insert the data entered: ";
				cin >> pos;
				insert(newNode, head, pos); break;		
				
			case '4':
				delNodeStart(head); break;
				
			case '5':
				delNodeEnd(head); break;
			
			case '6':
				cout << "Enter position that you want to delete: ";
				cin >> pos;
				delNode(head, pos); break;
							
			case '7':
				running = false;
				break;
				
			default:
				cout << "\nInvalid Value Entered\n";
		}
	
		cout << "\nCurrent contents of the list:\n";
		printlist(head);

		cout << "\n";
	}

	return 0;
}




