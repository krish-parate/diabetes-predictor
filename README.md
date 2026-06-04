#  Diabetes Prediction System
A Machine Learning-powered web application that predicts whether a person is likely to have diabetes based on health-related parameters.

##  Project Overview
This project uses a trained Machine Learning model to analyze user health data and predict the likelihood of diabetes. The application is built with Streamlit for an interactive and user-friendly interface.

##  Features
- User-friendly web interface
- Real-time diabetes prediction
- Machine Learning-based analysis
- Fast and accurate results
- Simple health parameter input form

##  Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

##  Project Structure
diabetes-predictor/
│
├── app.py                 # Streamlit web application
├── predict.py             # Prediction logic
├── train.py               # Model training script
├── diabetes_prediction.py # ML workflow
├── diabetes.csv           # Dataset
├── model.pkl              # Trained model
├── metrics.pkl            # Model metrics
├── requirement.txt        # Project dependencies
├── README.md              # Project documentation
```

##  Dataset
The model is trained on a diabetes dataset containing various health indicators such as:
- Glucose Level
- Blood Pressure
- BMI
- Insulin
- Age
- Pregnancies
- Skin Thickness

##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/krish-parate/diabetes-predictor.git
cd diabetes-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirement.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

##  How It Works
1. Enter health parameters.
2. Click the Predict button.
3. The model processes the input.
4. The application displays the prediction result.

##  Machine Learning Workflow
- Data Collection
- Data Preprocessing
- Model Training
- Model Evaluation
- Prediction Deployment using Streamlit

##  Author
**Krish Parate**
LinkedIn: linkdin.com/in/krish-parate

##  Support
If you found this project useful, consider giving it a star on GitHub!
