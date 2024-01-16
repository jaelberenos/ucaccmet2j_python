import json
with open ('precipitation.json', encoding= 'utf-8') as file:
    precipitation = json.load(file)

#calculate total monthly precipitation:  a list with the total precipitation per month, for that location
#seatle code GHCND:US1WAKG0038 


import csv
import json
from collections import defaultdict

# Load CSV data
with open('stations.csv', 'r') as csvfile:
    stations_data = list(csv.DictReader(csvfile))

# Filter measurements for Seattle station
seattle_measurements = [measurement for measurement in precipitation if measurement['station'] == 'GHCND:US1WAKG0038' ]

# Calculate total monthly precipitation
total_monthly_precipitation = defaultdict(float)
for measurement in seattle_measurements:
    date_parts = measurement['date'].split('-')
    month_key = f"{date_parts[0]}-{date_parts[1]}"
    total_monthly_precipitation[month_key] += measurement['value']

# Convert defaultdict to a list of dictionaries
results = [{'month': key, 'total_monthly_precipitation': value} for key, value in total_monthly_precipitation.items()]
print(results)

# Save results to results.json
with open('results.json', 'w') as resultfile:
    json.dump(results, resultfile, indent=2)


