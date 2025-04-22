from fastapi import FastAPI
from pydantic import BaseModel
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize FastAPI app
app = FastAPI()

# Initialize geolocator
geolocator = Nominatim(user_agent="geo_distance_api")

class LocationInput(BaseModel):
    place1: str
    place2: str

def get_coordinates(place):
    """Fetch latitude and longitude of a place."""
    try:
        location = geolocator.geocode(place)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except Exception as e:
        return None

def calculate_distance(place1, place2):
    """Calculate distance between two places in km."""
    coords1 = get_coordinates(place1)
    coords2 = get_coordinates(place2)

    if coords1 and coords2:
        return round(geodesic(coords1, coords2).kilometers, 2)
    else:
        return None  # Return None if coordinates are missing

@app.post("/calculate_distance")
async def get_distance(data: LocationInput):
    """API Endpoint to calculate distance between two locations."""
    distance = calculate_distance(data.place1, data.place2)
    return {"place1": data.place1, "place2": data.place2, "distance_km": distance}
