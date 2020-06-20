#import string and random library
import string
import random
#define an empty list
lst=[]
char_val=input("Do you want to generate an OTP? Y/N:")
#function to generate OTP
def gen_otp():
	str_set1=string.digits
	lst.extend(str_set1)
	random.shuffle(lst)
	temp="".join(lst[:4])
	print("Your OTP: " + temp)
#check if user wants to generate an OTP
if char_val == "Y" or char_val == "y":
	gen_otp()
else:
	quit()