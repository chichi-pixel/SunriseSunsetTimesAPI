# https://api.sunrise-sunset.org/json
# https://sunrise-sunset.org/api

import requests
from datetime import datetime


MY_LAT = 52.520008
MY_LONG =  13.404954


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,

}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()
#print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)
print(time_now.hour)

