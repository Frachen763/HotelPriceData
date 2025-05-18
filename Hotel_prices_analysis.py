import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/borgo/Desktop/KU Career/6th Sem/DAP Lab/hotel_analysis_full/data/bangalore.csv")

# Data Cleaning
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['Tax'] = df['Tax'].str.replace(',', '')
df['Tax'] = pd.to_numeric(df['Tax'], errors='coerce')
df['Total Price'] = df['Price'] + df['Tax']

# Convert distance to float (km or m)
df['Distance to Landmark (km)'] = df['Distance to Landmark'].str.replace(' km', '').str.replace(' m', '')
df['Distance to Landmark (km)'] = pd.to_numeric(df['Distance to Landmark (km)'], errors='coerce')

# ------------------------------
# 1. Average price by star rating
avg_price_by_star = df.groupby("Star Rating")["Price"].mean()
avg_price_by_star.plot(kind='bar', title="Average Price by Star Rating")
plt.ylabel("Average Price (INR)")
plt.xlabel("Star Rating")
plt.show()

# ------------------------------
# 2. Average rating by location
avg_rating_by_location = df.groupby("Location")["Rating"].mean().sort_values(ascending=False)
avg_rating_by_location.head(10).plot(kind='barh', title="Top 10 Locations by Avg Rating")
plt.xlabel("Average Rating")
plt.show()

# ------------------------------
# 3. Correlation between Reviews and Rating
sns.heatmap(df[["Reviews", "Rating"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation: Reviews vs Rating")
plt.show()

# ------------------------------
# 4. Price distribution
sns.boxplot(x=df["Price"])
plt.title("Price Distribution")
plt.show()

# ------------------------------
# 5. Tax vs Price scatter plot
subset = df[["Price", "Tax"]].dropna().head(50)
sns.scatterplot(data=subset, x='Price', y='Tax')
plt.title("Tax vs Price (Sample)")
plt.show()

# ------------------------------
# 6. Percentage of hotels by star rating
df["Star Rating"].value_counts(normalize=True).plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Hotel Distribution by Star Rating")
plt.ylabel("")
plt.show()

# ------------------------------
# 7. Most reviewed hotel
most_reviewed = df.loc[df["Reviews"].idxmax()]
print("Most Reviewed Hotel:")
print(most_reviewed[["Hotel Name", "Reviews", "Rating"]])

# ------------------------------
# 8. Most expensive hotel
most_expensive = df.loc[df["Total Price"].idxmax()]
print("\nMost Expensive Hotel:")
print(most_expensive[["Hotel Name", "Location", "Total Price"]])

# ------------------------------
# 9. Average price by rating
avg_price_by_rating = df.groupby("Rating")["Price"].mean()
avg_price_by_rating.plot(marker='o', title="Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Avg Price (INR)")
plt.show()

# ------------------------------
# 10. Average rating by landmark
landmark_ratings = df[df["Nearest Landmark"].notnull()].groupby("Nearest Landmark")["Rating"].mean()
landmark_ratings.head(10).plot(kind='barh', title="Top Landmarks by Avg Rating")
plt.xlabel("Average Rating")
plt.show()

# ------------------------------
# 11. Average distance to landmark
avg_distance = df["Distance to Landmark (km)"].mean()
print(f"\nAverage Distance to Nearest Landmark: {avg_distance:.2f} meters")

# ------------------------------
# 12. Count of 5-star hotels by location
five_star_locations = df[df["Star Rating"] == 5]["Location"].value_counts()
five_star_locations.head(10).plot(kind='bar', title="Top Locations with 5-Star Hotels")
plt.ylabel("Number of Hotels")
plt.show()

# ------------------------------
# 13. Rating description count
df["Rating Description"].value_counts().plot(kind='bar', title="Rating Descriptions")
plt.ylabel("Count")
plt.show()

# ------------------------------
# 14. Price stats by location
price_stats = df.groupby("Location")["Price"].agg(["min", "max", "mean"]).sort_values(by="mean", ascending=False)
price_stats["mean"].head(10).plot(kind='barh', title="Top 10 Locations by Avg Price")
plt.xlabel("Avg Price (INR)")
plt.show()

# ------------------------------
# 15. Expensive hotels with low ratings
expensive_low_rating = df[df["Price"] > 8000].sort_values("Rating")
sns.scatterplot(data=expensive_low_rating, x="Price", y="Rating", hue="Hotel Name", s=100)
plt.title("Expensive but Low-Rated Hotels")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
