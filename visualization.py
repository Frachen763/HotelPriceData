import matplotlib.pyplot as plt
from data_loader import load_data

def plot_distribution(df):
    plt.figure()
    df['RoomRent'].hist(bins=50)
    plt.title('Distribution of Room Rent')
    plt.xlabel('Room Rent (INR)')
    plt.ylabel('Frequency')
    plt.show()

def plot_star_rating(df):
    plt.figure()
    df.groupby('StarRating')['RoomRent'].mean().plot(kind='bar')
    plt.title('Average Room Rent by Star Rating')
    plt.xlabel('Star Rating')
    plt.ylabel('Average Room Rent')
    plt.show()

if __name__ == '__main__':
    df = load_data()
    plot_distribution(df)
    plot_star_rating(df)
