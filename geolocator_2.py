import time
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut

# Initialize geolocator
geolocator = Nominatim(user_agent="geo_distance_calculator")

# Cache to store coordinates and avoid repeated API calls
cache = {}

def get_coordinates(place, max_retries=3):
    """Get latitude and longitude of a place with retries and caching."""
    
    if place in cache:
        return cache[place]  # Return cached result

    retries = 0
    while retries < max_retries:
        try:
            time.sleep(5)  # Respect API rate limits
            location = geolocator.geocode(place, timeout=10)  # Increase timeout to 10 seconds
            
            if location:
                coords = (location.latitude, location.longitude)
                cache[place] = coords  # Store in cache
                return coords
            else:
                return None  # Location not found
        
        except GeocoderTimedOut:
            retries += 1
            print(f"Timeout for {place}. Retrying {retries}/{max_retries}...")
            time.sleep(5)  # Wait before retrying

    print(f"Failed to fetch coordinates for {place} after {max_retries} retries.")
    return None

def calculate_distance(Origem, Destino):
    """Calculate the distance between two places in km."""
    
    coords1 = get_coordinates(Origem)
    coords2 = get_coordinates(Destino)

    if coords1 and coords2:
        return round(geodesic(coords1, coords2).kilometers, 2)  # Return distance
    else:
        return None  # Return None if coordinates are missing

# Load Excel file
path = r'C:\BACKUP\CODDING\POWER BI\IPROFESSIONAL\EXCEL\LAIS\cronograma de vendas.xlsx'

# Load Excel file
df = pd.read_excel(path)
#df = pd.read_excel('places.xlsx')

# Apply function to DataFrame
df['Distance_km'] = df.apply(lambda row: calculate_distance(row['Origem'], row['Destino']), axis=1)

# Reorder columns: Move 'Distance_km' to be right after 'Destino'
column_order = df.columns.tolist()  # Get current column order
column_order.insert(column_order.index('Destino') + 1, column_order.pop(column_order.index('Distance_km')))  
df = df[column_order]  # Reorder DataFrame

# Save the updated DataFrame to a new Excel file
df.to_excel('cronograma de vendas_with_km.xlsx', index=False)

# Print the updated DataFrame
print(df)
