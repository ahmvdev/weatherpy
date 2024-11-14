import requests

key='ae00a4dbf3aa4c0f93d103719241411'

location = input('Enter location: ')
r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}')

response = r.json()



city = response['location']['name']
country = response['location']['country']
timezone = response['location']['tz_id']

print(f'City: {city}\nCountry: {country}\nTimezone: {timezone}')