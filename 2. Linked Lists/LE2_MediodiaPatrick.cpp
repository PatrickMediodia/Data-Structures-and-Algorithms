#include <iostream>
#include <limits>

using namespace std;


/*
The program must:

have an array to hold the correct answers. +
Allows user to input the student’s answers. +
Display a message if the student passed or failed the exam with the corresponding score. It is required that the student should get 15 correct answers out of the 25 questions. + 
Display the total number of questions correctly answered and the total number of questions incorrectly answered. +
must record the name of the student and his/her final score in a singly linked list. +
Ask the user if he/she would like to delete last record or to chose a record to be deleted from the linked list. +
Display the name of the students who takes the exam with final score, and count how many of the student passed or failed in the exam. +
*/

class Node
{
	public:
		string studName;
		int score; 
		Node *next;
};


bool checkAnswer(char answer, int index)
{
	//correct answer char array
	char correctAnswer[25] = {  'D' , 'C' , 'D' , 'D', 'A'
						  	    ,'B' , 'C' , 'A' , 'B', 'B'
						  	    ,'C' , 'D' , 'A' , 'B', 'C'
						  	    ,'D' , 'D' , 'A' , 'B', 'A'
						  	    ,'A' , 'B' , 'D' , 'A', 'C' };
	
	//return if answer is correct
	if (answer == correctAnswer[index])
		return true;
	return false;						
}


int getAnswers()
{
	int score;
	string answer;
	
	//loop while getting input
	for(int i = 0; i <25; i++)
	{
		while (true)
		{
			cout << "Enter answer " << "[" << i+1 <<"] : ";
			cin >> answer;
			
			//check if string entered is digit or longer than 1 in length
			if (answer.length()!=1 || isdigit(answer[0]))
			{
				cout << "\nInvalid Input, Please enter a character.\n" << endl;
				continue;
			}	
			
			//if it is equal to one and length and is not a digit therefore it is valid
			char charAns = answer[0];
			
			//uppercase for validation
			charAns = toupper(charAns);
				
			//check if charAns is either A, B, C or D
			if (charAns == 'A'|| charAns == 'B' || charAns == 'C'|| charAns == 'D')
			{
				//check using checkAnswer function
				if (checkAnswer(charAns, i)) 
					score++;
				break;
			}
			else
			{
				cout << "\nInvalid Input, Please enter a either A, B, C or D.\n" << endl;
			}
		}
	}
	return score;
}


void showResult(Node *&node)
{
	string msg;
	
	if (node->score >= 15)
		msg = " has passed the exam with the score ";
	else
		msg = " has failed the exam with the score ";
	
	cout << endl << "Result:" << endl;
	cout << endl << node->studName << msg << node->score << endl;
	cout << "Correct Answers: " << node->score << endl;
	cout << "Wrong Answers: " << 25 - node->score << endl;
}


void getData(Node *&node)
{
	node = new Node();
	
	cout << "\nEnter your name: ";
	cin >> node->studName;
	
	cout << "\nPlease Enter your answers:\n\n";
	node->score = getAnswers();
	
	node->next = NULL;
}


void insertData(Node *&node, Node *&head)
{
	Node *list = head;
	
	if (head == NULL)
	{
		head = node;
	}
	else
	{
		while (list->next != NULL)
		{
			list = list->next;
		}
		list->next = node;
	}
}


void deleteLast(Node *&head)
{
	Node *currentNode = head;
	Node *prevNode;
	
	if (head == NULL)
		cout << "\nThe list is empty\n";
	else
	{
		while(currentNode->next != NULL)
		{
			prevNode = currentNode;
			currentNode = currentNode->next;	
		}
		if (currentNode == head)
			head = NULL;
		else
			prevNode->next = NULL;
		
		delete currentNode;
	}
}


void deleteData(Node *&head, int pos)
{	//check if head is null
	if (head != NULL)
	{
		Node *currentNode = head;
		
		//check if position is in start
		if (pos == 1)
		{
			if (currentNode->next == NULL)
				head = NULL;
			else
				head = currentNode->next;
				
			delete currentNode;
		}
		else
		{
			Node *currentNode = head;
			
			//traverse until one node before node to be deleted
			while(currentNode->next != NULL && pos > 2)
			{
				currentNode = currentNode->next;
				pos--;
			}
			
			//prevNode is currentNode
			Node *prevNode = currentNode;
			//deleteNode is the node we want to delete, this is after prevMode
			Node *deleteNode = currentNode->next;
			Node *nextNode;
			
			//check if pointer field of node to be deleted is not null
			if (deleteNode->next != NULL)
			{
				nextNode = deleteNode->next;
				prevNode->next = nextNode;
			}
			//if it is null then prevNode pointer field is set to null
			else
				prevNode->next = NULL;
						
			delete deleteNode;
	 	}	
	}
	else
		cout << "\nThe list is empty.\n";
}


void printData(Node *&head)
{
	Node *currentNode = head;
	int index = 0, passed = 0;
	
	if (currentNode == NULL)
		cout << "\nThe list is empty.\n";
	
	while (currentNode != NULL)
	{
		cout << "\n[Student " << index+1 << "]" << endl;
		cout<< "Student Name: " <<currentNode->studName << endl;
		cout<< "Test Score: "<< currentNode->score << endl;
		
		index++;
		
		if (currentNode->score >=15)
			passed++;
				
		currentNode = currentNode->next;
	}
	
	cout << "\nNumber of students that passed: " << passed << endl;
	cout << "Number of students that failed: " << index-passed << endl;
}


int main()
{
	Node *head = NULL;
	Node *newNode = NULL;
	bool running = true;
	char choice, selection;
	int pos;
	
	cout << "This program will ask for name and answers of a student and will return the results if they have passed the exam." << endl;
	
	while (running)
	{
		cout << "\nMenu:\n" << "1. Input Student Answers\n2. View Result list\n3. Delete Record\n4. Exit\n\nChoice: ";
		cin >> selection;
		
		switch(selection)
		{
			case '1':
				getData(newNode);
				insertData(newNode, head);
				showResult(newNode);
				break;
			
			case '2':
				printData(head);
				break;
			
			case '3':
				while(true)
				{
					cout << "\nDo you want to delete data at a specific position or delete the last data entered?\n";
					cout << "Choices: Specific position [P] or Last data entered [L]\n\nChoice: ";
					cin >> choice;
					choice = toupper(choice);
					
					if (choice == 'P')
					{
						printData(head); 
						cout << "\nEnter position that you want to delete: ";
						cin >> pos;
						
						deleteData(head,pos);
						break;
					}
					else if (choice == 'L')
					{
						deleteLast(head);
						break;
					}
					else
						cout << "\nInvalid Input\n";
				} break;
			
			case '4':
				running = false;
				break;
		}
	}
	return 0;
}


