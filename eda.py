from data_loader import load_data

def run_eda(df):
    # Basic shape and stats
    print('Dataset shape:', df.shape)
    print('\nSummary statistics:')
    print(df.describe(include='all'))

    # Count of hotels per city
    print('\nHotels per city:')
    print(df['CityName'].value_counts().head())

if __name__ == '__main__':
    df = load_data()
    run_eda(df)
