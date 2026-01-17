# Data pipeline
import pandas as pd # Import pandas for data manipulation
import sys # Import sys module to access command-line arguments

print("arguments", sys.argv) # Print the list of command-line arguments
month = int(sys.argv[1]) # Convert the first argument to an integer representing the month
print(f"Running pipeline for month {month}") # Print which month's pipeline is being run

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "day" : [1,2],
        "num_passengers" : [3,4]
    }
)

df['month'] = month # Add a 'month' column to the DataFrame using the command-line argument
print(df.head()) # Print the first few rows of the DataFrame

df.to_parquet(f"output_{month}.parquet")
