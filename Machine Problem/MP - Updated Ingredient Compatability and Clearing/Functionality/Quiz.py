import sys
sys.path.append('..')

from DataStuctureLibrary import Queue
from Models import Recipe
from Functionality import Validation as valid 

def run(common, personal):
    catalog = Recipe.RecipeList()
    catalog.head = Recipe.merge(common, personal)
    if catalog:
        i = 0
        current = catalog.head
        while current:
            print(f"{i+1}. {current.name}")
            current = current.right
            i += 1
        length = i
        choice = None
        recipeIdx = None
        while True:
            choice = input(">> ")
            if choice.isdigit():
                recipeIdx = int(choice)-1
                if recipeIdx in range(length):
                    break
        
        steps = Queue.Queue()
        current = catalog.head
        for i in range(recipeIdx):
            current = current.right
        for i in current.steps:
            steps.enqueue(i)
        valid.clear_console()

        print("\n\t\t\t\t*~*~*~ Quiz ~*~*~*\n")
        print(f"{current.name} Quiz!")
        print(f"\nGuess the procedures in making {current.name}.")
        
        stepsCompleted = []
        while steps.queue:
            print("\nPress enter to show next procedure: ")
            input(">> ")
            print("\nSteps completed:", end = '')
            nextStep = steps.dequeue()
            stepsCompleted.append(nextStep)
            for i in range(len(stepsCompleted)):
                print(f"\n{i+1}. {stepsCompleted[i]}")
        print(f"\n\n{current.name} complete!\n")
        valid.clear_console_keypress()
    else:
        print("\n\nNo recipes found.\n")