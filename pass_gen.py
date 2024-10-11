import random
import string

def gen_pass(len):
   
    char = string.ascii_letters + string.digits + string.punctuation
    
   
    password = ''.join(random.choice(char) for i in range(len))
    
    return password


try:
    len = int(input("Enter the desired password length: "))
    if len < 1:
        print("Please enter a valid length greater than 0.")
    else:
       
        generated_password = gen_pass(len)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number!!!!")
