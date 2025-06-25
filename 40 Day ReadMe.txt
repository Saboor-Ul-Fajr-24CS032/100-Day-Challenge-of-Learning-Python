Day 40 -> seek() , tell() and other functions 


seek():
seek() is used to move the file cursor (pointer) to a specific position in the file. This lets you read or write from a chosen point instead of always starting at the beginning or end.

tell():
tell() returns the current position of the file cursor in bytes. It shows where you are in the file, which helps when reading or writing in parts.

truncate():
truncate() is used to cut (shorten) the file to a specific size. If no size is given, it cuts the file at the current cursor position.
It’s mostly used to shorten files.
Useful for clearing unwanted data at the end.