# Day 66 -> Shutil module in python


import shutil
import os

#Copying the files
shutil.copy("66 Day Shutil module in python.py", "2. 66 Day Shutil module in python.py")

#Copying a folder
shutil.copytree("e:\CP\\100-Day-Challenge-of-Learning-python\\66 Day Shutil module in python", "Coping a file .1")

#Move the folder from one path to another
shutil.move("Coping a file .1/Coping a file", "New file outside from using move")


#Can't remove the folder using shutil so i use os 
shutil.rmtree("Coping a file .1")
os. remove("2. 66 Day Shutil module in python.py")