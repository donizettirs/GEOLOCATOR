📦 Shipping Distance Calculator with Geopy & Pandas

🔍 What It Does
Reads shipping data from an Excel file using pandas
Uses geopy + Nominatim to fetch geolocation coordinates (lat/lon) for each origin and destination
Calculates the geodesic distance (in kilometers) between those points
Appends a new column with the result (Distance_km)
Saves the updated DataFrame back to Excel

🧠 Why It Matters
This tool is a helpful source of enriched geolocation data for logistics applications. It’s especially useful for supply chain analysts and BI professionals who need to:
Estimate fuel consumption
Calculate delivery times
Optimize routes
Evaluate carrier performance

🛠️ Tech Stack
Python 3
pandas – for data handling
geopy – for geocoding and distance calculation
openpyxl – for Excel file I/O (via pandas)

df['Distance_km'] = df.apply(lambda row: calculate_distance(row['Origem'], row['Destino']), axis=1)

💾 Input: Excel with columns Origem and Destino
📤 Output: New file with distances in km: cronograma de vendas_with_km.xlsx

⚙️ Notes
Uses caching to avoid repeated API calls
Includes retry logic for geocoding timeouts
Sleeps between API calls to respect rate limits
Columns are reordered to improve readability

cronograma de vendas.xlsx    
cronograma de vendas_with_km.xlsx
 geo_distance_calculator.py     


