import random

def password_generator(name: str, length: int) -> str:
    
    x = ''
    
    for i in range(length):
        r = random.randint(1,2)
        
        if x == 1:
            x = x + random.randint(0,9)
            
        else:
            x = x + chr(random.randint(32, 126))
        
    return x 

print(password_generator("Vk", 15))
            