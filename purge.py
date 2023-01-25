import requests
import json

while True:
    user_id = input("your discord account id: ")
    if user_id == "":
        print("invalid input")
    else:
        break
        
while True:
    channel_id = input("channel id: ")
    if channel_id == "":
        print("invalid input")
    else:
        break
        
while True:
    token = input("your discord account token: ")
    if token == "":
        print("invalid input")
    else:
        break
        
while True:
    try:
        how_many = int(input("How many messages to purge: "))
        break
    except:
        print("please type valid number")






auth = { 'authorization': token
}
url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={how_many}"

response = requests.get(url,headers = auth)
response = response.text
response = json.loads(response)

for message in response:
    try:
        content = message['content']
    except:
        input("exception has occurred: make sure you typed everything correctly!")
        exit()
    message_id = message['id']
    author = message['author']
    author_id = author['id']
    message_channel_id = message['channel_id']
    url2 = f"https://discord.com/api/v9/channels/{message_channel_id}/messages/{message_id}"
    if author_id == user_id:
        requests.delete(url2,headers = auth)
        print(f'deleted message "{content}"')

input("purge finished. press enter to close the window")


