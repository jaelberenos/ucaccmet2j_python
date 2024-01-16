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
#print(results_relative)

# Save results_relative to results.json
with open('results.json', 'w') as resultfile:
    json.dump(results_relative, resultfile, indent=2)




# Rewrite your code so that it calculates all the above for each location
# Calculate the relative_yearly_precipitation compared to the other stations, i.e. what percentage of all the measured rain in all locations, fell in Seattle?
    
# Create a dictionary to store total yearly precipitation for each station
total_yearly_precipitation_by_station = defaultdict(float)

# Create a dictionary to store relative monthly precipitation for each station
relative_monthly_precipitation_by_station = defaultdict(lambda: defaultdict(float))

# Calculate total yearly precipitation for each station
for station in stations_data:
    station_code = station['Station']
    station_measurements = [measurement 
                            for measurement in precipitation 
                                if measurement['station'] == station_code]
    
    total_yearly_precipitation = sum(measurement['value'] for measurement in station_measurements)
    total_yearly_precipitation_by_station[station_code] = total_yearly_precipitation
    
    # Calculate relative monthly precipitation for each station
    for measurement in station_measurements:
        date_parts = measurement['date'].split('-')
        month_key = f"{date_parts[0]}-{date_parts[1]}"
        relative_monthly_precipitation_by_station[station_code][month_key] += measurement['value'] / total_yearly_precipitation

# Calculate relative yearly precipitation for each station
relative_yearly_precipitation_by_station = {}
for station_code, total_yearly_precipitation in total_yearly_precipitation_by_station.items():
    relative_yearly_precipitation_by_station[station_code] = total_yearly_precipitation / sum(total_yearly_precipitation_by_station.values()) * 100

# Convert defaultdicts to lists of dictionaries for output
results_relative_by_station = {
    'total_yearly_precipitation_by_station': dict(total_yearly_precipitation_by_station),
    'relative_monthly_precipitation_by_station': {station_code: [{'month': key, 'relative_monthly_precipitation': value} for key, value in relative_monthly_precipitation.items()] for station_code, relative_monthly_precipitation in relative_monthly_precipitation_by_station.items()},
    'relative_yearly_precipitation_by_station': relative_yearly_precipitation_by_station
}

print(results_relative_by_station)

#Save results to results.json
with open('results.json', 'w') as resultfile:
    json.dump(results_relative_by_station, resultfile, indent=2)


                                 

        

    




