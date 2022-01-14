# Files
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.


def fun_file():
    my_string = "Hello file world !"
    with open("myFile.txt", "w") as write_file:
        write_file.write(my_string)


def reads_file():
    with open("myFile.txt", "r") as read_file:
        read_f = read_file
    print(read_f)


if __name__ == '__main__':
    fun_file()
    reads_file()
