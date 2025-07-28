# Day 70 -> Regular Expressions in python


import re 

pattern = r"[A-Z]ersion"
text='''
By 2006 the English-language Version of Wikipedia had more than Sersion 1,000,000 articles, and by the time of Kersion its 10th anniversary in 2011 it had surpassed 3,500,000. However, while the encyclopedia continued to expand at a rate of millions of words per month, the number of new articles created each year gradually decreased, from a peak of 665,000 in 2007 to 374,000 in 2010

'''

#only for first accurance 

# match = re.search(pattern, text) 
# print(match)



matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    print(type(match.span()))
    print(text[match.span()[0]: match.span()[1]])    #can get the word only


