# Hotel Price Analysis in Indian Cities

## 📖 Project Overview
This repository provides a comprehensive analysis pipeline for the "Hotel Price Data of Cities in India" dataset. It includes data loading, exploratory data analysis, visualizations, and a basic predictive model to understand factors influencing hotel room pricing.

## 📊 Dataset Details

- **Source:** Kaggle – [Hotel Price Data of Cities in India](https://www.kaggle.com/code/abdallabola/hotel-price-data-of-cities-in-india/input)
- **Total Records:** 13,232 hotel listings
- **Cities Covered:** 42 major Indian cities (e.g., Delhi, Mumbai, Bangalore, Goa, Jaipur)

### 🗂 Columns Description

| Column               | Type      | Description                                                       |
|----------------------|-----------|-------------------------------------------------------------------|
| `CityName`           | string    | Name of the city                                                  |
| `Population`         | integer   | City's population                                                |
| `CityRank`           | integer   | Rank by population size                                           |
| `IsMetroCity`        | binary    | 1 if city is a metro, 0 otherwise                                 |
| `IsTouristDestination` | binary  | 1 if city is a tourist destination, 0 otherwise                  |
| `IsWeekend`          | binary    | 1 if booking date falls on a weekend, 0 otherwise                |
| `IsNewYearEve`       | binary    | 1 if booking date is New Year's Eve, 0 otherwise                 |
| `Date`               | date      | Date of booking (YYYY-MM-DD)                                      |
| `HotelName`          | string    | Name of the hotel                                                 |
| `RoomRent`           | integer   | Price per night in INR                                            |
| `StarRating`         | float     | Hotel star rating (1-5)                                           |
| `Airport`            | float     | Distance to the nearest airport (in kilometers)                   |
| `FreeWifi`           | binary    | 1 if free Wi-Fi is available, 0 otherwise                        |
| `FreeBreakfast`      | binary    | 1 if free breakfast is available, 0 otherwise                    |
| `HotelCapacity`      | integer   | Number of rooms available                                         |
| `HasSwimmingPool`    | binary    | 1 if hotel has a swimming pool, 0 otherwise                      |

## 🏗️ Project Structure

```
hotel_analysis_full/
├── data/
│   └── hotel_prices.csv      # Raw dataset file
├── data_loader.py            # Load and preprocess data
├── eda.py                    # Exploratory Data Analysis
├── visualization.py          # Visualization scripts
├── modeling.py               # Predictive modeling
├── utils.py                  # Helper functions
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview and instructions
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hotel_analysis_full.git
   cd hotel_analysis_full
   ```

2. **Add the dataset**
   - Download from Kaggle: https://www.kaggle.com/code/abdallabola/hotel-price-data-of-cities-in-india/input
   - Place the file as `data/hotel_prices.csv`.

3. **Create a virtual environment & install dependencies**
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Data Loading**
   ```bash
   python data_loader.py
   ```
2. **Exploratory Data Analysis**
   ```bash
   python eda.py
   ```
3. **Generate Visualizations**
   ```bash
   python visualization.py
   ```
4. **Run Modeling**
   ```bash
   python modeling.py
   ```

## 📈 Quick Dataset Insights

- **Average Room Rent:** ₹5,474
- **Median Room Rent:** ₹4,000
- **Min Room Rent:** ₹299
- **Max Room Rent:** ₹322,500
- **Average Star Rating:** 3.46
- **Hotels with Free Wi-Fi:** ~92.6%
- **Hotels with Free Breakfast:** ~64.9%
- **Hotels with Swimming Pool:** ~35.6%

## 📝 Notes

- Feel free to extend the EDA with advanced visualizations.
- Replace or extend `modeling.py` with other ML algorithms.
- Contributions are welcome!

---

*Prepared on May 18, 2025*

## 🙌 Credits

- **Name:** Frachen Borgohain  
- **Roll No.:** ET22BTHCS014  
- **Branch:** CSE, Semester VI
