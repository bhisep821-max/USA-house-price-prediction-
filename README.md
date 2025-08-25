# USA-house-price-prediction-
This project combines statistical data analysis and machine learning to analyze and predict house prices in the USA.

It has two main parts:

Descriptive Statistics (prashant_stats.py)

Custom function to calculate summary statistics, distribution checks, and confidence intervals.

House Price Prediction (USA house Predication pkl file test.py)

Uses a trained regression model (USA house price pred model 100k rnse 25.08.2025.pkl) to predict house prices based on input features.

Dataset used: USA_Housing.csv (from Kaggle).


Part 1: Statistical Analysis
Run the prashant_stats.py script to calculate statistics on any dataset/array:
from prashant_stats import cal_stats

Part 2: House Price Prediction

Run the prediction script:

python "USA house Predication pkl file test.py"


It will ask for user input:

What is your income: 55000
What is your age: 45
What is your number of rooms: 6
What is your number of bedrooms: 3
What is your area population: 30000


Output Example:

Your house can be sold between $350000 to $450000

Dataset

File: USA_Housing.csv

Columns:

Avg. Area Income

Avg. Area House Age

Avg. Area Number of Rooms

Avg. Area Number of Bedrooms

Area Population

Price (Target Variable)
