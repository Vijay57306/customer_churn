import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #1f77b4;
}

.stButton>button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    font-size: 20px;
    border-radius: 12px;
    height: 3.2em;
    border: none;
}

.stButton>button:hover {
    background-color: #45a049;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(
    open(
        r"C:\Users\Vijay Kumar\Downloads\customer\churn_model.pkl",
        "rb"
    )
)

# =========================
# TITLE
# =========================

st.title("📊 Customer Churn Prediction System")

st.markdown("""
### Predict whether a customer will stay or churn using Machine Learning
""")

st.markdown("---")

# =========================
# INPUT SECTION
# =========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure Months",
        0, 100, 12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

with col2:

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.slider(
        "Monthly Charges",
        0.0, 10000.0, 500.0
    )

    total_charges = st.slider(
        "Total Charges",
        0.0, 100000.0, 5000.0
    )

# =========================
# PREDICTION BUTTON
# =========================

if st.button("🔍 Predict Churn"):

    # =========================
    # ENCODING
    # =========================

    gender = 1 if gender == "Male" else 0
    partner = 1 if partner == "Yes" else 0
    dependents = 1 if dependents == "Yes" else 0
    phone_service = 1 if phone_service == "Yes" else 0
    paperless_billing = 1 if paperless_billing == "Yes" else 0

    multiple_lines_map = {
        "No": 0,
        "Yes": 1,
        "No phone service": 2
    }

    internet_service_map = {
        "DSL": 0,
        "Fiber optic": 1,
        "No": 2
    }

    yes_no_map = {
        "No": 0,
        "Yes": 1,
        "No internet service": 2
    }

    contract_map = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }

    payment_method_map = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer (automatic)": 2,
        "Credit card (automatic)": 3
    }

    # =========================
    # CREATE DATAFRAME
    # =========================

    input_data = pd.DataFrame([[
        gender,
        senior_citizen,
        partner,
        dependents,
        tenure,
        phone_service,
        multiple_lines_map[multiple_lines],
        internet_service_map[internet_service],
        yes_no_map[online_security],
        yes_no_map[online_backup],
        yes_no_map[device_protection],
        yes_no_map[tech_support],
        yes_no_map[streaming_tv],
        yes_no_map[streaming_movies],
        contract_map[contract],
        paperless_billing,
        payment_method_map[payment_method],
        monthly_charges,
        total_charges
    ]], columns=[
        "Gender",
        "Senior Citizen",
        "Partner",
        "Dependents",
        "Tenure Months",
        "Phone Service",
        "Multiple Lines",
        "Internet Service",
        "Online Security",
        "Online Backup",
        "Device Protection",
        "Tech Support",
        "Streaming TV",
        "Streaming Movies",
        "Contract",
        "Paperless Billing",
        "Payment Method",
        "Monthly Charges",
        "Total Charges"
    ])

    # =========================
    # PREDICTION
    # =========================

    prediction = model.predict(input_data)

    # =========================
    # RESULT SECTION
    # =========================

    st.markdown("---")

    st.subheader("🎯 Prediction Result")

    if prediction[0] == 1:

        st.markdown("""
        <div style="
            background-color:#ffebee;
            padding:30px;
            border-radius:15px;
            text-align:center;
            border:2px solid red;
        ">
            <h1 style="color:red;">
                ⚠ Customer Will Churn
            </h1>

            <h3 style="color:#444;">
                High chance of leaving the company
            </h3>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
            background-color:#e8f5e9;
            padding:30px;
            border-radius:15px;
            text-align:center;
            border:2px solid green;
        ">
            <h1 style="color:green;">
                ✅ Customer Will Stay
            </h1>

            <h3 style="color:#444;">
                Customer is loyal to the company
            </h3>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # METRICS
    # =========================

    st.markdown("---")

    st.subheader("📌 Customer Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Tenure",
            f"{tenure} Months"
        )

    with c2:
        st.metric(
            "Monthly Charges",
            f"₹ {monthly_charges}"
        )

    with c3:
        st.metric(
            "Total Charges",
            f"₹ {total_charges}"
        )

    # =========================
    # VISUALIZATION
    # =========================

    st.markdown("---")

    st.subheader("📈 Customer Insights")

    chart_data = pd.DataFrame({
        "Features": [
            "Tenure",
            "Monthly Charges",
            "Total Charges"
        ],
        "Values": [
            tenure,
            monthly_charges,
            total_charges
        ]
    })

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        chart_data["Features"],
        chart_data["Values"]
    )

    ax.set_ylabel("Values")
    ax.set_title("Customer Overview")

    st.pyplot(fig)

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<center>
<h4>🚀 Built with Streamlit & Machine Learning</h4>
</center>
""", unsafe_allow_html=True)