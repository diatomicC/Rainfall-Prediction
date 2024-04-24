import pandas as pd

# Load the data from the CSV file
file_path = '/Users/diatomicc/Desktop/SEEM3650/Daily Temperature data.csv'
data = pd.read_csv(file_path)

# Clean up the column names if necessary (it looks like you might not need this step, but it's here just in case)
data.columns = [col.strip() for col in data.columns]

# Extract the relevant columns for each type of temperature
# The data likely starts from the second column ('Unnamed: 1' corresponds to 'Year', 'Unnamed: 2' to 'Month', etc.)
# Adjusting column references according to your index output
max_temp = data[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Maximum Temperature (°C)']].copy()
min_temp = data[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Minimum Temperature (°C)']].copy()
mean_temp = data[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Mean Temperature (°C)']].copy()

# Rename the columns in each DataFrame to be more understandable
max_temp.columns = ['Year', 'Month', 'Day', 'Maximum Temperature (°C)']
min_temp.columns = ['Year', 'Month', 'Day', 'Minimum Temperature (°C)']
mean_temp.columns = ['Year', 'Month', 'Day', 'Mean Temperature (°C)']

# Save each DataFrame to a new CSV file
max_temp.to_csv('/Users/diatomicc/Desktop/SEEM3650/Maximum_Temperature.csv', index=False)
min_temp.to_csv('/Users/diatomicc/Desktop/SEEM3650/Minimum_Temperature.csv', index=False)
mean_temp.to_csv('/Users/diatomicc/Desktop/SEEM3650/Mean_Temperature.csv', index=False)
