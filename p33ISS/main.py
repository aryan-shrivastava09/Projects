import requests
import datetime as dt
import smtplib
import time

MY_LNG = 78.008072
MY_LAT = 27.176670

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data1 = response1.json()
iss_position = (float(data1["iss_position"]["latitude"]), float(data1["iss_position"]["longitude"]))
# print(iss_position)
currenthour = int(str(dt.datetime.now()).split()[1].split(":")[0])
# print(currenthour)

parameters = {
    "lat":MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response2 = requests.get(url= "https://api.sunrise-sunset.org/json", params= parameters)
response2.raise_for_status()
data2 = response2.json()
sunrise = int((data2["results"]["sunrise"].split("T")[1]).split(":")[0]) + 5
sunset = int((data2["results"]["sunset"].split("T")[1]).split(":")[0]) + 5
# print(sunset)
while True:
    time.sleep(60)
    if currenthour >= sunset and abs(iss_position[0] - MY_LAT) <=5 and abs(iss_position[0]- MY_LNG) <= 5:
        MY_EMAIL = "aryansri009@gmail.com"
        MY_PASSWORD = "Prioryofsion09"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user= MY_EMAIL, password= MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs="aryansri0009@yahoo.com", msg= "Subject:ISS\n\nLOOK UP!")
        connection.close()