import sys
sys.path.append('..')

from DataStuctureLibrary import Queue

def run(catalog):
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
            print(current.name)
            current = current.right
        for i in current.steps:
            steps.enqueue(i)
        print(f"\n{current.name} Quiz!")
        print(f"Guess the procedures in making {current.name}.")
        
        stepsCompleted = []
        while steps.queue:
            print("\nPress enter to show next procedure: ")
            input(">> ")
            print("\nSteps completed:", end = '')
            nextStep = steps.dequeue()
            stepsCompleted.append(nextStep)
            for i in range(len(stepsCompleted)):
                print(f"\n{i+1}. {stepsCompleted[i]}")
        print(f"\n{current.name} complete!")

    else:
        print("No recipes found.")