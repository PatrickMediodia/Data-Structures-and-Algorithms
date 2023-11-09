import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def insertionSort(arr):
    for i in range(1, len(arr)+1):
        print("Sorted list:", arr[:i], end = "  ")
        print("Unsorted list:", arr[i:])
        if i == len(arr):
            print()
            break
        print("Item to insert:", arr[i])
        print()
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

def selectionSort(arr):
    for i in range(len(arr)):
        if i+1 == len(arr):
            break
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        print("Smallest: ", arr[min_idx])
        print(f"Swap {arr[i]} and {arr[min_idx]}")
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        
        print(i+1, arr)
        print()

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        temp = []
        print(f"{i+1} iteration")
        for value in arr:
            temp.append(value)
        for j in range(0, n-i-1):
            85, 37, 26, 74, 90, 41, 52
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
            print(arr)
        if temp == arr:
            break
        print()
# Python program for implementation of Radix Sort 
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
  
def countingSort(arr, exp1): 
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr, number): 
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    counter = 1
    while max1 / exp > 0: 
        countingSort(arr, exp)
        if counter <= number:
            print(arr)
            counter+=1
        exp *= 10

from decimal import Decimal, ROUND_HALF_UP

def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    divideby = 2
    interval = Decimal(n/divideby).quantize(0, ROUND_HALF_UP)
    while interval > 0:
        counter = 0
        print("\n\nbefore\n")
        for value in array:
            if counter == interval:
                print()
                counter = 0
            counter+=1
            print(value, end = " ")
        print()
        print("-------------------")
        interval = int(interval)
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        counter = 0
        for value in array:
            if counter == interval:
                print()
                counter = 0
            counter+=1
            print(value, end = " ")
        if interval == 1:
            break
        divideby = divideby ** 2
        interval = Decimal(n/divideby).quantize(0, ROUND_HALF_UP)
    "14, 46, 43, 27, 57, 41, 45, 21, 70"
    "85, 37, 26, 74, 90, 41, 52, 68, 15, 100"
    
def main():
    isRunning = True

    while isRunning:
        stringToBeSorted = input("Enter data to sort : ")
        
        try:
            elements = [ int(element.strip()) for element in stringToBeSorted.split(',') ]
        except: 
            print("\nElements should be numbers and seperated by a , comma as a delimiter\n")
            continue

        choice = input("\nChoose a sorting algorithm : "
                    +"\n\n[I] Insertion Sort"
                    +"\n[S] Selection Sort"
                    +"\n[B] Bubble Sort"
                    +"\n[R] Radix Sort"
                    +"\n[SS] Shell Sort"
                    +"\n\nEnter your choice : ")

        if choice.upper() == "I":
            print("\n\nInsertion Sort")
            print(f"\nBefore Sorting : \n{elements}\n")
            insertionSort(elements)
        elif choice.upper() == "S":
            print("\n\nSelection Sort")
            print(f"\nBefore Sorting : \n{elements}\n")
            selectionSort(elements)
        elif choice.upper() == "B":
            print("\n\nBubble Sort")
            print(f"\nBefore Sorting : \n{elements}\n")
            bubbleSort(elements)
        elif choice.upper() == "R":
            print("\n\nRadix Sort")
            number = int(input("\nInput maximum place value in list : "))
            radixSort(elements, number)
        elif choice.upper() == "SS":
            print("\nShell Sort\n")
            shellSort(elements, len(elements))
        else:
            print("\nInvalid Input\n")
        print(f"After Sorting: \n{elements}\n")

        while True:
            runAgain = input("Do you want to enter another data set [Y/N]? :")
            if runAgain.upper() == "Y":
                print()
                break
            elif runAgain.upper() == "N":
                isRunning = False
                break
            else:
                print("\nInvalid Input\n")
main()
