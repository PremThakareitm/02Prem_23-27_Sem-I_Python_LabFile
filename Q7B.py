# Write a program to use the ‘API’ of crypto currency.

import requests
api_id="CG-MVwfDPbzcds9onoar9oKSaqf"
while True:
    coin=input("Enter cryptocoin: ")
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr&x_cg_demo_api_key={api_id}")
    a=response.json()
    
    if(response.status_code == 200):
        while input("Press any key to see updates or \"N\" to exit") != "n":
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr&x_cg_demo_api_key={api_id}")
            a=response.json()
            for i in a:
                print("₹",a[i]['inr'])
        break
    else:
        print("Invalid currency name please retype")