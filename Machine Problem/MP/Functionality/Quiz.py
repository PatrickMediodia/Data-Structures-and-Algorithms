import sys
sys.path.append('..')

from DataStuctureLibrary import Queue

def run(catalog):
    recipes = catalog.getRecipes()
    if len(recipes) > 0:
        for i in range(len(recipes)):
            print(f"{i+1}. {recipes[i].name}")
        choice = None
        recipeIdx = None
        while True:
            choice = input(">> ")
            if choice.isdigit():
                recipeIdx = int(choice)-1
                if recipeIdx in range(len(recipes)):
                    break
        steps = Queue.Queue()
        for i in recipes[recipeIdx].steps:
            steps.enqueue(i)
        print(f"\n{recipes[recipeIdx].name} Quiz!")
        print(f"Guess the procedures in making {recipes[recipeIdx].name}.")
        stepsCompleted = []
        while steps.queue:
            print("\nPress enter to show next procedure: ")
            input(">> ")
            print("\nSteps completed:", end = '')
            nextStep = steps.dequeue()
            stepsCompleted.append(nextStep)
            for i in range(len(stepsCompleted)):
                print(f"\n{i+1}. {stepsCompleted[i]}")
        print(f"\n{recipes[recipeIdx].name} complete!")
    else:
        print("No recipes found.")