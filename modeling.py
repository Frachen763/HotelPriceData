from data_loader import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run_modeling(df):
    features = ['StarRating', 'IsMetroCity', 'IsTouristDestination', 'FreeWifi', 'FreeBreakfast', 'HasSwimmingPool']
    X = df[features]
    y = df['RoomRent']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"Test MSE: {mse:.2f}")

if __name__ == '__main__':
    df = load_data()
    run_modeling(df)
