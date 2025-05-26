# Customer Segmentation using K-Means (Unsupervised Learning)

"""
This project applies K-Means clustering to segment customers based on annual income and spending scores.
It follows a modular structure to ensure separation of concerns.

Modules:
- install_requirements.py: Install necessary libraries
- data_loader.py: Load dataset
- preprocess.py: Clean and preprocess data
- model.py: Train K-Means model
- visualize.py: Plot the clusters
- main.py: Run the full pipeline
"""

import sys
sys.dont_write_bytecode = True

from data_loader import load_csv, load_data
from preprocess import preprocess_data
from model import train_kmeans
from visualize import plot_clusters

if __name__ == "__main__":
    # Load the data
    try:
        df = load_csv()
    except:
        print("CSV file not found. Loaded sample data.")
        df = load_data()

    # Preprocess the data
    data = preprocess_data(df)

    # Train the K-Means model and plot the clusters
    model, clusters = train_kmeans(data)
    plot_clusters(data, clusters)