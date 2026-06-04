import joblib
import pandas as pd

model = joblib.load("model.pkl")

sample = pd.DataFrame({
    "Pregnancies": [2],
    "Glucose": [120],
    "BloodPressure": [70],
    "SkinThickness": [20],
    "Insulin": [85],
    "BMI": [28.5],
    "DiabetesPedigreeFunction": [0.35],
    "Age": [35]
})

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Diabetic")
else:
    print("Not Diabetic")

