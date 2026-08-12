import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Set up page config
st.set_page_config(page_title="PCOS Risk Assessment Tool", page_icon="🩺", layout="centered")

# App Header
st.title("🩺 PCOS Clinical Risk Screening Tool")
st.write("Adjust the patient clinical parameters below to assess predicted PCOS risk.")

# Load dataset and train model (cached so it runs fast)
@st.cache_resource
def load_and_train():
    df = pd.read_csv("pcos_dataset.csv")  # Adjust path if in 'data/pcos_dataset.csv'
    df.columns = df.columns.str.strip()
    
    X = df.drop(columns=['PCOS_Diagnosis'])
    y = df['PCOS_Diagnosis']
    
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X, y)
    return clf

model = load_and_train()

# --- Patient Input Form ---
st.header("📋 Patient Measurements")

col1, col2 = st.columns(2)

with col1:
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=24.5, step=0.1)
    menstrual = st.selectbox("Menstrual Irregularity", options=[0, 1], format_func=lambda x: "Yes (Irregular)" if x == 1 else "No (Regular)")
    age = st.slider("Age", min_value=18, max_value=50, value=28)

with col2:
    testosterone = st.number_input("Testosterone Level (ng/dL)", min_value=0.0, max_value=200.0, value=45.0, step=1.0)
    follicle_count = st.number_input("Antral Follicle Count", min_value=0, max_value=50, value=8, step=1)

# Predict Button
st.markdown("---")
if st.button("🔮 Calculate PCOS Risk", type="primary"):
    # Organize input into DataFrame matching training data format
    input_data = pd.DataFrame({
        'Age': [age],
        'BMI': [bmi],
        'Menstrual_Irregularity': [menstrual],
        'Testosterone_Level(ng/dL)': [testosterone],
        'Antral_Follicle_Count': [follicle_count]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100
    
    # Display Result
    st.subheader("Assessment Result")
    if prediction == 1:
        st.error(f"⚠️ **High Risk of PCOS Detected** (Confidence: {probability:.1f}%)")
        st.write("Clinical indicators suggest high likelihood of PCOS. Follow-up consultation is recommended.")
    else:
        st.success(f"✅ **Low Risk of PCOS** (Confidence: {100 - probability:.1f}%)")
        st.write("Clinical markers are within typical non-PCOS baseline ranges.")
