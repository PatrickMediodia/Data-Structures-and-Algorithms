class Account:
    def __init__(self, username, password, recipes):
        self.username = username
        self.password = password
        self.recipes = recipes
        self.right = None
    
class AccountList:
    def __init__(self):
        self.head = None
    
    def insert(self, newAccount):
        current = self.head
        
        if current is None:
            self.head = newAccount
        else:
            while current.right != None:
                current = current.right
            current.right = newAccount
    
    def getHead(self):
        return self.head

