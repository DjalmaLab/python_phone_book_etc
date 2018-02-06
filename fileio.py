# 1. Write a program that prompts the user to enter a file name, reads the contents of the file and prints it to the screen.

file = raw_input("Enter your file name. ")
file_read = open(file, 'r').read()
print file_read


# 2. Write a program that prompts the user to enter a file name, then prompts the user to enter the contents of the file, and then saves the content to the file.

file = raw_input("Enter your file name. ")
content = raw_input("What would you like to write into the file? ")
file_open = open(file, 'w')
file_write = file_open.write(content)
print file_write
file_open.close()

# 3. Write a program that prompts the user to enter a file name, then prints the letter histogram and the word histogram of the contents of the file.
letter_histogram = {

}
file = raw_input("Enter your file name. ")
file_open = open(file, 'r')
file_read = file_open.read()
file_read = file_read.lower()
for letter in file_read:
    if letter in letter_histogram:
        letter_histogram[letter] = letter_histogram[letter]+1
    else:
        letter_histogram[letter] = 1
print letter_histogram
