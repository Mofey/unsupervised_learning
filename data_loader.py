import pandas as pd

def load_data():
    """Generates a sample customer dataset."""
    data = {
        'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female', 'Female', 'Male', 'Female'],
        'Age': [19, 21, 20, 23, 31, 22, 35, 23, 64, 30],
        'Annual Income (k$)': [15, 15, 16, 16, 17, 17, 18, 18, 19, 19],
        'Spending Score (1-100)': [39, 81, 6, 77, 40, 76, 6, 94, 3, 72]
    }
    return pd.DataFrame(data)

def load_csv(file_path='customers.csv'):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(file_path)