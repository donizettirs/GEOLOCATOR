import pandas as pd

# Example DataFrame
data = {
    'place1': ['New York', 'Paris', 'London'],
    'place2': ['Los Angeles', 'Berlin', 'Rome']
}
df = pd.DataFrame(data)

# Iterate through each row
for index, row in df.iterrows():
    print(f"Index: {index}, place1: {row['place1']}, place2: {row['place2']}")
