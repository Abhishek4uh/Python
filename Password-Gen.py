import string
import random
s1=string.ascii_letters
s2=string.ascii_lowercase
s3=string.ascii_uppercase
s4=string.digits
s5=string.punctuation
pass_len=int(input("Enter Password Length!"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))
random.shuffle(s)
print("Your Password Is")
print("".join(random.sample(s,pass_len)))
