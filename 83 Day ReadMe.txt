 Day 83 -> Handling Events 


Handling Events in Tkinter:
Event Handling in Tkinter allows the program to respond to user actions, like mouse clicks or key presses.
It is done using the .bind() method, which links an event to a function (called an event handler).

Key Points:
bind(event, function):
Connects a widget to an event. When the event occurs, the function runs.

Common Events:
<Button-1> → Left mouse click
<Double-1> → Double left-click

Event Object:
The function receives an event object, which contains info like:
event.x, event.y: Mouse pointer position
event.char: Character of key pressed