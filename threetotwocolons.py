import glob

def List_Text():
    global filename
    myFiles = glob.glob('*.txt')

    for i in range(0, len(myFiles)):
        print(str(i) + ": " + myFiles[i])
    
    print("(c) Use custom file ")

    print()
    selection = input("Make your selction from above: ")

    if selection == "c" or selection == "C":
        filename = input("File name (example [don't put extension]): ")
        filename = filename + ".txt"
    else:
        changedselection = int(selection)
        filename = myFiles[changedselection]


    return filename





print("1. Format three section combolist")
print("2. Combine files")
option = int(input(" Select from above: "))





if option == 1: # Format
    List_Text() 

    newfilename = '(formatted)' + filename
    passfilename = '(passwords)' + filename
    userfilename = '(emails)' + filename

    with open(filename) as reader:
        line = reader.readline()

        user = []
        password = []

        while line != '':  # The EOF char is an empty string
            templist = line.split(':')
            if len(templist) == 3:
                user.append(templist[0])
                password.append(templist[1])

            line = reader.readline()

    with open(newfilename, 'w') as writer: # Two combolist
        if len(user) == len(password):
            for i in range(0, len(user)):
                writer.write(user[i] + ":" + password[i] + '\n')
    print("New file saved as " + newfilename)

    with open(passfilename, 'w') as writer: # Password list
        for i in range(0, len(password)):
            writer.write(password[i] + '\n')
    print("New file saved as " + passfilename)

    with open(userfilename, 'w') as writer: # Email list
        for i in range(0, len(user)):
            writer.write(user[i] + '\n')
    print("New file saved as " + userfilename)




if option == 2: # Join files
    

    print("File one (dont put extension): ")
    file1name = List_Text()

    print ("File two (dont put extension): ")
    file2name = List_Text()



    newfile = file1name[:-4] + "x" + file2name[:-4] + ".txt"


    templist = []
    

    # open file 1 and save each line to list
    with open(file1name) as reader:
        line = reader.readline()
        while line != '': 
            print(line)
            templist.append(line)

            line = reader.readline()


    # open file 2 and save each line to list
    with open(file2name) as reader:
        line = reader.readline()
        while line != '': 
            templist.append(line)

            line = reader.readline()


    # Open write file and output contents of list
    with open(newfile, 'w') as writer:
        for i in range(0, len(templist)):
            writer.write(templist[i])


    print("New file saved to " + newfile)

