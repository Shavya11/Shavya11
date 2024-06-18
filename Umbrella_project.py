import requests
from twilio.rest import Client
api_key = "login in twilio and get it"
account_sid = "login in twilio and get it"
auth_token = "login in twilio and get it"
MY_LAT = 23.113501  # Your latitude
MY_LONG = 70.027702  # Your longitude

api_call = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4

}
responce = requests.get(url=api_call, params=parameters)
responce.raise_for_status()
weather_data = responce.json()
if_rain = False
for i in range(0, 4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        if_rain = True

if if_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Take Umbrella",
        from_='Temp no you will get from twilio',
        to='number on which sms will be sent'
    )
    print(message.status)
