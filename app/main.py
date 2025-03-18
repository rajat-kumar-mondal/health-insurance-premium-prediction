import streamlit as st
from predictior import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", page_icon="🛡️", layout="wide")  # Set full-screen layout with title and icon
st.title('🛡️ Health Insurance Cost Predictor')
st.markdown('#')

categorical_options = {
    'Gender': ['Male', 'Female'], 'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': ['No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
                        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                        'Diabetes & Heart disease'],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

inputs = [
    ('Age', 18, 100), ('Number of Dependants', 0, 20),
    ('Income in Lakhs', 0, 200), ('Genetical Risk', 0, 5),
    ('Insurance Plan', categorical_options['Insurance Plan']),
    ('Employment Status', categorical_options['Employment Status']),
    ('Gender', categorical_options['Gender']),
    ('Marital Status', categorical_options['Marital Status']),
    ('BMI Category', categorical_options['BMI Category']),
    ('Smoking Status', categorical_options['Smoking Status']),
    ('Region', categorical_options['Region']),
    ('Medical History', categorical_options['Medical History'])
]

values = {}
cols = st.columns(4)
for idx, (label, *opts) in enumerate(inputs):
    with cols[idx % 4]:
        if isinstance(opts[0], list):
            values[label] = st.selectbox(f'**{label}**', opts[0])
        else:
            values[label] = st.number_input(f'**{label}**', min_value=opts[0], max_value=opts[1], step=1)

if st.button('Predict'):
    prediction = predict(values)
    st.success(f'**Predicted Health Insurance Cost**: {prediction}')
