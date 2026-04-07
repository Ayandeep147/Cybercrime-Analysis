import streamlit as st
from src.data_loader import load_data
from src.analysis_page import show_analysis_page
from src.ml_page import show_ml_page
from src.utils import get_district_table
from src.about import show_about_page
import base64
import os
import streamlit as st

def set_bg():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(BASE_DIR, "assets", "bg.png")

    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="A Hybrid Machine Learning Framework for Geospatial Cyber Crime Prediction and Demographic Pattern Analysis", layout="wide")

# ---------------- Session State for Navigation ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- Home Page ----------------
def show_home_page():
    st.components.v1.html(
        """
        <div style="text-align:center; padding: 40px 0; color: white;">
            <h1>A Hybrid Machine Learning Framework for Geospatial Cyber Crime Prediction and Demographic Pattern Analysis</h1>
            <h2 style="font-size:18px;">33rd West Bengal State Science & Technology Congress, 2025–26</h2>

            <hr style="width:60%; margin:auto;">

            <h3 style="margin-top:30px;">Author</h3>
            <p><b>Dr. Anupam Mukherjee</b></p>
            <p>Department of Computer Science & Engineering</p>
            <p>Siliguri Institute of Technology</p>

            <hr style="width:40%; margin:auto;">

            <h3 style="margin-top:30px;">Co-Authors</h3>
            <p>
                Ayandeep Roy &nbsp; | &nbsp; 
                Suryashis Banerjee &nbsp; | &nbsp; 
                Arnav Biswas &nbsp; | &nbsp; 
                Rimi Dutta
            </p>
            <p>Department of Computer Science & Engineering</p>
            <p>Siliguri Institute of Technology</p>

            <br>
        </div>
        """,
        height=600
    )

# ---------------- Sidebar ----------------
st.sidebar.title("Navigation")

if st.sidebar.button("Home", use_container_width=True):
    st.session_state.page = "Home"

if st.sidebar.button("Data Analysis", use_container_width=True):
    st.session_state.page = "Data Analysis"

if st.sidebar.button("Machine Learning", use_container_width=True):
    st.session_state.page = "Machine Learning"

if st.sidebar.button("About", use_container_width=True):
    st.session_state.page = "About"

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader("Upload Cleaned Dataset (CSV / Excel)", type=["csv", "xlsx"])

# ---------------- Page Routing ----------------
if st.session_state.page == "Home":
    show_home_page()
else:
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        # st.info("Please upload your cleaned dataset.")
        # st.stop()
    else:
        df = load_data("data_cleaing_and_analysis\data_files\Crimes_Cleaned.csv")

    # df = load_data(uploaded_file)
    district_table_df = get_district_table()

    if st.session_state.page == "Data Analysis":
        show_analysis_page(df, district_table_df)
    elif st.session_state.page == "Machine Learning":
        show_ml_page(df)
    elif st.session_state.page == "About":
        show_about_page()