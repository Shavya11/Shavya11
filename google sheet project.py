
import requests
from datetime import datetime


Nutritiomix_id = "Login and get id"
Api_Key = "Get free Api_key"
Api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety API endpoint
shetty_endpoint = "https://api.sheety.co/e42364b615be3ef00dbc14e4207a9743/copyOfMyWorkouts/workouts"

# Headers for Nutritionix API
headers = {
    "x-app-id": Nutritiomix_id,
    "x-app-key": Api_Key,
    "Content-Type": "application/json"
}

# Get user input for exercise
Exercise_text = input("What exercises did you perform: ")

# Parameters for Nutritionix API
parameters = {
    "query": Exercise_text
}

# Make request to Nutritionix API
response = requests.post(url=Api_endpoint, headers=headers, json=parameters)
response_data = response.json()

# Extract exercise data
exercise = response_data["exercises"][0]["user_input"]
duration = response_data["exercises"][0]["duration_min"]
calories_burned = response_data["exercises"][0]["nf_calories"]

# Print exercise data
print("Calories Burned:", calories_burned)


# Get current date and time
current_time = datetime.now()
formatted_day = current_time.strftime("%Y/%m/%d")
formatted_time = current_time.strftime("%H:%M:%S")


sheet_inputs = {
    "workout": {
        "date": formatted_day,
        "time": formatted_time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories_burned,
    }
}


response_2 = requests.post(url=shetty_endpoint, json=sheet_inputs)
print(response_2.json())
