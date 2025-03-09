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

from data_loader import load_data
from preprocess import preprocess_data
from model import train_kmeans
from visualize import plot_clusters

if __name__ == "__main__":
    df = load_data('customers.csv')
    data = preprocess_data(df)
    model, clusters = train_kmeans(data)
    plot_clusters(data, clusters)
