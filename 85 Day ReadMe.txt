Day 85 -> Message Box


Messagebox in Tkinter:
A messagebox is a popup dialog used to show messages, ask questions, or display alerts.
It is part of tkinter.messagebox and is used to interact with the user through dialog windows.

Functions of Messagebox Used:
1. showinfo(title, message)
Shows a simple information popup with an OK button.
Used in your help() and Rating() functions.

2. askquestion(title, message)
Asks a Yes/No question and returns 'yes' or 'no'.
Used in Rating() to check user experience.

3. askretrycancel(title, message)
Shows a Retry/Cancel box and returns True (Retry) or False (Cancel).
Used in friending() to handle decision-making.

