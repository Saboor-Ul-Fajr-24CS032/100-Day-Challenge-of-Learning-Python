Day 90 -> Status Bar 


Status Bar:
Definition: A horizontal information area at the bottom of a window, made using a Label that can display changing messages.
Dynamic Text: Uses a StringVar() so the displayed text can be updated in real time (statusvar.set() in your code).
Appearance: Created with Label using relief=SUNKEN and anchor="w" to look like a classic status bar.
Placement: Positioned at the bottom with .pack(side=BOTTOM, fill=X).
Behavior: Updated during program actions — in your code, it changes to "Busy", waits, then switches to "Ready now".
