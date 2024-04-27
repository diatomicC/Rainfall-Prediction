import pandas as pd

# Load the CSV files
path_to_rainfall = '/Users/diatomicc/Desktop/SEEM3650/Rainfall.csv'
path_to_windspeed = '/Users/diatomicc/Desktop/SEEM3650/WindSpeed.csv'
path_to_cloudamount = '/Users/diatomicc/Desktop/SEEM3650/CloudAmount.csv'
path_to_dailytemp = '/Users/diatomicc/Desktop/SEEM3650/Daily Temperature data.csv'
path_to_sunlight = '/Users/diatomicc/Desktop/SEEM3650/Sunlight.csv'
path_to_humidity = '/Users/diatomicc/Desktop/SEEM3650/Humidity.csv'
path_to_mintemp = '/Users/diatomicc/Desktop/SEEM3650/MinimumTemperature.csv'
path_to_meantemp = '/Users/diatomicc/Desktop/SEEM3650/MeanTemperature.csv'
path_to_maxtemp = '/Users/diatomicc/Desktop/SEEM3650/MaximumTemperature.csv'

rainfall = pd.read_csv(path_to_rainfall)
windspeed = pd.read_csv(path_to_windspeed)
cloudamount = pd.read_csv(path_to_cloudamount)

sun = pd.read_csv(path_to_sunlight)
humidity = pd.read_csv(path_to_humidity)

mintemperature = pd.read_csv(path_to_mintemp)
meantemperature = pd.read_csv(path_to_meantemp)
maxtemperature = pd.read_csv(path_to_maxtemp)

# Merge the dataframes on the 'Year', 'Month', and 'Day' columns  Maximum Temperature (°C)""",,"Minimum Temperature (°C)""",,"Mean Temperature (°C)"
from functools import reduce
data_frames = [rainfall, windspeed, cloudamount, sun, humidity, mintemperature, meantemperature, maxtemperature]
merged_data = reduce(lambda left, right: pd.merge(left, right, on=['Year', 'Month', 'Day']), data_frames)

# Convert 'Year', 'Month', 'Day' to a 'Date' column
merged_data['Date'] = pd.to_datetime(merged_data[['Year', 'Month', 'Day']])

# Drop the original 'Year', 'Month', 'Day' columns if not needed
merged_data.drop(['Year', 'Month', 'Day'], axis=1, inplace=True)

# Reorder columns to match requested format and keep the 'Date' column
column_order = ['Date', 'Total Rainfall (mm)', 'Mean Wind Speed (km/h)', 'Mean Amount of Cloud (%)', 'Sun', 'Humidity', 'Minimum Temperature (°C)', 'Mean Temperature (°C)', 'Maximum Temperature (°C)']
merged_data = merged_data[column_order]

# Save the merged data to a new CSV file
merged_data.to_csv('/Users/diatomicc/Desktop/SEEM3650/Training.csv', index=False)

print("Data has been successfully merged and saved.")