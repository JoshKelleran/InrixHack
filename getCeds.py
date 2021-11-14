import requests

response = requests.get("https://www.googleapis.com/auth/calendar")

print(response.text)
