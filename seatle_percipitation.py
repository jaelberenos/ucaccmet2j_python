#import and load data sets

import json
with open ('precipitation.json', encoding= 'utf-8') as file:
    precipitation = json.load(file)

import csv
with open('stations.csv', 'r') as csvfile:
    stations_data = list(csv.DictReader(csvfile))

from collections import defaultdict

#calculate total monthly precipitation:  a list with the total precipitation per month, for that location
#seatle code GHCND:US1WAKG0038 

# Filter measurements for Seattle station
seattle_measurements = [measurement 
                        for measurement in precipitation 
                            if measurement['station'] == 'GHCND:US1WAKG0038' ]

# Calculate total monthly precipitation
total_monthly_precipitation = defaultdict(float)
for measurement in seattle_measurements:
    date_parts = measurement['date'].split('-')
    month_key = f"{date_parts[0]}-{date_parts[1]}"
    total_monthly_precipitation[month_key] += measurement['value']

# Convert defaultdict to a list of dictionaries
results = [{'month': key, 'total_monthly_precipitation': value} for key, value in total_monthly_precipitation.items()]
    #print(results)

# Save results to results.json
with open('results.json', 'w') as resultfile:
    json.dump(results, resultfile, indent=2)



# Calculate total yearly precipitation
total_yearly_precipitation = sum(measurement['value'] 
                                 for measurement in seattle_measurements)
    #print(total_yearly_precipitation)



# Calculate relative monthly precipitation
relative_monthly_precipitation = defaultdict(float)

for measurement in seattle_measurements:
    date_parts = measurement['date'].split('-')
    month_key = f"{date_parts[0]}-{date_parts[1]}"
    relative_monthly_precipitation[month_key] += measurement['value'] / total_yearly_precipitation

# Convert defaultdict to a list of dictionaries
results_relative = {
    'total_yearly_precipitation': total_yearly_precipitation,
    'relative_monthly_precipitation': [{'month': key, 'relative montly percipitation': value} for key, value in relative_monthly_precipitation.items()]
}

print(results_relative)

