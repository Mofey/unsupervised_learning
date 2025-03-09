import pandas as pd

def load_data(file_path):
    """Loads dataset from a CSV file."""
    return pd.read_csv(file_path)