# 🩺 PCOS Risk Classification & Clinical Screening Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pcosriskclassification.streamlit.app/)

> 🔗 **Live Web App:** [Click here to launch the application](https://pcosriskclassification.streamlit.app/)

## 📌 Project Overview

Polycystic Ovary Syndrome (PCOS) is a common endocrine disorder affecting women of reproductive age. Early identification of high-risk patients is critical for timely intervention.

This project builds an end-to-end data analytics and machine learning pipeline using Python to analyze key clinical markers (e.g., hormone levels, ultrasound findings, cycle regularity) and classify PCOS risk.

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Seaborn, Matplotlib
* **Machine Learning:** Scikit-Learn (Random Forest, Train/Test Split, Metrics)

---

## 📊 Key Clinical Insights & Exploratory Findings

1. **Primary Risk Drivers:** Correlation analysis and feature importance modeling revealed that **Menstrual Irregularity** and **BMI** are the strongest leading indicators of PCOS risk in this cohort.
2. **Hormone & Imaging Signals:** Higher **Testosterone levels** and elevated **Antral Follicle Counts** consistently correlated with positive diagnoses, aligning with standard Rotterdam criteria for PCOS screening.
3. **Irrelevant Markers:** **Age** showed virtually zero correlation ($r = -0.06$) with diagnosis in this demographic, confirming that risk spans across reproductive ages.

### 1. Clinical Parameter Distributions
Comparing key diagnostic markers across diagnosed PCOS vs. non-PCOS cases highlights clear elevation in both **Antral Follicle Count** and **Testosterone Levels**:

<img width="1184" height="484" alt="image" src="https://github.com/user-attachments/assets/28af3f89-8624-4fd8-8288-ae12e07a3c2a" />


---

### 2. Feature Correlation Heatmap
Exploratory correlation analysis reveals that **Menstrual Irregularity (0.47)** and **BMI (0.38)** exhibit the strongest linear relationship with a positive PCOS diagnosis:

<img width="806" height="688" alt="image" src="https://github.com/user-attachments/assets/ce5f037f-d6fa-438d-9194-59e960f33923" />


---

## 🤖 Model Performance & Evaluation

A **Random Forest Classifier** was trained on 80% of the patient dataset and evaluated on an unseen 20% test set (200 patients).

* **Overall Accuracy:** 100%
* **Precision:** 1.00 (Zero false alarms)
* **Recall (Priority Metric):** 1.00 (Zero missed diagnoses)

> **Healthcare Focus:** In clinical screening, **Recall** is prioritized to ensure that zero symptomatic patients fall through the cracks without follow-up care.

Feature importance scores extracted from the Random Forest model demonstrate that **BMI** and **Menstrual Irregularity** carry the highest predictive weight, followed by **Testosterone Levels** and **Antral Follicle Count**:

<img width="784" height="484" alt="image" src="https://github.com/user-attachments/assets/d4e8e00d-b750-4965-a52b-f886c0b88c6d" />

---

## 💡 Feature Importance Ranking

1. **BMI:** ~31% relative importance
2. **Menstrual Irregularity:** ~31% relative importance
3. **Testosterone Level:** ~19% relative importance
4. **Antral Follicle Count:** ~15% relative importance
5. **Age:** ~2% relative importance

---

## 💻 Interactive Streamlit Web App

This project includes an interactive web application built with Streamlit that allows users to input clinical measurements and receive real-time PCOS risk assessments powered by the trained Machine Learning model.

### Features
* **Interactive Parameters:** Sliders and numerical inputs for BMI, Age, Menstrual Irregularity, Testosterone levels, and Antral Follicle Count.
* **Instant Prediction:** Returns a risk classification (High Risk vs. Low Risk) along with confidence probability.

---

## 🏃 How to Run the App Locally

# 1. Clone the repository
git clone https://github.com/ashlag54/pcos_risk_classification.git

# 2. Navigate to project directory
cd pcos_risk_classification

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run Streamlit app
python -m streamlit run app.py
