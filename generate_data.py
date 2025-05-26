import sys
sys.dont_write_bytecode = True

import pandas as pd
import random

# Set the seed for reproducibility
def generate_data(num_customers=10):
    """Generates a sample customer dataset with random values."""
    data = {
        'CustomerID': list(range(1, num_customers + 1)),
        'Gender': [random.choice(['Male', 'Female']) for _ in range(num_customers)],
        'Age': [random.randint(18, 70) for _ in range(num_customers)],
        'Annual Income (k$)': [random.randint(15, 100) for _ in range(num_customers)],
        'Spending Score (1-100)': [random.randint(1, 100) for _ in range(num_customers)]
    }
    return data

def save_data_to_csv(data, file_path):
    """Saves the dataset to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Generate the data
    data_dict = generate_data(num_customers=10)
    
    # Save the data to a CSV file
    csv_file_path = 'customers.csv'
    save_data_to_csv(data_dict, csv_file_path)
    print(f"Data has been generated and saved to {csv_file_path}")