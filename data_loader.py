import pandas as pd

def load_data(path='data/hotel_prices.csv'):
    """Load hotel prices data from CSV."""
    df = pd.read_csv(path, parse_dates=['Date'])
    print(f"Loaded {len(df)} records.")
    return df

if __name__ == '__main__':
    df = load_data()
    print(df.info())
