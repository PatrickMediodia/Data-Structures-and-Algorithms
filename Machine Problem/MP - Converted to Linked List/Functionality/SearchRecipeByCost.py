import sys
sys.path.append('..')

from Models import CostTree

def run(recipesTree):
    while True:
        minCost = input("Enter minimum cost: ")
        if minCost.isdigit():
            minCost = int(minCost)
            break
    while True:
        maxCost = input("Enter maximum cost: ")
        if maxCost.isdigit():
            maxCost = int(maxCost)
            break
    recipesIOS = CostTree.inOrderSearch(recipesTree, minCost, maxCost)
    print(f"\nRecipes that cost between PHP{minCost} and PHP{maxCost}:")
        
    if recipesIOS:
        for i in recipesIOS:
        # Selection sort
            for k in range(len(i.recipes)):
                min_idx = k
                for j in range(k+1, len(i.recipes)):
                    if i.recipes[j] < i.recipes[min_idx]:
                        min_idx = j
                i.recipes[k], i.recipes[min_idx] = i.recipes[min_idx], i.recipes[k]

            for j in i.recipes:
                print(f"PHP{i.val} - {j}")
    else:
        print("No recipes found.")