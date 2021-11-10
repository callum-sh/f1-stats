import requests
import json

url = 'http://ergast.com/api/f1/2021/drivers'
response = requests.get(url)
print(response.content)

race_year = "current"
race_round = "last"

race_results_url = "http://ergast.com/api/f1/" + race_year + "/" + race_round + "/results"
race_results = requests.get(race_results_url)
print("Race Result for Race " + race_round + " in the " + race_year + " season.")
# print(race_results.content)

race_qualifying_url = "http://ergast.com/api/f1/" + race_year + "/" + race_round + "/qualifying.json?callback=myParser"
qualifying_results = requests.get(race_qualifying_url)
# print(qualifying_results.content)

x = qualifying_results.json()

print(x)

