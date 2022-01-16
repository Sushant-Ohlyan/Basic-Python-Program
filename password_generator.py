import string
import random

if __name__ == "__main__":
    s1=string.ascii_lowercase

    s2=string.ascii_uppercase

    s3=string.digits
    plen=int(input("enter password length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s3))
    s.extend(list(s2))
    #print(s)
    #random.shuffle(s)
    #print(s)
    print("your new password is::")
    print("".join(random.sample(s,plen)))