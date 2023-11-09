class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, val):
        self.stack.append(val)
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return "\nThe stack is empty."
    
    def pop(self):
        if len(self.stack) > 0:
            return f'\nDeleted {self.stack.pop()}'
        else:
            return "\nThe stack is empty."
    
    def getStack(self):
        if len(self.stack) > 0:
            return self.stack
        else:
            return "The stack is empty."
        
newStack = Stack()

while True:
    choice = input("1 - Push\n2 - Pop\n3 - View Stack\n4 - Exit\nEnter your choice: ")
    
    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            newStack.push(num)
        except:
            print("\nValue inputted is not a number")

    elif choice == "2": print(newStack.pop())

    elif choice == "3": print(f'\n{newStack.getStack()}')

    elif choice == "4": 
        print("\nProgram has been terminated . . . . . .\n")
        exit()

    else: print("\nInvalid Input.")

    print()


