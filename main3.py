# open a file 
file = open('sample_doc.txt', 'r')

# read and print first three lines of the file
print(file.readline())
print(file.readline())
print(file.readline())

# close the file
file.close()