import streamlit as st

def show():
    st.markdown(
        """
        <div class="card">
          <p class="kpi">📞 Kontak</p>

          <div class="card-content">
            📧 Email: 
            <a href="mailto:alzahrareyhan@gmail.com">
              alzahrareyhan@gmail.com
            </a><br>
            💼 LinkedIn: 
            <a href="https://www.linkedin.com/in/reyhan-nandita-al-zahra-64a82a278/" target="_blank">
              Reyhan Nandita Al Zahra
            </a><br>
            💻 GitHub: 
            <a href="https://github.com/alzahrareyhan" target="_blank">
              alzahrareyhan
            </a>
          </div>

        </div>
        
        """,
        unsafe_allow_html=True,
    )
