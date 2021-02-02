import requests
from datetime import datetime

API_ID = "1f68ffc9"
API_KEY = "404b5b47040141f97e4f42201fef6276"

GENDER = "female"
WEIGHT_KG = 58
HEIGHT_CM = 160
AGE = 25

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did: ")

sheet_endpoint = "https://api.sheety.co/1274e5bff0f612a7132ca3098efb8a41/workoutTracking/workouts"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    }

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer ghjghj"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "Date": today_date,
            "Time": now_time,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"]
            }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)
