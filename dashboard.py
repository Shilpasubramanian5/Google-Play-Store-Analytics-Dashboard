import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(
    page_title="Google Play Store Dashboard",
    layout="wide"
)

st.title("Google Play Store Dashboard")

ist_now = datetime.now(ZoneInfo("Asia/Kolkata"))
current_hour = ist_now.hour

def show_html(filename, height=500):

    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    components.html(
        html,
        height=height,
        scrolling=True
    )

col1, col2 = st.columns(2)

with col1:

    if 15 <= current_hour < 17:

        st.subheader("Analysis 1")

        show_html(
            "analysis1.html",
            height=700
        )

with col2:

    if 18 <= current_hour < 20:

        st.subheader("Analysis 2")

        show_html(
            "analysis2.html"
        )

with col1:

    if 13 <= current_hour < 14:

        st.subheader("Analysis 3")

        show_html(
            "analysis3.html",
            height=650
        )

with col2:

    if 18 <= current_hour < 21:

        st.subheader("Analysis 4")

        show_html(
            "analysis4.html"
        )

with col1:

    if 17 <= current_hour < 19:

        st.subheader("Analysis 5")

        show_html(
            "analysis5.html"
        )

with col2:

    if 16 <= current_hour < 18:

        st.subheader("Analysis 6")

        show_html(
            "analysis6.html"
        )