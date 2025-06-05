# Day 15 Functions 


def Name(a):
    print("Your Name is ", a , ". and you are welcome in this 100 Day of python learning challenge")




def CountingLetters(b):
    no_space= b.replace(" ", "")
    count=0
    for i in no_space:
        count += 1

    print(f"Your name has {count} numbers")

Name("Saboor Ul Fajr")
CountingLetters("Saboor Ul Fajr")

