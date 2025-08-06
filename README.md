# ⚡ Energy Consumption Predictor

This project is a machine learning regression model that predicts **daily energy consumption (in kWh)** based on several building-related and environmental inputs. The model is trained on a dataset of 1,000 entries and deployed using **Streamlit** for real-time, interactive predictions.
Try the model on Streamlit cloud:

https://energyconsumptionpredictor-o.streamlit.app

---

## 📊 Dataset Overview

- **Source**: Kaggle dataset  
- **Size**: 1,000 entries × 7 columns  
- **Target Variable**: Daily energy consumption (continuous value in kWh)
### Features:

| Feature             | Description                      |
|---------------------|---------------------------------|
| 🏢 Building Type     | Residential, Commercial, etc.   |
| 📐 Square Footage    | Size of the building             |
| 👥 Number of Occupants | People inside the building       |
| 🔌 Appliances Used   | Count of appliances used         |
| 🌡️ Average Temperature | Daily average temperature        |
| 📅 Day of Week      | Day (Weekday/Weekend)            |

---


## 🎯 Objective

Predict the total energy usage for a building in a given day using the most relevant lifestyle and structural features. This regression-based approach helps building managers and residents make informed energy decisions.

---

## ⚙️ Model Training

### Algorithms Explored:
- Linear Regression
- Random Forest
- XGBoost
- **LightGBM ✅ (Best)**

### ✅ Best Model: LightGBM
- **Accuracy**: Over 80%

---

## 📈 Evaluation

- During training: MAE, RMSE, and R² score used for validation
- In the Streamlit app: Simplified result showing predicted energy usage in **kWh** along with r2 score

---

## 🛠 Feature Engineering

- One-hot encoding of categorical variables (e.g., Building Type, Day of Week)
- Normalization of numerical features (if applicable)
- Dropping irrelevant fields (if any)

---

## 🚀 Deployment

- The trained LightGBM model is saved as a `.joblib` file
- Integrated into a **Streamlit** web app
- Takes real-time input and displays the **predicted energy consumption**

---

## ✅ Model Strengths

- High predictive accuracy
- Fast inference using LightGBM
- No major limitations observed during evaluation

---

## 📬 Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

📧 **rakhmonovbb@gmail.com**
# energy_consumption_predictor
