import read
from datetime import datetime


# Extract data required in a suitable format.
def manip_data():
    input_data = read.read_data()

    # Create output data list of dictionaries.
    output_data = []
    for row in input_data:
        output_data.append({
            "start": row["Start"],
            "end": row["End"],
            "duration": ""
        })

    # Convert strings to datatime objects.
    for row in output_data:
        row["start"] = datetime.strptime(row["start"], "%Y-%m-%d %H:%M:%S")
        row["end"] = datetime.strptime(row["end"], "%Y-%m-%d %H:%M:%S")
        row["duration"] = row["end"] - row["start"]

    return output_data


# Print data with each dictionary (night's sleep) on a new row.
def view_manip_data():
    data = manip_data()
    for row in data:
        print(row)


# Convert duration to seconds (needed for calculating mean, max. etc.)
def duration_in_secs():
    data = manip_data()
    duration = []
    for row in data:
        row["duration"] = row["duration"].seconds
        duration.append(row["duration"])
    return duration
