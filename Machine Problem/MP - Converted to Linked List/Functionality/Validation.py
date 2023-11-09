import getpass

def getValidInputNumberRange(greaterThan, lessThan, label):
    while True:
        validInputNumberRange = input(f"Enter {label} : ")
        try:
            validInputNumberRange = int(validInputNumberRange)
            if validInputNumberRange >= greaterThan and validInputNumberRange <= lessThan:
                break
            print(f"\n{label.capitalize()} must be greater than or equal to {greaterThan} and less then or equal to {lessThan}\n")
        except:
            print(f"\n{label.capitalize()} must be numerical\n")

    return validInputNumberRange

def getValidInputNumberValue(greaterThan, label):
    while True:
        validInputNumberRange = input(f"Enter {label} : ")
        try:
            validInputNumberRange = int(validInputNumberRange)
            if validInputNumberRange > greaterThan:
                break
            print(f"\n{label.capitalize()} must be greater than {greaterThan}\n")
        except:
            print(f"\n{label.capitalize()} must be numerical\n")

    return validInputNumberRange


def getValidInputLegnth(length, label):
    while True:
        validInputLengthString = input(f"Enter {label} : ")
        if len(validInputLengthString) > length:
            break
        print(f"\n{label.capitalize()} must have a length greater than {length}\n")

    return validInputLengthString

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
        print(f"\n{label.capitalize()} must be numerical\n")

    return validNumber

def getValidPassword(label):
    while True:
        validPassword = getpass.getpass(f'Enter {label} : ')
        if len(validPassword) > 8:
            break
        print(f"\n{label.capitalize()} must have a length greater than 8\n")
    
    return validPassword

def getValidSpecificNumberValue(value, label):
    while True:
        validSpecificNumberValue = int(getValidNumber(label))
        if validSpecificNumberValue == value:
            break
        print("\nInvalid Input\n")
    
    return validSpecificNumberValue