import streamlit as st
from utils import load_assets, predict_churn

model, encoders, scalers = load_assets()

def show():

    # ===== HEADER =====
    st.markdown("""
    <div class="card">
        <div class="title">🔮 Customer Churn Prediction</div>
        <div class="subtitle">Isi data customer untuk memprediksi potensi churn</div>
    </div>
    """, unsafe_allow_html=True)

    # ===== FORM =====
    with st.form("churn_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            gender = st.selectbox("Gender", ["Female","Male"])
            SeniorCitizen = st.selectbox("SeniorCitizen",[0,1])
            Partner = st.selectbox("Partner",["Yes","No"])
            Dependents = st.selectbox("Dependents",["Yes","No"])
            tenure = st.slider("Tenure",0,72,5)

        with col2:
            PhoneService = st.selectbox("PhoneService",["Yes","No"])
            MultipleLines = st.selectbox("MultipleLines",["No","Yes","No phone service"])
            InternetService = st.selectbox("InternetService",["DSL","Fiber optic","No"])
            OnlineSecurity = st.selectbox("OnlineSecurity",["No","Yes","No internet service"])
            OnlineBackup = st.selectbox("OnlineBackup",["No","Yes","No internet service"])

        with col3:
            DeviceProtection = st.selectbox("DeviceProtection",["No","Yes","No internet service"])
            TechSupport = st.selectbox("TechSupport",["No","Yes","No internet service"])
            StreamingTV = st.selectbox("StreamingTV",["No","Yes","No internet service"])
            StreamingMovies = st.selectbox("StreamingMovies",["No","Yes","No internet service"])
            Contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])

        PaperlessBilling = st.selectbox("PaperlessBilling",["Yes","No"])
        PaymentMethod = st.selectbox(
            "PaymentMethod",
            ["Electronic check","Mailed check","Bank transfer","Credit card"]
        )

        MonthlyCharges = st.number_input("MonthlyCharges",0.0,1000.0,70.0)
        TotalCharges = st.number_input("TotalCharges",0.0,10000.0,200.0)

        submit = st.form_submit_button("Predict")
        

    # ===== RESULT =====
    if submit:

        input_data = {
            'gender': gender,
            'SeniorCitizen': SeniorCitizen,
            'Partner': Partner,
            'Dependents': Dependents,
            'tenure': tenure,
            'PhoneService': PhoneService,
            'MultipleLines': MultipleLines,
            'InternetService': InternetService,
            'OnlineSecurity': OnlineSecurity,
            'OnlineBackup': OnlineBackup,
            'DeviceProtection': DeviceProtection,
            'TechSupport': TechSupport,
            'StreamingTV': StreamingTV,
            'StreamingMovies': StreamingMovies,
            'Contract': Contract,
            'PaperlessBilling': PaperlessBilling,
            'PaymentMethod': PaymentMethod,
            'MonthlyCharges': MonthlyCharges,
            'TotalCharges': TotalCharges
        }

        pred, proba = predict_churn(model, encoders, scalers, input_data)

        
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        left, right = st.columns([1,2], gap="large")

        # ===== STATUS CARD =====
        with left:

            st.markdown("##### Prediction Status")

            if pred == 1:
                st.markdown("""
                <div class='badge-danger'>
                    ⚠ Berpotensi Churn
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown("""
                <div class='badge-success'>
                    ✔ Customer Loyal
                </div>
                """, unsafe_allow_html=True)

        # ===== PROBABILITY CARD =====
        with right:

            st.markdown("##### Probability Churn")

            st.progress(float(proba))

            st.markdown(
                f"<h1 style='margin-top:10px'>{proba*100:.2f}%</h1>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        with st.expander("Detail Input"):
            st.json(input_data)
