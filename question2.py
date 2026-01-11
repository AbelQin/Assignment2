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