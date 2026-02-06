import streamlit as st
import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "dataset" / "TelcoCustomerChurn.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

df = load_data()
FEATURES = [
 'gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines',
 'InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
 'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod',
 'MonthlyCharges','TotalCharges'
]

def show():
    st.markdown(
        """
        <div class="card">
          <p class="kpi">📚 Tentang Project</p>
          <p class="muted", style="text-align: justify;">
          Project ini merupakan aplikasi prediksi Customer Churn menggunakan dataset Telco Customer Churn. Model dikembangkan untuk mengidentifikasi pelanggan yang berpotensi berhenti berlangganan berdasarkan data layanan, kontrak, dan pola pembayaran pelanggan. Dalam pengembangan model, dilakukan penyeimbangan data menggunakan SMOTE (Synthetic Minority Over-sampling Technique) untuk mengatasi ketidakseimbangan kelas. Selanjutnya, proses prediksi menggunakan algoritma XGBoost karena memiliki performa tinggi pada data tabular. Aplikasi ini menampilkan hasil prediksi churn beserta probabilitas risiko churn berdasarkan data input pengguna.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
          <b>Tujuan:</b> Memprediksi pelanggan yang berpotensi churn.<br>
          <b>Artifacts:</b> model (.pkl), encoders.pkl, scalers.pkl.<br>
          <b>Alur:</b> input → encoding → scaling → prediction.<br><br>

          <b>Dataset:</b> 
          <a href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn" target="_blank">
            Telco Customer Churn Dataset
          </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("## 📊 Dataset Visualization")

    # ================= KPI OVERVIEW =================
    st.markdown("### Dataset Overview")

    k1, k2, k3 = st.columns(3)

    k1.metric("Jumlah Data", df.shape[0])
    k2.metric("Jumlah Kolom", df.shape[1])
    k3.metric("Jumlah Pelanggan Churn", df[df["Churn"] == "Yes"].shape[0])


    # ================= ROW 1 =================
    col1, col2, col3 = st.columns(3)

    # ----- Churn Distribution -----
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        fig = px.pie(df, names="Churn", title="Distribusi Customer Churn")
        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Contract vs Churn -----
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        contract = pd.crosstab(df["Contract"], df["Churn"]).reset_index()
        fig = px.bar(
            contract,
            x="Contract",
            y=["Yes", "No"],
            title="Contract Type vs Churn",
            barmode="group"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Payment Method vs Churn -----
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        payment = pd.crosstab(df["PaymentMethod"], df["Churn"]).reset_index()
        fig = px.bar(
            payment,
            x="PaymentMethod",
            y=["Yes", "No"],
            title="Payment Method vs Churn",
            barmode="group"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ================= ROW 2 =================
    col4, col5, col6 = st.columns(3)

    # ----- Tenure Distribution -----
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        fig = px.histogram(
            df,
            x="tenure",
            color="Churn",
            title="Distribusi Tenure"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Monthly Charges -----
    with col5:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        fig = px.box(
            df,
            x="Churn",
            y="MonthlyCharges",
            title="Monthly Charges vs Churn"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Total Charges -----
    with col6:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        fig = px.box(
            df,
            x="Churn",
            y="TotalCharges",
            title="Total Charges vs Churn"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ================= ROW 3 =================
    col7, col8, col9 = st.columns(3)

    # ----- Internet Service -----
    with col7:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        internet = pd.crosstab(df["InternetService"], df["Churn"]).reset_index()
        fig = px.bar(
            internet,
            x="InternetService",
            y=["Yes", "No"],
            title="Internet Service vs Churn",
            barmode="group"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Streaming TV -----
    with col8:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        streaming = pd.crosstab(df["StreamingTV"], df["Churn"]).reset_index()
        fig = px.bar(
            streaming,
            x="StreamingTV",
            y=["Yes", "No"],
            title="Streaming TV vs Churn",
            barmode="group"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)


    # ----- Tech Support -----
    with col9:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        support = pd.crosstab(df["TechSupport"], df["Churn"]).reset_index()
        fig = px.bar(
            support,
            x="TechSupport",
            y=["Yes", "No"],
            title="Tech Support vs Churn",
            barmode="group"
        )

        st.plotly_chart(fig, width="stretch")

        st.markdown("</div>", unsafe_allow_html=True)
