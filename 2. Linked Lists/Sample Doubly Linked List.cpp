#include <iostream>

using namespace std;

class Node
{
	public:
		string name;
		int age;
		Node *left = NULL;
		Node *right = NULL;
};


void getData(Node *&newNode)
{
	newNode = new Node();
	cout << "Enter name: ";
	cin >> newNode ->name;
	cout << "Enter age: ";
	cin >> newNode ->age;
}


void insertDataLast(Node *&head, Node *&tail, Node*&newNode)
{
	if (head == NULL)
	{
		head = newNode;
		tail = newNode;
	}
	else
	{
		tail->right = newNode;
		newNode->left = tail;
		tail = newNode;
	}			
}


void printData(Node *&head)
{
	Node *currentNode = head;
	int index = 0;
	
	while(currentNode != NULL)
	{
		cout << "\n[Name " << index+1 << "]" << endl;
		cout<< "Name: " <<currentNode->name << endl;
		cout<< "Age: " <<currentNode->age << endl;
		index++;
		
		currentNode = currentNode->right;
	}	
}


void insertNode(Node *&head, Node *&tail, Node *&newNode, int pos)
{
	if (head == NULL)
	{
		head = newNode;
		tail = newNode;
	}
	else
	{
		if(pos == 1)
		{
			head->left = newNode;
			newNode->right = head;
			head = newNode;
		}
		else
		{
			Node* prevNode = head;
			
			while(prevNode->right != NULL && pos > 2 )
			{
				prevNode = prevNode->right;
				pos--;
			}
			if (prevNode == tail)
			{
				newNode->left = prevNode;
				prevNode->right = newNode;
				tail = newNode;
			}
			else
			{
				prevNode->right->left = newNode;
				newNode->right = prevNode->right;
				prevNode->right = newNode;
				newNode->left = prevNode;
			}
		}
	}
}


void delNode(Node *&head, Node *tail, int pos)
{
	if (head == NULL)
		cout << "\nThe list is empty.\n";
	
	else
	{
		Node *nodeToDel;
		
		if (pos == 1)
		{
			nodeToDel = head;
			head = head->right;
			head->left = NULL;
			
			delete nodeToDel;
		}
		else
		{
			nodeToDel = head;
			Node *prevNode;
			
			while(nodeToDel->right != NULL && pos > 1)
			{
				prevNode = nodeToDel;
				nodeToDel = nodeToDel->right;
				pos--;
			}
			if (nodeToDel == tail)
			{
				prevNode->right = NULL;
				tail = prevNode;
				 
				delete nodeToDel;
			}
			else
			{
				nodeToDel->right->left = prevNode;
				prevNode->right = nodeToDel->right;
				
				delete nodeToDel;
			}
		}
	}
}


int main()
{
	Node *head = NULL;
	Node *tail = NULL;
	Node *newNode = NULL;
	
	getData(newNode);
	insertDataLast(head, tail, newNode);
	
	getData(newNode);
	insertDataLast(head, tail, newNode);
	
	getData(newNode);
	insertDataLast(head, tail, newNode);

	printData(head);
	
	getData(newNode);
	insertNode(head, tail, newNode, 3);
	
	delNode(head, tail, 1);
	
	printData(head);
	
	return 0;
}
