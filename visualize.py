import matplotlib.pyplot as plt

def plot_clusters(data, clusters):
    """Plots the clustered data."""
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=clusters, cmap='viridis')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Customer Segments')
    plt.show()