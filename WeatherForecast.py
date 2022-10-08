import requests

city = input("Enter city name ==>")

url = "https://wttr.in/{}".format(city)

print(requests.get(url).text)