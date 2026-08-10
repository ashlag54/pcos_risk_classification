# 🩺 PCOS Clinical Risk Classification & Feature Analysis

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

---

## 🤖 Model Performance & Evaluation

A **Random Forest Classifier** was trained on 80% of the patient dataset and evaluated on an unseen 20% test set (200 patients).

* **Overall Accuracy:** 100%
* **Precision:** 1.00 (Zero false alarms)
* **Recall (Priority Metric):** 1.00 (Zero missed diagnoses)

> **Healthcare Focus:** In clinical screening, **Recall** is prioritized to ensure that zero symptomatic patients fall through the cracks without follow-up care.

---

## 💡 Feature Importance Ranking

1. **BMI:** ~31% relative importance
2. **Menstrual Irregularity:** ~31% relative importance
3. **Testosterone Level:** ~19% relative importance
4. **Antral Follicle Count:** ~15% relative importance
5. **Age:** ~2% relative importance

