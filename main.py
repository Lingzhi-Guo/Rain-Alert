import requests
import smtplib

lat = 41.878113
lon = -87.629799
api_key = "6efaf720b67cefc4bb5df8761474b771"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

parameters = {
    "appid": api_key,
    "lat": lat,
    "lon": lon,
    "cnt": 4
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

for data_piece in weather_data["list"]:
    if data_piece["weather"][0]["id"] < 700:
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Remember to  bring an Umbrella!"
        )
