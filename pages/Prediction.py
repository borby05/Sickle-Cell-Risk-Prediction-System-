import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Sickle Cell Risk Prediction")

st.write(
    """
Enter the patient's information below to estimate the risk level using the trained XGBoost model.
"""
)

RISK_LABELS = {
    0: "Low",
    1: "Medium",
    2: "High"
}

st.markdown("---")

st.subheader("Patient Information")

left, right = st.columns(2)

with left:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=25
    )

    pain_score = st.slider(
        "Pain Score",
        min_value=0,
        max_value=10,
        value=5
    )

    wbc = st.number_input(
        "WBC",
        min_value=3000.0,
        max_value=33000.0,
        step=100.0
    )

with right:

    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    crisis = st.number_input(
        "Crisis Last 6 Months",
        min_value=0,
        max_value=6,
        value=0
    )

    hb = st.number_input(
        "Hb Level",
        min_value=0.0,
        max_value=17.0,
        step=0.1
    )

st.markdown("---")

predict = st.button(
    "🔍 Predict Risk",
    use_container_width=True
)

if predict:

    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "HB_Level": [hb],
        "WBC": [wbc],
        "Crisis_Last_6M": [crisis],
        "Pain_Score": [pain_score]
    })

    # calling the model to make predictions
    model = joblib.load("sickle_cell_model.pkl")

    prediction = model.predict(input_data)[0]

    risk_level = RISK_LABELS[int(prediction)]

    probabilities = model.predict_proba(input_data)[0]

    classes = model.classes_

    probability_dict = {RISK_LABELS[int(cls)]: prob
    for cls, prob in zip(classes, probabilities)}

    # Save to session state
    st.session_state["patient_data"] = input_data
    st.session_state["prediction"] = risk_level
    st.session_state["probabilities"] = probability_dict

    st.success("Prediction completed successfully.")

if st.button("View Full Report"):
    st.switch_page("pages/Result.py")
