# Sickle Cell Risk Prediction System

## Overview

The Sickle Cell Risk Prediction System is a machine learning web application developed to predict the risk level of sickle cell disease using patient clinical information.

The application was built using Streamlit and an XGBoost classifier. Users can enter patient information, predict the risk level, view the prediction probabilities, and download the results as PDF, CSV, or Excel.

The model predicts one of three risk levels:

* Low
* Medium
* High

---

## Dataset

A public dataset was used for this project.

Dataset information:

* Number of rows: 100,000
* Number of columns: 9

Target Variable:

* Risk Level

The target variable contains three classes:

* Low
* Medium
* High

The features used for prediction are:

* Age
* Sex
* HB Level
* WBC
* Pain Score
* Crisis Last 6 Months

Patient ID and Genotype were removed during preprocessing because they were not used for prediction and could introduce data leakage(genotype).

---

## Data Preprocessing

The following preprocessing steps were performed:

* Selected the relevant features
* Split the data into training and testing sets
* Applied One Hot Encoding to the categorical feature
* Applied StandardScaler to the numerical features
* Used SMOTE to address class imbalance
* Used class weights during model training
* Built a preprocessing pipeline for model training

---

## Models Trained

The following machine learning models were trained and evaluated:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

The final deployed model is **XGBoost**, selected based on its Weighted F1 Score and overall performance.

---

## Model Performance

The model was evaluated using several classification metrics.

| Metric | Score |
|---------|------:|
| **Weighted F1 Score** | **95.99%** |
| Weighted Precision | 96.14% |
| Weighted Recall | 95.00% |
| Cross Validation Score | 95.79% |

The close agreement between the model performance and the cross validation score indicates that the model generalizes well to unseen data.

---

## Application Features

The application allows users to:

* Enter patient clinical information
* Predict sickle cell risk level
* View prediction probabilities for all three classes
* Download prediction reports as PDF
* Export results as CSV
* Export results as Excel

---

## Project Structure

```text
Sickle Cell Risk Prediction System

│── app.py
│── sickle_cell_model.pkl
│── requirements.txt
│── style.css
│── README.md

└── pages
    ├── prediction.py
    └── result.py
```

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit Learn
* XGBoost
* ReportLab
* OpenPyXL
* Joblib

---

## How to Run

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

# Team Members

| Name | Registration Number |
|------|---------------------|
| OLANIYI OLUWATOSIN PETER | ARI/2026/TC-7/0430 |
| ADEBESIN GREATNESS | ARI/2026/TC-7/0310 |
| ADETOLA OLAMIDE ISSAC | ARI/2026/TC-7/0005 |
| ASAMOAH FESTUS | ARI/2026/TC-7/0329 |
| IBRAHIM BARNABAS GAGO | ARI/2026/TC-7/0299 |
| OSEIWE CLEVERSON OJIEIFOH | ARI/2026/TC-7/0193|
| RAYMOND IZUKA | ARI/2026/TC-7/0408 |
| SAMBO BASHIR | ARI/2026/TC-7/0043|
| IBUKUN AKINMOLADUN | ARI/2026/TC-7/0268|
| BAKARE MUHAMMAD | ARI/2026/TC-7/0285|
| BRIDGET DATONYE | ARI/2026/TC-7/0534|
| MUSTAPHA NASIR | ARI/2026/TC-7/0498 |
| ADEDEJI AYODELE ODEWALE | ARI/2026/TC-7/ |
| DAVOU BULUS DANDI | ARI/2026/TC-7/ |
| IBRAHIM ABDULLAH ABEFE | ARI/2026/TC-7/0450 |

---

## Disclaimer

This application is developed for educational and research purposes. The prediction results are intended to support learning and should not replace professional medical diagnosis or clinical judgment.
