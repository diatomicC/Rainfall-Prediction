import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("Training.csv")

# Extract the required columns
dates = pd.to_datetime(data["Date"])
total_rainfall = data["Total Rainfall (mm)"]
mean_wind_speed = data["Mean Wind Speed (km/h)"]
mean_cloud_amount = data["Mean Amount of Cloud (%)"]
sun = data["Sun"]
humidity = data["Humidity"]
min_temperature = data["Minimum Temperature (°C)"]
mean_temperature = data["Mean Temperature (°C)"]
max_temperature = data["Maximum Temperature (°C)"]

# Iterate through each column and plot it against the dates
columns = {
    "Total Rainfall": total_rainfall,
    "Mean Wind Speed": mean_wind_speed,
    "Mean Amount of Cloud": mean_cloud_amount,
    "Sun": sun,
    "Humidity": humidity,
    "Minimum Temperature": min_temperature,
    "Mean Temperature": mean_temperature,
    "Maximum Temperature": max_temperature
}

for column_name, column_data in columns.items():
    plt.plot(dates, column_data)
    plt.xlabel("Date")
    plt.ylabel(column_name)
    plt.title(f"{column_name} vs. Date")
    plt.xticks(rotation=45)

    # Customize the y-axis tick marks for specific columns
    if column_name == "Total Rainfall":
        plt.yticks([0, 50, 100, 150])
    elif column_name in ["Minimum Temperature", "Mean Temperature", "Maximum Temperature"]:
        plt.yticks([0, 50, 100])

    plt.tight_layout()
    plt.show()