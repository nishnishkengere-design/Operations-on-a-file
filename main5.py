# open a file 
file = open('sample_doc.txt', 'r')

# loop through the lines of the file
for x in file:
    print(x)

# close the file
file.close()