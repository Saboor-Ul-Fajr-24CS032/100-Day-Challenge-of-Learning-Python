# Day 43 -> OS Module

#The work i done using od module 

import os

main_folder = "."

# Old folder names
old_folders = [
    "Day 33 Dictionaries",
    "Day 34 Dictionaries methods",
    "Day 35 For loop with else",
    "Day 36 Exception handling",
    "Day 37 Finally Keyword",
    "Day 38 Customs Errors",
    "Day 39 Short Hand If else",
    "Day 40 Enumerate Function"
]

# New folder names
new_folders = [
    "26 Day Dictionaries",
    "27 Day Dictionaries methods",
    "28 Day For loop with else",
    "29 Day Exception handling",
    "30 Day Finally Keyword",
    "31 Day Customs Errors",
    "32 Day Short Hand If else",
    "33 Day Enumerate Function"
]

# Exact old files for each folder
old_files = [
    ["33 Day Dictionaries.py", "33 Day ReadMe.txt"],
    ["34 Day Dictionaries methods.py", "34 Day ReadMe.txt"],
    ["35 Day For loop with else.py", "35 Day ReadMe.txt"],
    ["36 Day Exception handling.py", "36 Day ReadMe.txt"],
    ["37 Day Final Keyword.py", "37 Day ReadMe.txt"],  
    ["38 Day Customs Errors.py", "38 Day ReadMe.txt"],
    ["39 Day Short Hand If else.py", "39 Day ReadMe.txt"],
    ["40 Day Enumerate Function.py", "40 Day ReadMe.txt"]
]

# Exact new file names matching new folder numbering
new_files = [
    ["26 Day Dictionaries.py", "26 Day ReadMe.txt"],
    ["27 Day Dictionaries methods.py", "27 Day ReadMe.txt"],
    ["28 Day For loop with else.py", "28 Day ReadMe.txt"],
    ["29 Day Exception handling.py", "29 Day ReadMe.txt"],
    ["30 Day Final Keyword.py", "30 Day ReadMe.txt"],  
    ["31 Day Customs Errors.py", "31 Day ReadMe.txt"],
    ["32 Day Short Hand If else.py", "32 Day ReadMe.txt"],
    ["33 Day Enumerate Function.py", "33 Day ReadMe.txt"]
]

# Rename folders
for old, new in zip(old_folders, new_folders):
    os.rename(os.path.join(main_folder, old), os.path.join(main_folder, new))

# Rename files inside
for folder, old_list, new_list in zip(new_folders, old_files, new_files):
    for old_file, new_file in zip(old_list, new_list):
        os.rename(
            os.path.join(main_folder, folder, old_file),
            os.path.join(main_folder, folder, new_file)
        )

print("✅ All folders and files renamed safely with correct file names!")
