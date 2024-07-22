import random
import requests
import config 


def password_generator(name="Name", length=18) -> str:
    
    
    x = ''
    
    for i in range(length):
        r = random.randint(1,2)
        
        if x == 1:
            x = x + random.randint(0,9)
            
        else:
            x = x + chr(random.randint(33, 126))
    
    x = f"{name}:{x}"  
    
    return x

def send_msg(text):
    
    token = config.token  #Bot token 
    chat_id = config.chat_id  # Сhat where passwords will be sent 
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


send_msg(password_generator("GitHub", 25))
