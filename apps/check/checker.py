

import requests
import json
import time
import random

def check_card(card, gate):
    donelist= []
    if gate == "gate1":
        reqUrl = "https://str1pe-gate1.up.railway.app/runserver/"
    else:
        reqUrl = "https://str1pe-gate1.up.railway.app/runserver/"
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "application/json" 
    }


    try:
         payload = json.dumps({"card": card})
         response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
         print(response.text)
         print(card)
         return card + " => " + response 
    # or do something else with the line

    except:
        print("error...")
        
            
def get_result():
    with open('_livefile', 'r') as file:
    # Read each line of the file
        for line in file:
            # Remove any newline characters
            line = line.strip()
            # Print the line
            return line
    with open('_deadfile', 'r') as file:
    # Read each line of the file
        for line in file:
            # Remove any newline characters
            line = line.strip()
            # Print the line
            return line