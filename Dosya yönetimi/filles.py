#The open() function is used to open and create files.
#Use of: open(File_name, File_access_mode)
# File access mode: Indicates for what purpose we opened the file

#"w": (Write) writing mode. The file creates the structures.
#   *** Deletes and reprocesses the file contents.

# file= open("newfile.txt", "w")
# file.close( )

# file = open("newfile.txt", "w", encoding= 'utf-8')
# file.write('Sadik turan')
# file.close()

#"a": (Append) append. If the file doesn't exist, ıt creates ıt.

# file = open("newfile.txt", "a", encoding= 'utf-8')
#  file.write('\nSadik turan')
# file.write('Sadik turan\n')
# file.close()

#"x": (Create) create. It throws an error if the file already exist.

file = open("newfile2.txt", "x", encoding= 'utf-8')

#"r": (Read) read. If the default file doesn't exist in the location, it will throw an error.
