# Question 2 - Temperature Analysis

import os
import csv
import math

# Folder where all temperature csv files are stored
DATA_FOLDER = "temperatures"

# Month names used in the csv files
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Australian seasons
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}


# Read all csv files and collect temperature data
def read_temperature_data():
    season_temperatures = {
        "Summer": [],
        "Autumn": [],
        "Winter": [],
        "Spring": []
    }

    station_temperatures = {}

    # Go through all files in temperatures folder
    for file_name in os.listdir(DATA_FOLDER):
        if file_name.endswith(".csv"):
            file_path = os.path.join(DATA_FOLDER, file_name)

            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    station = row["STATION_NAME"]

                    # Create list for station if not exists
                    if station not in station_temperatures:
                        station_temperatures[station] = []

                    # Read each month temperature
                    for month in MONTHS:
                        value = row[month]

                        # Skip missing values
                        if value == "" or value == "NaN":
                            continue

                        temperature = float(value)

                        station_temperatures[station].append(temperature)

                        # Put temperature into correct season
                        for season in SEASONS:
                            if month in SEASONS[season]:
                                season_temperatures[season].append(temperature)

    return season_temperatures, station_temperatures


# Calculate standard deviation (basic formula)
def standard_deviation(values):
    mean = sum(values) / len(values)
    total = 0

    for v in values:
        total += (v - mean) ** 2

    return math.sqrt(total / len(values))


# Find most stable and most variable stations
def calculate_temperature_stability(station_temperatures):
    min_std = float("inf")
    max_std = -1

    most_stable = []
    most_variable = []

    for station in station_temperatures:
        std = standard_deviation(station_temperatures[station])

        if std < min_std:
            min_std = std
            most_stable = [(station, std)]
        elif std == min_std:
            most_stable.append((station, std))

        if std > max_std:
            max_std = std
            most_variable = [(station, std)]
        elif std == max_std:
            most_variable.append((station, std))

    with open("temperature_stability_stations.txt", "w") as f:
        for s, std in most_stable:
            f.write(f"Most Stable: Station {s}: StdDev {std:.2f}°C\n")

        for s, std in most_variable:
            f.write(f"Most Variable: Station {s}: StdDev {std:.2f}°C\n")
