# File Handling :- Mechanism to read and write the file, and to save data permanently into file.
a = open("regex.txt")    # store memory address in variable 'a'
out = a.read()           # by default, file open in read mode
a.close()
print(out)

# To write in a file,
a = open("regex.txt","w")              # "r+"
a.write("Hello World")
a.close()

# write mode will create a file if the file doesn't exist.
# In 'w' mode, previous content written in the file will be overwrite by the new content

# To see the position of a cursor, we use a.tell()
# To change the position of a cursor, a.seek() 

# read :- reads the entire file
# readline :- reads one line at a time

# Using 'with' syntax:-
with open ("regex.txt","w") as f:
    out = f.write("Hello Mayuri")

# readline(), readlines(), using loop
  