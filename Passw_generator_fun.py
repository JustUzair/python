import string
import random
pass_len=int(input("Enter desired length of password:"))
def gen_pass():
    lst=[]
    str_set1=string.ascii_letters
    str_set2=string.digits
    str_set3=string.punctuation
    lst.extend(str_set1)
    lst.extend(str_set2)
    lst.extend(str_set3)
    random.shuffle(lst)
    return lst
new_pass=gen_pass()
print("".join(new_pass[0:pass_len]))