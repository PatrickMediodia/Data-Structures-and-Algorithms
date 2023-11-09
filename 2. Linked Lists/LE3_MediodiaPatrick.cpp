#include <iostream>

using namespace std;


class Player
{
	public:
		string name;
		int score;
		Player *left = NULL;
		Player *right = NULL;
};


//check if name entered by user is already in list
string validateName(Player *&head)
{
	string name;
	
	while(true)
	{
		Player *currentPlayer = head;
		
		cout << "\nEnter player name: ";
		cin >> name;
		
		while(currentPlayer != NULL)
		{
			if(currentPlayer->name == name)
			{
				cout << "\nPlayer name already exists in the list, Please enter a different name.\n";
				break;
			}
			currentPlayer = currentPlayer->right;
		}
		if (currentPlayer == NULL) break;
	}
	return name;
}


//get data such as name and score
void getPlayerData(Player *&newPlayer, Player *&head)
{
	newPlayer = new Player();
	
	newPlayer->name = validateName(head);
	
	cout << "\nEnter score: "; 
	cin >> newPlayer->score;
	
	newPlayer->left = NULL;
	newPlayer->right = NULL;	
}


//create a new player node and then set the nodes fields to the updated player data
string getUpdatedPlayerData(Player *&newPlayer, Player *&head)
{
	newPlayer = new Player();
	char choice;
	int score;
	
	string name;
	
	cout << "\nEnter name of player that you want to update : ";
	cin >> name;
		
	Player *currentPlayer = head;
	
	while(currentPlayer->name != name )
	{
		if (currentPlayer->right == NULL) 
		{ currentPlayer = NULL; break; }
		
		currentPlayer = currentPlayer->right;
	}
	
	//check if current player is null, if true then no player with that name in the list
	if (currentPlayer == NULL)
		return "";
	
	else
	{
		while (true)
		{
			cout << "\nDo you want to change the player name or player score? [N - name / S - score]\nChoice : ";
			cin >> choice;
			if (toupper(choice) == 'N')
			{
				newPlayer->name = validateName(head); 
				newPlayer->score = currentPlayer->score;
				break;
			}
			else if (toupper(choice) == 'S')
			{
				cout << "\nEnter updated score : ";
				cin >> score;
				newPlayer->name = currentPlayer->name;
				newPlayer->score = score;
				break;
			}
			else
				cout << "\nInvalid Input.\n";
		}		
	}

	newPlayer->left = NULL;
	newPlayer->right = NULL;	
	
	//return name to be deleted
	return currentPlayer->name;
}


//insert data entered by player
void insertPlayerData(Player *&head, Player *&tail, Player *&newPlayer)
{
	if (head == NULL)
	{
		head = newPlayer;
		tail = newPlayer;
	}
	else
	{
		Player *currentPlayer = head;
		Player *prevPlayer;
		
		//compare score value to list 
		while(currentPlayer->score < newPlayer->score)
		{		
			prevPlayer = currentPlayer;
			
			if (currentPlayer->right == NULL) 
			{ currentPlayer = NULL; break; }
			
			currentPlayer = currentPlayer->right;
		}
			
		//insert score at end
		
		//the condition is depending on your approach when you need to insert at the end of the list
		//you can check current node pointed to by tail and check if new node value is greater.
		//in my apprauch i tranversed through the list checking where it should be placed and if it is greater than all other nodes
		if (currentPlayer == NULL)
		{
			newPlayer->left = tail; // 1.) set new node's previous or left field to current node pointed to by tail
			tail->right = newPlayer; // 2.) set current node pointed to by tail's next pointer to new player
			tail = newPlayer; //3.) set tail to new player
		}
			
		//insert score at start
		else if (currentPlayer == head)
		{
			newPlayer->right = currentPlayer;
			currentPlayer->left = newPlayer;
			head = newPlayer;
		}
			
		//insert score depending on value
		else
		{
			//connect new node to previous and current node
			newPlayer->left = prevPlayer;
			newPlayer->right = currentPlayer;
			
			//connect previous and current node to new node			
			currentPlayer->left = newPlayer;
			prevPlayer->right = newPlayer;
		}
	}
}


//delete data depending on the name entered by user
bool deletePlayerData(Player *&head, Player *&tail, string name)
{
	Player *currentPlayer = head;
	
	while(currentPlayer->name != name )
	{
		if (currentPlayer->right == NULL) 
		{ currentPlayer = NULL; break; }
		
		currentPlayer = currentPlayer->right;
	}
	
	//check if current player is null, if true then no player with that name in the list
	if (currentPlayer == NULL)
	{
		cout << "\nNo player with that name in players list.\n";
		return false;
	}	
	else
	{
		//check if currentplayer is equal to head
		//delete first node
		if (currentPlayer == head)
		{	
			//special case if only 1 node in the list
			if (head == tail)
			{
				head = NULL;
				tail = NULL;
			}
			//if more than 1 node in the list
			else
			{
				head = head->right;
				head->left = NULL;
			}
		}
		//delete last node in the list
		else if (currentPlayer->right == NULL)
		{
			currentPlayer->left->right = NULL;
			tail = currentPlayer->left;
		}
		//delete node in the middle
		else
		{
			currentPlayer->left->right = currentPlayer->right;
			currentPlayer->right->left = currentPlayer->left;
		}
		
		delete currentPlayer;
	}
	return true;
}


//view player data, either ascending or descending order
bool viewPlayerData(Player *&startingPoint, Player *&head, Player *&tail)
{
	Player *currentPlayer = startingPoint;
	
	int index = 1;
	
	if (currentPlayer == NULL)
	{
		cout << "\nPlayer list is empty.\n";
		return false;
	}
	else
	{
		while (currentPlayer != NULL)
		{
			cout << "\n[Player " << index << "]" << endl;
			cout<< "Name : " <<currentPlayer->name << endl;
			cout<< "Score : "<< currentPlayer->score << endl;
			index++;
			
			if (startingPoint == head)
				currentPlayer = currentPlayer->right;
			else
				currentPlayer = currentPlayer->left;
		}
	}
	return true;
}


//choose between ascending and descending order
bool viewPlayerDataChoice(Player *&head, Player *&tail)
{
	char choice;
	
	while(true)
	{
		cout << "\nDo you want to view data in ascending or descending order? [A - Ascending / D - Descending]\nChoice : ";
		cin >> choice;
					
		if (toupper(choice) == 'A')
		{
			cout << "\nShowing scores in ascending order (lowest to highest)\n";
			return viewPlayerData(head, head, tail); 
		}
		else if (toupper(choice) == 'D')
		{
			cout << "\nShowing scores in descending order (highest to lowest)\n";
			return viewPlayerData(tail, head, tail);
		}
		else
			cout << "\nInvalid Input\n";
	}
}


//print player names with score entered by user
void searchPlayerScore(Player *&head, int score)
{
	Player *currentPlayer = head;
	int index = 0;
	
	if (head == NULL)
		cout << "\nPlayer list is empty.\n";
	else
	{
		cout << "\nPlayers with a score of " << score << endl;
		
		//traverse through list checking 1 by 1 if currentPlayer score is equal to score
		while(currentPlayer != NULL)
		{
			
			if(currentPlayer->score == score)
			{
				cout << "\n[Player " << index+1 << "]" << endl;
				cout<< "Name : " <<currentPlayer->name << endl;
				cout<< "Score : "<< currentPlayer->score << endl;
				index++;
			}
			
			if (currentPlayer->right == NULL) 
			{ currentPlayer = NULL; break; }
			
			currentPlayer = currentPlayer->right;
		}
		
		if (index == 0)
			cout << "\nNo players equal to the score inputted.\n";
	}
}


int main()
{
	Player *head = NULL;
	Player *tail = NULL;
	Player *newPlayer = NULL;
	
	bool running = true;
	char choice, selection;
	int pos, score;
	string name;
	
	cout << "This program stores a list of scores in order, you can input a new player record, view player records and delete a player record." << endl;
	
	while(running)
	{
		cout << "\nMain Menu:\n" << "1. Input new player record\n2. View scores\n3. Search for a score\n4. Update player details\n5. Delete player record\n6. Exit\n\nChoice: ";
		cin >> selection;
	
		switch(selection)
		{
			case '1':
				getPlayerData(newPlayer, head);
				insertPlayerData(head, tail, newPlayer);
				break;
			
			case '2':
				viewPlayerDataChoice(head,tail);
				break;
				
			case '3':
				cout << "\nEnter the score you want to search for\nScore : ";
				cin >> score;
				searchPlayerScore(head, score);
				break;
				
			
			case '4':
				if(viewPlayerDataChoice(head,tail))
				{
					if (deletePlayerData(head, tail, getUpdatedPlayerData(newPlayer, head)))
					insertPlayerData(head, tail, newPlayer);
				}
				break;
				
			case '5':
				if(viewPlayerDataChoice(head,tail))
				{
					cout << "\nEnter the name of players score you want to delete\n(Note: Player names are case sensitive)\n\nName : ";
					cin >> name;
					deletePlayerData(head, tail, name);
				} 
				break;
				
			case '6':
				running = false; break;
				
			default:
				cout << "\nInvalid Input\n";
		}
	}
	return 0;
}
