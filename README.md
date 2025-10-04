# IPL Score Prediction - Machine Learning Project

## Project Overview

This project predicts the total score of a cricket team at the end of their innings during an IPL (Indian Premier League) match using Machine Learning. The model is trained on historical IPL data from seasons 1-9 (2008-2016) and tested on season 10 (2017).

## Table of Contents

- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Building](#model-building)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Work](#future-work)

## Dataset

**Source**: IPL Ball-by-Ball Dataset (2008-2017)

**Features**:
- Batting team
- Bowling team
- Overs completed
- Current runs scored
- Wickets fallen
- Runs in last 5 overs
- Wickets in last 5 overs
- Total score (target variable)
- Match date

**Dataset Size**: 53,811 rows × 23 columns (after preprocessing)

## Data Preprocessing

### 1. Data Cleaning
- Removed irrelevant columns: match ID, venue, batsman, bowler, striker, non-striker
- Filtered consistent teams only (8 teams)
- Removed first 5 overs of each match (insufficient historical data)
- Converted date column to datetime format

### 2. Feature Engineering
- **One-Hot Encoding**: Applied to batting and bowling team columns
- **Feature Selection**: Correlation analysis using heatmap

### 3. Train-Test Split
- **Training Set**: IPL Seasons 1-9 (2008-2016)
- **Test Set**: IPL Season 10 (2017)
- **Split Type**: Time-based split (not random)

## Model Building

### Models Evaluated

Four regression models were trained and evaluated:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**
4. **AdaBoost Regressor** (with Linear Regression as base)

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Model Performance

| Model | MAE | MSE | RMSE |
|-------|-----|-----|------|
| **Linear Regression** | **12.12** | **251.01** | **15.84** |
| AdaBoost | 12.08 | 244.80 | 15.65 |
| Random Forest | 13.86 | 337.23 | 18.36 |
| Decision Tree | 17.57 | 558.38 | 23.63 |

### Model Selection: Linear Regression

**Why Linear Regression?**
- RMSE of 15.84 (excellent performance)
- Only 0.19 RMSE difference from AdaBoost (marginal improvement not worth complexity)
- Simpler model - easier to deploy and interpret
- Faster prediction time
- No overfitting issues
- Production-ready

**Performance Interpretation**:
- On average, predictions are within **±15.84 runs** of actual scores
- For a typical IPL score of 160-180, this represents ~9% error
- Highly acceptable for real-world cricket score prediction

## #project-structure
ipl-score-prediction/
│
├── Dataset/
│   └── ipl.csv
│
├── ipl_score_prediction.ipynb    # Main notebook with all analysis
├── app.py                         # Streamlit web application
├── linear_regression_model.pkl   # Trained model (pickle file)
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies

## Run Streamlit App

- streamlit run app.py

### Prerequisites
```bash
Python 3.8+
pip
