## 1) Print the path of the file if filename was given ?

A)

```
import os
print (os.path.abspath("<filename>"))
```

## 2) How to open an file in python ?

A)

```
f=open("<File Path>", "mode") # mode can be 'r' --> read, 'w'--> write, 'a' --> append
f.close() # This will close the opened file
```

## 3) How to read a file in python ?

A)
There are three ways to read a file:
**read():** Returns the read bytes in the form of a string. Reads n bytes; if n is not specified, then reads the entire file.

**readline():** Reads a line of the file and returns in the form of a string. For specified n, reads at most n bytes. readline ( ) function does not read more than one line at a time; even if n exceeds, it reads only one line.

**readlines():** Reads all the lines and returns them as a string element in a list. Readlines ( ) is used to read all the lines at a single go and then return them as a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then splits it into separate lines. Using the strip () function, we can iterate over the list and strip the newline ' \n ' character using the strip ( ) function.
Eg:

```
f=open("<File Path>", "mode")
print(f.read())
print(f.readline())
print(f.readlines())
```

## 4) Different mdoes in python file handling.

"r" - Read - Default value. Opens a file for reading, error if the file does not exist.

"a" - Append - Opens a file for appending, creates the file if it does not exist.

"w" - Write - Opens a file for writing, creates the file if it does not exist.

"x" - Create - Creates the specified file, returns an error if the file exists.

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

## 5) How to write to an existing file ?

```
f=open("demofile.txt", "a")
f.write("New content is getting added to the file now")
f.close()
```

## 6) Few python OS level commands ?

**os.mkdir():** It'll create directory.
Eg: `os.mkdir("c:/test/w3school")`

**os.getcwd():** It'll display the current working directory.
Eg: `os.getcwd()`

**os.chdir():** It'll change the directory.
Eg: `os.chdir("mydir")`

**os.chmod():** To change the permission of file
Eg: `os.chmod(path, mode)`
stat.S_IREAD - Read by owner.
stat.S_IWRITE - Write by owner.
stat.S_IEXEC - Execute by owner.
stat.S_IRWXU - Read, write, and execute by owner.
stat.S_IRGRP - Read by group
stat.S_IWGRP - Write by group
stat.S_IXGRP - Execute by group
stat.S_IRWXG - Read, write, and execute by group
stat.S_IROTH - Read by others
stat.S_IWOTH - Write by others
stat.S_IXOTH - Execute by others
stat.S_IRWXO - Read, write, and execute by others

**os.fchown():**
Eg: `os.chown(fd, uid, gid)`
