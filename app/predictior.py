import pandas as pd
import joblib

model_young = joblib.load("../artifacts/model_young.joblib")
model_rest = joblib.load("../artifacts/model_rest.joblib")
scaler_young = joblib.load("../artifacts/scaler_young.joblib")
scaler_rest = joblib.load("../artifacts/scaler_rest.joblib")

def normalized_risk(medical_history):
    risk_scores = {"diabetes": 6, "heart disease": 8, "high blood pressure": 6, "thyroid": 5, "no disease": 0, "none": 0}
    return (sum(risk_scores.get(d, 0) for d in medical_history.lower().split(" & ")) - 0) / (14 - 0)

def preprocess_input(input_dict):
    expected_columns = ['age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score', 'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried', 'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional', 'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed']
    df = pd.DataFrame(0, columns=expected_columns, index=[0])
    encodings = {"Insurance Plan": {'Bronze': 1, 'Silver': 2, 'Gold': 3}, "Gender": {'Male': 'gender_Male'}, "Region": {'Northwest': 'region_Northwest', 'Southeast': 'region_Southeast', 'Southwest': 'region_Southwest'}, "Marital Status": {'Unmarried': 'marital_status_Unmarried'}, "BMI Category": {'Obesity': 'bmi_category_Obesity', 'Overweight': 'bmi_category_Overweight', 'Underweight': 'bmi_category_Underweight'}, "Smoking Status": {'Occasional': 'smoking_status_Occasional', 'Regular': 'smoking_status_Regular'}, "Employment Status": {'Salaried': 'employment_status_Salaried', 'Self-Employed': 'employment_status_Self-Employed'}}
    for k, v in input_dict.items():
        if k in encodings and v in encodings[k]:
            if encodings[k][v] in df.columns:
                df[encodings[k][v]] = 1
        elif k == "Income in Lakhs":
            df['income_lakhs'] = v
        elif k in ["Insurance Plan", "Age", "Number of Dependants", "Genetical Risk"]:
            df[k.lower().replace(' ', '_')] = encodings.get(k, {}).get(v, v)
    df['normalized_risk_score'] = normalized_risk(input_dict['Medical History'])
    return handle_scaling(input_dict['Age'], df)

def handle_scaling(age, df):
    scaler_object = scaler_young if age <= 25 else scaler_rest
    df['income_level'] = None
    df[scaler_object['cols_to_scale']] = scaler_object['scaler'].transform(df[scaler_object['cols_to_scale']])
    df.drop('income_level', axis='columns', inplace=True)
    return df

def predict(input_dict):
    return int((model_young if input_dict['Age'] <= 25 else model_rest).predict(preprocess_input(input_dict))[0])
