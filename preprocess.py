def preprocess_data(df):
    """Cleans and preprocesses the dataset."""
    df = df.dropna()
    df = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    return df