class Student:
    def __init__(self, studNum, studName, program, age, grade):
        self.studNum = studNum
        self.studName = studName
        self.program = program
        self.age = age
        self.grade = grade


def getValidString(label):
    while True:
        validString = input(f"Enter {label} : ")
        if len(validString) > 0:
            break
        print(f"\n{label.capitalize()} must not be empty\n")

    return validString


def getValidNumber(label):
    while True:
        validNumber = input(f"Enter {label} : ")
        if validNumber.isdigit(): 
            break
        print(f"\n{label.capitalize()} must numerical\n")

    return validNumber


def noDupilicateStudNum(studentList):
    while True:
        isValid = True
        studNum = getValidNumber("student number")
        for student in studentList:
            if student.studNum == studNum:
                print("\nStudent Number is already in list\n")
                isValid = False
        if isValid == True:
            break
    return studNum


def addStudent(studentList):
    print() #for formatting only
    studNum = noDupilicateStudNum(studentList)
    studName = getValidString("student name")
    program = getValidString("program")
    age = getValidNumber("age")
    grade = getValidNumber("grade")

    print("\nStudent has been added to the list\n")

    return Student(studNum, studName, program, age, grade)


def deleteStudent(studentList):
    deleteBy = input("\nDelete by\n"
                    +"\nA - Student Number"
                    +"\nB - Student Name"
                    +"\n\nEnter your choice : ").upper()
    
    deleteByLabel = {
        "A" : "student number",
        "B" : "student name"
    }

    if deleteBy != "A" and deleteBy != "B":
        print("\nInvalid Input\n")
        return

    studInfo = input(f"\nEnter {deleteByLabel[deleteBy]} to be deleted : ")
    deleteStudent = False

    for student in studentList:
        if deleteBy == "A":
            if student.studNum == studInfo:
                deleteStudent = True

        elif deleteBy == "B":
            if student.studName.lower() == studInfo.lower():
                deleteStudent = True
        
        if deleteStudent == True:
            studentList.remove(student)
            print("\nStudent Info has been deleted\n")
            break
    else:
        print(f"\n{deleteByLabel[deleteBy].capitalize()} entered is not in list\n")
    

def viewStudentBubbleSort(studentList, field):
    #get length of student list
    studListLen = len(studentList)

    #Use Bubble Sort 
    for i in range(studListLen):
        for j in range(0, studListLen-i-1):
            if field == "Student Number": 
                currentElement = int(studentList[j].studNum)
                nextElement = int(studentList[j+1].studNum)
                
            elif field == "Student Name": 
                currentElement = studentList[j].studName.lower()
                nextElement = studentList[j+1].studName.lower()

            #if right of current student number is greater than current student number, exchange
            if currentElement > nextElement:
                #where the exchange happens
                studentList[j] , studentList[j + 1] = studentList[j + 1] , studentList[j]
 
    print(f"\n\nView List by {field.capitalize()}")
    printStudentList(studentList)


def viewStudentByProgram(studentList):
    for i in range(1, len(studentList)):
        key = studentList[i]
         #set index in sorted sublist -1 of first index of unsorted sublist
        indexInSorted = i - 1
        
        #while indexInSorted is still valid meaning >= 0
        #check if value at index of unsorted sublist is less than value at index of sorted list
        while indexInSorted >= 0 and key.program.lower() < studentList[indexInSorted].program.lower():
            #if value of index in unsorted is less than, move the value at sorted index plus 1 in the list
            studentList[indexInSorted + 1] = studentList[indexInSorted]
            #next index to check for next value in sorted comparted to value recently inserted from unsorted list
            indexInSorted -= 1
        #set indexInSorted next value to key to achieve proper sorting
        studentList[indexInSorted + 1] = key
        
    print(f"\n\nView List by Program")
    printStudentList(studentList)


def viewStudentByAge(studentList):
    for i in range(1, len(studentList)):
        key = studentList[i]
        indexInSorted = i - 1      

        while indexInSorted >= 0 and int(key.age) < int(studentList[indexInSorted].age):
            studentList[indexInSorted + 1] = studentList[indexInSorted]
            indexInSorted -= 1
        studentList[indexInSorted + 1] = key

    print(f"\n\nView List by Age")
    printStudentList(studentList)


#shows list by grade in descending order
def viewStudentGrade(studentList):
    for i in range(len(studentList)):
        index = i

        #incrementing value of J which is cheching all right values of current index in the list
        for j in range(i + 1, len(studentList)):
            #check if value at current index is greater than incrementing index value of j
            if int(studentList[index].grade) < int(studentList[j].grade):
                index = j

        #swap values
        studentList[i], studentList[index] = studentList[index], studentList[i]
    
    print(f"\n\nView List by Grade")
    printStudentListByGrade(studentList)


def printStudentList(studentList):
    print("\nAscending Order")
    for student in studentList:
        print(f'\nStudent Number : {student.studNum}'
            + f'\nStudent Name : {student.studName}'
            + f'\nProgram : {student.program}'
            + f'\nAge : {student.age}'
            + f'\nGrade : {student.grade}\n')


def printStudentListByGrade(studentList):
    print("\nDescending Order")
    for index in range(10):
        try:
            studentList[index]
            print(f'\nTop {index+1}')
            print(f'\nStudent Number : {studentList[index].studNum}'
                + f'\nStudent Name : {studentList[index].studName}'
                + f'\nProgram : {studentList[index].program}'
                + f'\nAge : {studentList[index].age}'
                + f'\nGrade : {studentList[index].grade}\n')
        except:
            print(f"Student List only contains {index} entries\n")
            break


def main():
    studentList = []

    while True:
        choice = input("\nStudent List Menu\n"
                     + "\n1 - Add Student"
                     + "\n2 - Delete Student"
                     + "\n3 - View List"
                     + "\n4 - Exit"
                     + "\n\nEnter your choice : ")

        if choice == "1":
            studentList.append(addStudent(studentList))

        elif choice == "2":
            if len(studentList) > 0:
                deleteStudent(studentList)
            else:
                print("\nNo records found.\n")

        elif choice == "3":
            viewBy = input("\nView List by:\n"
                         + "\n1 - Student Number"
                         + "\n2 - Student Name"
                         + "\n3 - Program"
                         + "\n4 - Age"
                         + "\n5 - Top 10 by Grades"
                         + "\n\nEnter your choice : ")
            
            if len(studentList) > 0:
                if viewBy == "1":
                    #ascending order
                    viewStudentBubbleSort(studentList, "Student Number")

                elif viewBy == "2":
                    #ascending order
                    viewStudentBubbleSort(studentList, "Student Name")
                
                elif viewBy == "3":
                    #ascending order
                    viewStudentByProgram(studentList)
                
                elif viewBy == "4":
                    #ascending order
                    viewStudentByAge(studentList)
                
                elif viewBy == "5":
                    #descending order
                    viewStudentGrade(studentList)
            else:
                print("\nNo records found.\n")

        elif choice == "4":
            print("\nGoodbye! . . . . . \n")
            break

        else:
            print("\nInvalid Input\n")

main()