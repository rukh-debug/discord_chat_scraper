import requests
import json
import pandas as pd




limit = int(input("Enter the number of last messages you wanna export \n"))  #Number of Last Messages
channelid = int(input("Enter The Channel ID you want to export chats from\n")) #Channel ID
datas = [] 

def retrieve_messages(channelid):
    headers = {
        'authorization': 'NjYyNTYxNzg1NjIyMDM2NDkz.GBa1Ei.e_qt6t6Je3u-ZijuACdpaE__TsdaPT7Prazfc0'
    }
    r= requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit={limit}', headers=headers)
    json_loader = json.loads(r.text)
    for value in json_loader:
        liyeko = value['content']
        # print(value['content'], '\n')
        i = 1
        while i < limit:
            i +=1
            datas.insert(i, liyeko)
            break
    
    print(datas)
    df = pd.DataFrame(datas)
    df.to_excel("retrieved_messages.xlsx")
    
   

retrieve_messages(channelid)