# github repo link: https://github.com/joanneslee/ds2002

import json
import requests
import sys

'''
Documentation:
This data processor, coordinates.py, uses Geocoding API from OpenWeatherMap. 
It takes in user input of a city name and stores the coordinate points, latitude and longitude, 
of up to five locations with the given city name in a JSON file, coordinate_information.json. 

If an invalid city name is entered, an error message is printed. 
'''

try:
    # asks user for a city name
    input_location = input("Find the coordinates of a city! \n Enter city name: ")

    # api call to geocoding api
    url = "http://api.openweathermap.org/geo/1.0/direct?"
    query_str = {"q": input_location, "limit": 5, "appid": "30264ef95ba13313cccb97665398919e"}
    response = requests.request("GET", url, params=query_str)
    coord_json = response.json()
    if not coord_json:
        sys.exit()

    # remove property "local names"
    for element in coord_json:
        if "local_names" in element.keys():
            del element["local_names"]

    # serializing json: dumps() takes a json object and returns a string
    json_object = json.dumps(coord_json, indent=4)

    # writing json file to local disk
    with open("coordinate_information.json", "w") as outfile:
        outfile.write(json_object)
    print("Coordinates of up to five location(s) named", input_location, "stored in coordinate_information.json.")

except:
    print("Error: Invalid location. API unable to return information.")
