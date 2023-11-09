import sys
sys.path.append('..')

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

    def delete(self, deleteAccount):
        current = self.head
        nextAccount = current.right

        if current == deleteAccount:
            self.head = nextAccount
            del current
        else:
            while nextAccount != deleteAccount:
                current = current.right
                nextAccount = nextAccount.right

            if nextAccount.right == None:
                current.right = None
                del nextAccount
            else:
                current.right = nextAccount.right
                del nextAccount

    def getHead(self):
        return self.head


