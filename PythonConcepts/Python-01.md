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
