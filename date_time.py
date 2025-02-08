from datetime import datetime, timedelta
import json

# Original JSON data
data = {
    "input_data": [
        {
            "fields": [
                "date",
                "Location",
                "Altitude",
                "Rainfall (mm)",
                "Population",
                "% Blockage of Drains"
            ],
            "values": [
                [
                    "1/1/2077",
                    "Bronx",
                    12,
                    44,
                    1471160,
                    75
                ]
            ]
        }
    ]
}

# Function to generate a week's worth of data with incremented dates
def increment_dates(data, days):
    start_date_str = data["input_data"][0]["values"][0][0]  # Get the start date
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")  # Convert to datetime
    
    # For each day in the range (0 to days-1)
    for i in range(1, days):
        # Increment the date
        new_date = start_date + timedelta(days=i)
        # Format the new date and append new entry to values
        new_entry = data["input_data"][0]["values"][0].copy()  # Copy the initial values
        new_entry[0] = new_date.strftime("%m/%d/%Y")  # Update date
        data["input_data"][0]["values"].append(new_entry)  # Add to values

# Increment dates for a week (7 days)
increment_dates(data, 7)

# Print updated JSON data
print(json.dumps(data, indent=1))

with open('data.txt', 'w') as json_file:
    json.dump(data, json_file)