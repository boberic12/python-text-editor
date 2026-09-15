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
    print("This option creates a new file and sets it to the affected file")
    print(" ")
    newFile = input("Choose a name for the new file: ")
    createFile(newFile)
    print("New file created:", newFile)
    print("Waiting for changes to apply...")
    print("This will take 20s")
    # I know that's a lie
    sleep(18)
    filenameA = newFile
    print("File Chosen:", filenameA)
    sleep(1)


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


def chooseNewFile():
    print("\n" * 100)
    print("This option chooses a new file")
    print("If the file doesnt exist a new one will be created when writing or wiping the file")
    print(" ")  # Harold Haggis was here
    filenameA = input("Choose a filename: ")
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
    3: Create
    4: Wipe File
    5: Choose New File
    6: Exit

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
        chooseNewFile()
    if option == "6":
        exit()
    else:
        chooseOption()


print("Welcome to the Text Editor!")
filenameA = input("Choose a file name: ")
try:
    with open(filenameA, 'x') as file:
        file.write("")
    print("File Created")
except FileExistsError:
    print("File Opened")
sleep(1)
chooseOption()