import joblib
import pandas as pd

# Load model and preprocessor

model = joblib.load("models/churn_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

threshold = 0.55

def predict_churn(customer_data):
    # Convert dictionary into DataFrame 
    df = pd.DataFrame([customer_data])

    # Apply preprocessing
    processed_data = preprocessor.transform(df)

    # Get churn probability 
    probability = model.predict_proba( processed_data )[0][1]

    # Apply optimized threshold 
    prediction = ( "Yes" if probability >= threshold else "No" )

    return prediction, probability

sample_customer = {
"gender": "Female",
"SeniorCitizen": 0,
"Partner": "Yes",
"Dependents": "No",
"tenure": 12,
"PhoneService": "Yes",
"MultipleLines": "No",
"InternetService": "Fiber optic",
"OnlineSecurity": "No",
"OnlineBackup": "Yes",
"DeviceProtection": "No",
"TechSupport": "No",
"StreamingTV": "Yes",
"StreamingMovies": "Yes",
"Contract": "Month-to-month",
"PaperlessBilling": "Yes",
"PaymentMethod": "Electronic check",
"MonthlyCharges": 90.5,
"TotalCharges": 1086.0
}

prediction, probability = predict_churn(
sample_customer
)

print("Prediction:", prediction)
print(
"Probability:",
round(probability * 100, 2),
"%"
)
