# 🏨 Hotel Price Data of Cities in India

This project provides a starter template for analyzing hotel pricing data across Indian cities.

## 📂 Project Structure

```
hotel-price-analysis/
├── data/
│   └── hotel_prices.csv  # Place the downloaded dataset here
├── eda.py                # Starter script for exploratory data analysis
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and instructions
```

## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/hotel-price-analysis.git
   cd hotel-price-analysis
   ```

2. **Download the dataset**  
   Download the hotel price dataset from Kaggle:
   https://www.kaggle.com/code/abdallabola/hotel-price-data-of-cities-in-india/input  
   Place `hotel-price-data-of-cities-in-india.csv` into the `data/` folder and rename it to `hotel_prices.csv`.

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Exploratory Data Analysis**  
   ```bash
   python eda.py
   ```

## 🛠️ Starter Code (eda.py)

This script loads the data and prints some initial insights. Feel free to extend it with visualizations and modeling.

```python
import pandas as pd

def main():
    # Load dataset
    df = pd.read_csv('data/hotel_prices.csv')
    # Display basic information
    print("Dataset Shape:", df.shape)
    print(df.head())
    # Summary statistics
    print(df.describe())

if __name__ == '__main__':
    main()
```
