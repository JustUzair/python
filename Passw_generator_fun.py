#import string and random library
import string
import random
pass_len=int(input("Enter desired length of password:"))
#function to generate password
def gen_pass():
    lst=[]
    str_set1=string.ascii_letters #add ascii chars from string lib and assign it to str_set1
    str_set2=string.digits #add digits from string lib and assign it to str_set2
    str_set3=string.punctuation #add special chars from string lib and assign it to str_set3
    #extend the list with string sets defined above
    lst.extend(str_set1)
    lst.extend(str_set2)
    lst.extend(str_set3)
    #shuffle the list
    random.shuffle(lst)
    return lst
#assign new generated password to new_pass 
new_pass=gen_pass()
#print the password with required no. of chars desired by user using the slicing operator
print("".join(new_pass[0:pass_len]))
