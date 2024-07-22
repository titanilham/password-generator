import random

def password_generator(name="Name", length="18") -> str:
    
    name = input("Name: ")
    length = int(input("Length: "))
    
    x = ''
    
    for i in range(length):
        r = random.randint(1,2)
        
        if x == 1:
            x = x + random.randint(0,9)
            
        else:
            x = x + chr(random.randint(33, 126))
    
    x = f"\033[1m{name}:\033[0m \x1B[3m{x}\x1B[0m"  
    
    return x

print(password_generator())

