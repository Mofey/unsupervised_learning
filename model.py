from sklearn.cluster import KMeans

def train_kmeans(data, n_clusters=3):
    """Trains a K-Means clustering model."""
    model = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = model.fit_predict(data)
    return model, clusters