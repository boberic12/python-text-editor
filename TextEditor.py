from time import sleep

# File Functions

def createFile(filenameA):
    with open(filenameA, 'x') as file:
        file.write("")


def writeToFile(filenameA, text):
    with open(filenameA, 'a') as file:
        file.write(text, )


def readFromFile(filenameA):
    with open(filenameA, 'r') as file:
        return file.read()


def wipeFile(filenameA):
    with open(filenameA, 'w') as file:
        file.write("")


newLine = "\n"


# Writes to file and shows what's already in it
def writeCLI():
    print("\n" * 100)
    print("This option adds the text to a new line to the end of the file")
    print("Type ` to return to menu")
    print(" ")
    print("Writing to:", filenameA)
    print("""

    """)
    print(readFromFile(filenameA))
    textWrite = input("")
    if textWrite == "`":
        chooseOption()
    else:
        writeToFile(filenameA, textWrite)
        with open(filenameA, 'a') as file:
            file.write(newLine)
        writeCLI()


# Reads file
def readCLI():
    print("\n" * 100)
    print("Reading from:", filenameA)
    print(" ")
    print(readFromFile(filenameA))
    print(" ")
    print(" ")
    if input("Choose another option? y/n ") == "y":
        chooseOption()
    else:
        exit()


# Creates a new file and sets filenameA to the new file
def createCLI():
    print("\n" * 100)
    print("This option creates a new file if needed and sets selected filename to affected file")
    print(" ")
    newFile = input("Choose a filename: ")
    try:
        with open(newFile, 'x') as file:
            file.write("\n")
        print("Wait 5s for Changes to apply")
        sleep(5)
        print("File Created")
        filenameA = newFile
        print("File Chosen:", filenameA)
    except FileExistsError:
        filenameA = newFile
        print("File Chosen:", filenameA)
    if input("Choose another option? y/n ") == "y":
        chooseOption()
    else:
        exit()

# Wipes all data from file

def wipeCLI():
    print("\n" * 100)
    print("This option wipes the file")
    print(" ")
    input("Press enter to continue or CTRL+C to exit")
    wipeFile(filenameA)
    print("File Wiped:", filenameA)
    print("File Chosen:", filenameA)
    if input("Choose another option? y/n ") == "y":
        chooseOption()
    else:
        exit()



# Choose What To Do
def chooseOption():
    print("\n" * 100)
    print("Choose an option")
    print("Chosen File:", filenameA)
    print(" ")
    option = input("""    1: Write
    2: Read
    3: Create or Choose File
    4: Wipe File
    5: Exit

    """)
    if option == "1":
        writeCLI()
    if option == "2":
        readCLI()
    if option == "3":
        createCLI()
    if option == "4":
        wipeCLI()
    if option == "5":
        exit()
    else:
        chooseOption()



filenameA = input("Choose a file name: ")
try:
    with open(filenameA, 'x') as file:
      file.write("\n")
    createFile(filenameA)
    print("File Created")
except FileExistsError:
    print("File Opened")
sleep(1)
chooseOption()

print("Welcome to the Text Editor!")

