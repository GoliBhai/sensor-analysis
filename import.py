import csv

# Function to calculate the minimum, maximum, and average temperatures
def analyze_sensor_data(filename, threshold=23):
    temperatures = []
    time_stamps = []
    
    # Read the CSV file
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if it exists
        
        for row in reader:
            timestamp, node, temperature, humidity = row
            temperatures.append(float(temperature))
            time_stamps.append(timestamp)
    
    # Calculate Min, Max, and Average temperatures
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)
    
    print(f"Min Temperature: {min_temp}°C")
    print(f"Max Temperature: {max_temp}°C")
    print(f"Average Temperature: {avg_temp:.2f}°C")
    
    # Check for temperature spikes and alerts (temperature above threshold)
    print("\nAlerts:")
    for i, temp in enumerate(temperatures):
        if temp > threshold:
            print(f"Alert: Temperature above {threshold}°C at timestamp {time_stamps[i]} (Temperature: {temp}°C)")

        # Check for temperature spikes (define a spike as a sudden increase of 5°C or more)
        if i > 0 and temp - temperatures[i-1] > 5:
            print(f"Alert: Spike detected! Sudden increase of {temp - temperatures[i-1]}°C at timestamp {time_stamps[i]}")

# Path to your CSV file (adjust the path if needed)
filename = 'sensor_data.csv'

# Call the function to analyze the data
analyze_sensor_data(filename)
