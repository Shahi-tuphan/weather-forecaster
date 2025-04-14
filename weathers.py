# importing requesting... 
import requests
# defining my api key and bas url 
api_key = "1047127113cfa874f4ae6c3a402919c4"
base_url ="https://api.openweathermap.org/data/2.5/weather"

# Taking city name as input 

city = input("Enter your city name :")
# Sending  a GET request to the API with the city and API key 
request_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
response = requests.get(request_url)

# Converting  the JSON response to a dictionary 
data = response.json()

# Handling the response 
if response.status_code == 200 :
    weather = data["weather"][0]["description"]
    tempreature = data["main"]["temp"]
    print (f"Weather in {city} : {weather}")
    print (f"Tempreatur : {tempreature}°C")
    # print(data)

elif response.status_code == 404 :
    print("City does not found")

else :
    print("An error while fetching the data")