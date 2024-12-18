import numpy as np

# Simulate temperature data for a week (7 days, 3 times a day: morning, afternoon, evening)
# Temperatures in degrees Celsius
temperature_data = np.array([
    [15, 20, 18],  # Day 1
    [16, 22, 19],  # Day 2
    [14, 21, 17],  # Day 3
    [15, 19, 16],  # Day 4
    [13, 18, 15],  # Day 5
    [12, 17, 14],  # Day 6
    [14, 20, 16],  # Day 7
])

# Slicing and indexing: Get temperatures for the 1st day (row 0)
day_1_temps = temperature_data[0]
print("Day 1 temperatures:", day_1_temps)

# Slicing: Get afternoon temperatures for all days (column 1)
afternoon_temps = temperature_data[:, 1]
print("Afternoon temperatures for all days:", afternoon_temps)

# Shaping: Get the shape of the array
print("Original shape:", temperature_data.shape)

# Reshaping: Flatten the array to 1D
flattened_data = temperature_data.reshape(-1)
print("Flattened data:", flattened_data)

# Reshaping: Reshape to 3 rows and 7 columns
reshaped_data = temperature_data.reshape(3, 7)
print("Reshaped data (3x7):\n", reshaped_data)

# Statistical calculations
# Mean temperature for the week
mean_temp = np.mean(temperature_data)
print("Mean temperature for the week:", mean_temp)

# Mean temperature for each time of day (columns)
mean_temp_time_of_day = np.mean(temperature_data, axis=0)
print("Mean temperature for each time of day (morning, afternoon, evening):", mean_temp_time_of_day)

# Max temperature for each day
max_temp_per_day = np.max(temperature_data, axis=1)
print("Max temperature for each day:", max_temp_per_day)

# Min temperature for each day
min_temp_per_day = np.min(temperature_data, axis=1)
print("Min temperature for each day:", min_temp_per_day)

# Standard deviation of temperatures
std_dev = np.std(temperature_data)
print("Standard deviation of temperatures:", std_dev)

# Identify the highest temperature in the week and its position
max_temp = np.max(temperature_data)
max_temp_position = np.unravel_index(np.argmax(temperature_data), temperature_data.shape)
print(f"Highest temperature: {max_temp} at position (day {max_temp_position[0] + 1}, time index {max_temp_position[1]})")
