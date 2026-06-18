import streamlit as st
from src.predict import predict_churn

# 1. Define a clean, adaptable warning box component
def custom_warning(emoji, text):
    st.markdown(
        f"""
        <div style="
            background-color: rgba(255, 193, 7, 0.12); 
            border-left: 5px solid #ffc107; 
            padding: 14px 18px; 
            border-radius: 6px; 
            margin-bottom: 15px;
            font-size: 1rem;
        ">
            <span style="margin-right: 8px;">{emoji}</span>
            <span style="color: var(--text-color); font-weight: 500;">{text}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Simple page setup
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Simple title and description
st.title("📊 Customer Churn Prediction System")
st.markdown("**Predict whether a customer is likely to churn using Machine Learning**")
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("📝 Customer Information")
st.sidebar.markdown("Enter customer details and click Predict")
st.sidebar.markdown("---")

# Group inputs by category
st.sidebar.subheader("👤 Personal Details")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])

st.sidebar.subheader("📱 Services")
phone_service = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

st.sidebar.subheader("🔒 Internet Add-ons")
online_security = st.sidebar.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.sidebar.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.sidebar.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

st.sidebar.subheader("💳 Contract & Billing")
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])
payment = st.sidebar.selectbox("Payment Method", 
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

st.sidebar.subheader("💰 Financial Information")
tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly = st.sidebar.number_input("Monthly Charges (₹)", min_value=0.0, value=70.0)
total = st.sidebar.number_input("Total Charges (₹)", min_value=0.0, value=1000.0)
st.sidebar.markdown("---")

# Predict button
if st.sidebar.button("🚀 Predict Churn", use_container_width=True):
    
    # Create customer dictionary
    customer = {
        "gender": gender,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    # Get prediction
    prediction, probability = predict_churn(customer)
    probability *= 100

    # Display results
    
    st.subheader("📊 Prediction Results")
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tenure", f"{tenure} months")
    col2.metric("Monthly Charges", f"₹{monthly:.2f}")
    col3.metric("Total Charges", f"₹{total:.2f}")
    col4.metric("Contract", contract)

    st.markdown("---")
    
    # Main prediction metrics
    col1, col2 = st.columns(2)
    col1.metric("Churn Probability", f"{probability:.2f}%")
    col2.metric("Prediction", prediction)

    # Risk indicator
    st.markdown("---")
    if probability >= 70:
        st.error(f"🔴 HIGH CHURN RISK - {probability:.2f}%")
    elif probability >= 40:
        custom_warning("🟡", f"MEDIUM CHURN RISK - {probability:.2f}%")
    else:
        st.success(f"🟢 LOW CHURN RISK - {probability:.2f}%")

    # Progress bar
    st.progress(int(probability) / 100)
    st.info(f"The model estimates a {probability:.2f}% probability that this customer will churn.")

    # Customer Summary
    st.markdown("---")
    st.subheader("👥 Customer Summary")
    
    with st.expander("View Details"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Gender:** {gender}")
            st.write(f"**Senior Citizen:** {senior}")
            st.write(f"**Partner:** {partner}")
            st.write(f"**Dependents:** {dependents}")
            st.write(f"**Tenure:** {tenure} months")
        with col2:
            st.write(f"**Internet Service:** {internet_service}")
            st.write(f"**Contract:** {contract}")
            st.write(f"**Monthly Charges:** ₹{monthly:.2f}")
            st.write(f"**Total Charges:** ₹{total:.2f}")
            st.write(f"**Payment Method:** {payment}")

    # Recommendations
    st.markdown("---")
    st.subheader("💡 Recommendations")

    if probability >= 70:
        st.error("🔴 HIGH PRIORITY - Take Immediate Action")
        st.markdown("""
        - Offer retention discounts immediately
        - Assign a dedicated customer support executive
        - Promote yearly or two-year contracts
        - Contact customer proactively
        - Offer exclusive perks or loyalty rewards
        """)

    elif probability >= 40:
        custom_warning("🟡", "MEDIUM PRIORITY - Implement Preventive Measures")
        st.markdown("""
        - Offer promotional discounts
        - Encourage additional services
        - Monitor customer engagement closely
        - Recommend long-term plans
        - Improve service quality
        """)

    else:
        st.success("🟢 LOW PRIORITY - Maintain Current Satisfaction")
        st.markdown("""
        - Continue regular engagement
        - Offer loyalty rewards
        - Recommend complementary services
        - Maintain high service quality
        - Gather feedback regularly
        """)

    # Risk Factors
    st.markdown("---")
    st.subheader("⚠️ Risk Factors")

    if probability >= 40:
        risk_factors = []

        if contract == "Month-to-month":
            risk_factors.append("Month-to-month contract (easy to leave)")

        if internet_service == "Fiber optic":
            risk_factors.append("Fiber optic service (higher churn rate)")

        if payment == "Electronic check":
            risk_factors.append("Electronic check payment method")

        if tenure < 12:
            risk_factors.append(f"Low tenure ({tenure} months)")

        if monthly > 80:
            risk_factors.append(f"High monthly charges (₹{monthly:.2f})")

        if risk_factors:
            for i, factor in enumerate(risk_factors, 1):
                custom_warning("⚠️", f"{factor}")
        else:
            st.success("No major risk factors identified")
    else:
        st.success("No major churn risk factors identified")

    # Model Info
    st.markdown("---")
    st.subheader("ℹ️ About the Model")
    
    with st.expander("View Model Details"):
        col1, col2 = st.columns(2)
        col1.metric("Algorithm", "Logistic Regression")
        col1.metric("Accuracy", "80.70%")
        col2.metric("Cross Validation", "80.44%")
        col2.metric("Threshold", "0.55")
        
        st.info("**Dataset:** Telco Customer Churn Dataset (7,043 customers)")

    # Download Report
    st.markdown("---")
    st.subheader("📄 Download Report")
    
    report = f"""
CUSTOMER CHURN PREDICTION REPORT
{'='*50}

PREDICTION RESULTS
Prediction: {prediction}
Probability: {probability:.2f}%
Risk Level: {'HIGH' if probability >= 70 else 'MEDIUM' if probability >= 40 else 'LOW'}

CUSTOMER DETAILS
Gender: {gender}
Senior Citizen: {senior}
Partner: {partner}
Dependents: {dependents}
Contract: {contract}
Internet Service: {internet_service}
Tenure: {tenure} months
Monthly Charges: ₹{monthly:.2f}
Total Charges: ₹{total:.2f}
Payment Method: {payment}

{'='*50}
Generated by Customer Churn Prediction System
Developed by Meet Modi
"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="churn_prediction_report.txt",
        use_container_width=True
    )

    # Footer
    st.markdown("---")
    st.caption("Developed by Meet Modi | Customer Churn Prediction ")

else:
    
    st.info("""
    ### 👋 Welcome!
    
    **Steps to use:**
    1. Fill in customer details in the sidebar
    2. Click **🚀 Predict Churn**
    3. View results and recommendations
    4. Download the report
    
    **What you'll get:**
    - 📊 Churn probability prediction
    - 💡 Actionable recommendations
    - ⚠️ Risk factors analysis
    - 📄 Downloadable report
    """)