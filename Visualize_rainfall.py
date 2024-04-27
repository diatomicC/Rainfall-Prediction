import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("Training.csv")

# Extract the required columns
total_rainfall = data["Total Rainfall (mm)"]
mean_wind_speed = data["Mean Wind Speed (km/h)"]
mean_cloud_amount = data["Mean Amount of Cloud (%)"]
sun = data["Sun"]
humidity = data["Humidity"]
min_temperature = data["Minimum Temperature (°C)"]
mean_temperature = data["Mean Temperature (°C)"]
max_temperature = data["Maximum Temperature (°C)"]

# Create a dictionary of column data
columns = {
    "Mean Wind Speed": mean_wind_speed,
    "Mean Amount of Cloud": mean_cloud_amount,
    "Sun": sun,
    "Humidity": humidity,
    "Minimum Temperature": min_temperature,
    "Mean Temperature": mean_temperature,
    "Maximum Temperature": max_temperature
}

# Iterate through each column and plot it against Total Rainfall
for column_name, column_data in columns.items():
    plt.plot(column_data, total_rainfall, 'o')
    plt.xlabel(column_name)
    plt.ylabel("Total Rainfall (mm)")
    plt.title(f"{column_name} vs. Total Rainfall")
    plt.tight_layout()
    plt.show()