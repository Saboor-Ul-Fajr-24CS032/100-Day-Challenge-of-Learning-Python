# Day 76 -> Attributes of Label and Pack


from tkinter import * 

root = Tk()
root .geometry("444x233")
root.title("76 Day Lecture")


# Label Options 

label1 = Label(text = '''
The city is flying. We're fighting an army of robots. 
And I have a bow and arrow. None of this makes sense. 
But I'm going back out there ‘cause this is my job. Okay? And I can't do my job and babysit. 
Doesn't matter what you did, or what you were. If you go out there, you fight, and you fight to kill. 
Stay in here and you're good. I'll send your brother to come find you. 
But if you step out that door, you are an Avenger.

''' , bg="lightblue" , foreground="white" , padx= 40 , pady = 70 , font = ("Times new roman", 19, "bold"), borderwidth=3 , relief=RIDGE
  )
label1.pack()


#Pack Options 

label1.pack(side= "bottom", anchor="se", fill= "x", padx=34, pady= 50)


root.mainloop()