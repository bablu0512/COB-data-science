import requests
import pandas as pd

# Define the API URL
api_url = "https://api.binance.com/api/v3/ticker/24hr"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Convert the JSON response to a Python data structure
    df = pd.DataFrame(data)  # Convert the data to a Pandas DataFrame
else:
    print("Failed to fetch data from the API")
    exit()

# Define the name for the CSV file
csv_filename = "binance_data.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_filename, index=False)
print(f"Data has been saved to {csv_filename}")
