def swapFiles():

    file1 = input("Enter 1st file name: ")
    file2 = input("Enter 2nd file name: ")

    refer1 = open(file1, 'r')
    file1Data = refer1.read()

    refer2 = open(file2, 'r')
    file2Data = refer2.read()

    write1 = open(file1, 'w')
    write1.write(file2Data)

    write2 = open(file2, 'w')
    write2.write(file1Data)

swapFiles()
