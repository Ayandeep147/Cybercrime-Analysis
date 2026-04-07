import streamlit as st

def show_about_page():

    st.title("About the Team")
    st.markdown("---")

    # ---------------- AUTHOR & MENTOR ----------------
    st.title("Author & Mentor")

    # ---------- CONTENT ----------
    col1, col2, col3 = st.columns([1,0.2,2])

    with col1:
        st.image("assets\mentor.png", width=180)

    with col2:
        print("")

    with col3:
        st.title("Dr. Anupam Mukherjee")
        st.write("Department of Computer Science & Engineering")
        st.write("Siliguri Institute of Technology")
                 
        
    st.markdown("---")

    # ---------------- CO-AUTHORS ----------------
    st.markdown("<h1 style='text-align: center;'>Co-Authors</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1])

    with col1:
        st.image("assets\\arnav.png", width=150)
        st.markdown("**Arnav Biswas**  \nCSE Student")

    with col2:
        st.image("assets\\ayan.jpeg", width=100)
        st.markdown("**Ayandeep Roy**  \nCSE Student")
    
    col3, col4 = st.columns([1,1])

    with col3:
        st.image("assets\\rimi.png", width=120)
        st.markdown("**Rimi Dutta**  \nCSE Student")

    with col4:
        st.image("assets\surya.png", width=120)
        st.markdown("**Suryashis Banerjee**  \nCSE Student")

    st.markdown("---")

    # ---------------- AWARDS ----------------
    st.markdown("<h2 style='text-align: center;'>Awards & Accomplishments</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("assets\\award.png", caption="State Science Congress", use_container_width=True)

    with col2:
        st.image("assets\certificate.png", caption="Project Recognition", use_container_width=True)
