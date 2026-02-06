import streamlit as st

def show():
    st.markdown(
        """
        <div class="card">
          <p class="kpi">👤 Tentang Saya</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 2], vertical_alignment="top")

    with col1:
        st.image("image/Reyhan.jpeg")

    with col2:
        st.markdown(
            """
            <div class="card">
             <p style="text-align: justify;">
             "Saya adalah lulusan Sarjana Teknik Informatika dari Universitas Negeri Semarang (2025) dengan minat pada Data Analyst, Data Science, AI Engineer, ML Engineer. Memiliki pengalaman dalam mengembangkan model prediktif, visualisasi data, serta solusi berbasis kecerdasan buatan dan aplikasi web, dengan kemampuan mengolah data terstruktur maupun tidak terstruktur serta merancang algoritma yang efisien untuk menyelesaikan permasalahan kompleks. Saya memiliki kemampuan analisis, pemecahan masalah, dan kerja tim yang baik serta berkomitmen untuk terus belajar dan berkontribusi dalam pengembangan solusi teknologi inovatif."
             </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card">
              <b>Nama:</b> Reyhan Nandita Al Zahra<br>
              <b>Role:</b> Data Science / Machine Learning<br>
              <b>Fokus:</b> Customer Analytics, Churn Prediction<br><br>
              Project ini dibuat untuk menampilkan pipeline prediksi churn end-to-end.
            </div>
            """,
            unsafe_allow_html=True,
        )

