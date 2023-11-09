#use modulo hashing to get hash key
def moduloHashFunction(hashTableSize, key):
    return key % hashTableSize

#insert into hash table and solve collision by means of linear probing
def insertIntoHashTable(hashTable, hashKey, value):
    print(f'\nInsert {value}')
    while True:
        #if index at hasKey is not None
        if hashTable[hashKey]:
            print(f"Collision between {hashTable[hashKey]} and {value} at index {hashKey}")
            hashKey+=1 
        #if it is none
        else:
            hashTable[hashKey] = value
            print(f'{value} has been inserted in index {hashKey} of the hash table')
            break 
        #if quadratic probing is to be used 
        #hashKey > len(hashtable) or hashKey < len(hashTable)?
        if hashKey == len(hashTable):
            hashKey = 0

#print index to element relation in list
def printHashTable(hashTable):
    print('\nIndex --> Element\n')
    for index, element in enumerate(hashTable):
        print(f'{index} --> {element}')
    print(f'\nHash Table : {hashTable}\n')

def main():
    #declare size of hash table
    hashTableSize = 11

    #list of values to be inserted
    values = [113, 117, 97, 100, 114, 108, 116, 105, 99]

    #list comprehension to make 11 slots in the list
    hashTable = [None for x in range(hashTableSize)]

    #values list to be inserted
    print(f'\nValues to be inserted : {values}')

    #loop to get hash key of all values and use that as hash key for hashTable list
    for value in values:
        insertIntoHashTable(hashTable, moduloHashFunction(hashTableSize, value), value)

    #printing of hashTable index to element relation
    printHashTable(hashTable)

main()