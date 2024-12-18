# Save this as 'app.py' or run in Jupyter
import streamlit as st
from PIL import Image
import os


pages = {
    "Streamlit": [
    st.Page("pages/00_MY_PROFILE.py", title ="My Profile"),
    st.Page("pages/01_GRAND_CANYON_VISITOR_CENTER.py", title ="Project 01"),
    st.Page("pages/02_CONSTRUCTION_DRAWING.py", title ="Project 02"),
    st.Page("pages/03_STRUCTURAL_MODULE_WORKSHOP.py", title ="Project 03"),
    ],
    "Resources": [
    st.Page("pages/00_MY_PROFILE.py", title ="My Profile"),

    ]
}
pg = st.navigation(pages)
pg.run()

# Title and basic elements
st.title("ARCH 492 | Algorithmic Thinking in Design")
st.subheader('Session 2020 | Credit: 1.5 | Optional Sessional Course')
st.subheader('Department of Architectrue | BUET')

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid black; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)

st.title("1901027_Task 7_Streamlit")
st.subheader('[N.B. : This is an academic project. All the rights are reserved to the student & Course teachers.]')

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid black; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)

st.markdown('<p style="color:#81a2ca; font-size:25px;">❗ This is a cover page only. The main pages are into the subpage section with various formating scripts.</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#81a2ca; font-size:25px;">❗ Click on the upper left ">" to view sub sections!</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#81a2ca; font-size:25px;">❗ Use **light theme** and **wide mode** for best experience! </p>', unsafe_allow_html=True)

# Add a custom styled divider
st.markdown(
    """
    <hr style="border: 2px solid black; border-width: 2px; font-weight: bold;"/>
    """, 
    unsafe_allow_html=True
)








