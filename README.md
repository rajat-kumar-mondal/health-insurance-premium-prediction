# Health Insurance Premium Prediction

[![Live App](https://img.shields.io/badge/Live_App-Click_Here-blue)](https://healthinsurance-cost-predictor.streamlit.app/)

## 📌 Overview
This project is designed to predict health insurance premiums using machine learning techniques. The model analyzes key factors such as age, genetic risk, and other demographics to provide accurate premium estimates.

The web application, developed with **Streamlit**, offers an intuitive interface for users to enter relevant data and obtain premium predictions quickly.

## 🚀 Live Demo
Experience the live application here: [Health Insurance Cost Predictor](https://healthinsurance-cost-predictor.streamlit.app/)

## 📂 Project Structure
```
/
notebooks/
│   ├── 1_premium_prediction.ipynb                # Primary model development notebook
│   ├── 2_data_segment.ipynb                      # Data segmentation steps
│   ├── 3_premium_prediction_young.ipynb          # Prediction for young individuals
│   ├── 4_premium_prediction_rest.ipynb           # Prediction for rest of the population
│   ├── 5_premium_prediction_young_with_genetic_risk.ipynb  # Prediction for youth with genetic risk
│   ├── 6_premium_prediction_rest_with_genetic_risk.ipynb   # Prediction for rest with genetic risk
app/
│   ├── main.py                                   # Streamlit web application
│   ├── predictior.py                             # Prediction logic and functions
│   ├── requirements.txt                          # List of dependencies
artifacts/
│   ├── model_rest.joblib                         # Trained model for general population
│   ├── model_young.joblib                        # Trained model for young individuals
│   ├── scaler_rest.joblib                        # Scaler for general population data
│   ├── scaler_young.joblib                       # Scaler for young individual data
data/
│   ├── premiums.csv                              # Primary dataset
│   ├── more_data_with_genetic_risk/              # Dataset with genetic risk factors
│   │   ├── premiums_young_with_gr.csv
│   ├── segmented_data/                           # Segmented data for improved model training
│   │   ├── premiums_rest.csv
│   │   ├── premiums_young.csv
```

## ⚡ Features
- Accurate prediction of insurance premiums based on demographic and genetic risk factors
- Comprehensive data segmentation for improved prediction accuracy
- Interactive web interface for real-time premium prediction
- Optimized machine learning models for enhanced performance

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/health-insurance-premium-prediction.git
cd health-insurance-premium-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r app/requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app/main.py
```

## 📊 Dataset
- **`premiums.csv`**: Core dataset containing customer demographics and premium values
- **`segmented_data/`**: Segmented data for improved model efficiency and reduce error
- **`more_data_with_genetic_risk/`**: Extended dataset with genetic risk feature

## 📦 Libraries & Packages
The project utilizes the following key libraries:
- **pandas** – Data manipulation and analysis  
- **numpy** – Numerical computations  
- **matplotlib.pyplot & seaborn** – Data visualization   
- **scikit-learn**:
  - `train_test_split` – Splitting data into training and testing sets  
  - `MinMaxScaler` – Feature scaling  
  - `LinearRegression` – Regression model
  - `Ridge` - Ridge regression model   
  - `RandomizedSearchCV` – Hyperparameter tuning
  - `mean_squared_error` – Model evaluation metrics 
- **statsmodels**:
  - `variance_inflation_factor` – Detecting multicollinearity  
- **xgboost** – Gradient boosting model  
- **joblib**:
  - `dump` – Store the models and scaler objects
- **streamlit** - App user interface (UI)

## 🤖 Model Training & Evaluation
The model was trained with various techniques to improve prediction accuracy:
- **Data Preprocessing:**
  - Handling missing values through imputation strategies.
  - Encoding categorical variables using one-hot encoding.
  - Feature scaling with **MinMaxScaler**.
  - Removing multicollinearity using **Variance Inflation Factor (VIF)**.
  - **Data Segmentation**
    - Data segmentation for precise model building and error reduction.
- **Model Development:**
  - Models trained separately for:
    - **Young individuals (Age <= 25)**
    - **Rest population (Age > 25)**
    - **Both groups with genetic risk considerations**
- **Model Evaluation Metrices:**
  - **Accuracy**
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**

## 📈 Performance of the best model (i.e., XGBoost)
- **Young Model:**
  - **Accuracy:** 98.76%
  - **MSE:** 93545.52
  - **RMSE:** 305.85
  - **Extreme errors:** 2.48% (initially ~73%) [Note: The error has been reduced through error analysis and by considering genetic risk features.]

- **Rest Model:**
  - **Accuracy:** 99.70%
  - **MSE:** 243847.75
  - **RMSE:** 493.80
  - **Extreme errors:** 0.32%

