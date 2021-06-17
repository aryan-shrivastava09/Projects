import requests
from datetime import datetime

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = "9e110058"
app_key = "487a774b61f9a589a0c1f50ba62a5664"
header_api = {
    "x-app-id":app_id,
    "x-app-key":app_key,
}

exercise_text = input("Tell me which excercises you did: ")

parameters = {
    "query" : exercise_text,
    "gender":"male",
    "weight_kg":72.5,
    "height_cm":175,
    "age":21
}

response = requests.post(url = excercise_endpoint, json= parameters, headers = header_api)
result = response.json()
exercises = {exercise["name"]:[exercise["duration_min"], exercise["nf_calories"]] for exercise in result["exercises"]}
print(exercises)

today = datetime.now()
sheety_url = "https://api.sheety.co/b97bf893bfb25d8ddd9a3cbee3a19644/copyOfMyWorkouts/workouts"
sheety_header = {
    "Authorization": "Basic QXJ5YW4wOTpQcmlvcnlvZnNpb24wOQ=="
}

for key in exercises:
    parameters_sheet = {
        "workout":{
            "date" : today.strftime("%d/%m/%Y"),
            "time" : today.strftime("%H:%M:%S"),
            "exercise" : key.title(),
            "duration" : exercises[key][0],
            "calories" : exercises[key][1]
        }
    }
    response2 = requests.post(url= sheety_url, json= parameters_sheet, headers = sheety_header)
    print(response2.json())
