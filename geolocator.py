from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
import openpyxl
import time



df = pd.read_excel('places.xlsx')


def get_coordinates(place):
    geolocator = Nominatim(user_agent="geo_distance_calculator")
    location = geolocator.geocode(place)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def calculate_distance(place1, place2):
    coords1 = get_coordinates(place1)
    coords2 = get_coordinates(place2)

    if coords1 and coords2:
        distance = geodesic(coords1, coords2).kilometers
        return f"The distance between {place1} and {place2} is {distance:.2f} km."
    else:
        return "Could not find location data for one or both places."

# Example usage
place1 = input("Enter first location: ")
place2 = input("Enter second location: ")

print(calculate_distance(place1, place2))
#print(df)
