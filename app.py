import streamlit as st
import pandas as pd
import joblib
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)
img = get_base64("diabetes web image.webp")
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/webp;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
<style>
h1 {
    color: navy;
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}

label {
    color: navy;
    font-weight: bold;
}

/* Semi-transparent input boxes */
.stNumberInput input {
    background-color: rgba(255, 255, 255, 0.5) !important;
    color: black !important;
    border-radius: 10px;
}
            
</style>
""", unsafe_allow_html=True)

model = joblib.load("model.pkl")
st.markdown(page_bg, unsafe_allow_html=True)
model=joblib.load("model.pkl")
model = joblib.load("model.pkl")
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.markdown(page_bg, unsafe_allow_html=True)

st.markdown(
    "<h1 style='color:purple; text-align:center;'>🩺 Diabetes Prediction System</h1>",
    unsafe_allow_html=True
)
st.metric("Model Accuracy", "79%")
st.sidebar.title("About Project")

st.sidebar.info("""
This Diabetes Prediction System uses
Machine Learning to predict whether
a person is at risk of diabetes.

Technologies Used:
- Python
- Streamlit
- Pandas
- Scikit-Learn
- Random Forest
""")
col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("Pregnancies")
    glucose = st.number_input("Glucose")
    bp = st.number_input("Blood Pressure")
    skin = st.number_input("Skin Thickness")

with col2:
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI")
    dpf = st.number_input("Diabetes Pedigree Function")
    age = st.number_input("Age")

if st.button("🔍 Predict Diabetes Risk"):
    sample = pd.DataFrame({
        "Pregnancies": [preg],
        "Glucose": [glucose],
        "BloodPressure": [bp],
        "SkinThickness": [skin],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [dpf],
        "Age": [age]
    })

    prediction = model.predict(sample)

    if prediction[0] == 1:
       st.error("⚠️ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk of Diabetes")