import requests

key='API KEY HERE'

location = input('Enter location: ')
r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={location}')

response = r.json()



city = response['location']['name']
country = response['location']['country']
timezone = response['location']['tz_id']

print(f'City: {city}\nCountry: {country}\nTimezone: {timezone}')