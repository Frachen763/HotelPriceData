# Hotel Price Analysis in Indian Cities

This repository contains a complete analysis pipeline for the Hotel Price dataset of 42 Indian cities.

## Project Structure

```
hotel_analysis_full/
├── data/
│   └── hotel_prices.csv      # Hotel price data (place your dataset here)
├── data_loader.py            # Loads and preprocesses the data
├── eda.py                    # Exploratory Data Analysis scripts
├── visualization.py          # Scripts to generate visualizations
├── modeling.py               # Simple predictive modeling
├── utils.py                  # Helper functions
└── README.md                 # Project overview and instructions
```

## Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/hotel_analysis_full.git
   cd hotel_analysis_full
   ```

2. **Add the dataset**  
   Download the full CSV from Kaggle:
   https://www.kaggle.com/code/abdallabola/hotel-price-data-of-cities-in-india/input  
   Place the file as `data/hotel_prices.csv`.

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scripts**  
   - **Data Loading:** `python data_loader.py`  
   - **EDA:** `python eda.py`  
   - **Visualizations:** `python visualization.py`  
   - **Modeling:** `python modeling.py`  

## Requirements

- pandas
- numpy
- matplotlib
- scikit-learn

Feel free to extend the analysis with additional models or visualizations!
