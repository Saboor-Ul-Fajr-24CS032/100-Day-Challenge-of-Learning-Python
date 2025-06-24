Day 38 -> File IO


I am using this in python file in opening and closing of file.



File I/O?
File I/O (Input/Output) means reading data from a file and writing data to a file using a Python program. This allows to store information permanently.

Opening a file:
You use Python’s built-in open() function.
Syntax:
file = open('filename', 'mode')

Closing a file:
When you’re done, you should close the file using:
file.close()

File Modes:
Mode	Meaning
r	    Read mode (default) — opens file for reading. Error if file does not exist.
w	    Write mode — creates a new file or overwrites existing one.
a	    Append mode — adds data to the end of the file. Creates file if it doesn’t exist.
x	    Exclusive creation — creates a new file but gives an error if file already exists.
t	    Text mode (default) — handles file as text (strings).
b	    Binary mode — handles file as binary (bytes). Useful for images, videos, etc.
rb	    Read binary — read file in binary mode.
rt	    Read text — read file in text mode (same as r).


with statement?
The with statement automatically opens and closes the file properly, even if an error happens inside the block.
It’s safer and cleaner because you don’t have to remember to call close().
