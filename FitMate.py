
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def basic_information():
    st.subheader("Basic Information")
    basic_info = st.columns(
        spec=2,
        gap="medium"
    )
    basic_info[0].text_input(
        label="**Full Name**",
        placeholder="John, Smith",
        max_chars=100
    )
    basic_info[1].date_input(
        '**Date of birth**'
    )
    return basic_info

def health_status():
    st.subheader("Health Status")
    fit_lvl = st.selectbox(
        label= "**Fitness level**",
        options = [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )
    diet = st.text_input(
        label="**Dietary restrictions**",
        placeholder="None",
        max_chars=100

    )
    med_cond = st.text_area(
        label="**Medical condition**",
        max_chars=300
    )
    return [fit_lvl, diet, med_cond]

def fit_goals():
    st.subheader("Goals")
    fitness_goals = st.text_area(
        label="**Fitness goals**",
        max_chars=300
    )
    freq = st.slider(
        label='**Training Frequency**',
        min_value=0,
        max_value=7,
        step=1,
        format="%i days a week"
    )

def fit_mate():
    st.set_page_config(
        page_title="FitMate AI",
        page_icon="💪",
        initial_sidebar_state="collapsed"
    )
    st.title("Welcome to FitMate AI! 👋")
    st.write("##### _FitMate AI can provide you a personalized workout programe and nutritional advice based on your need._")
    basic_info = basic_information()
    health_stat = health_status()
    goals = fit_goals()


if __name__ == "__main__":
    fit_mate()


    # st.write("##### Are you wainting to lose some weight, put on some muscle or just start to move around a bit? Provide the following info:")

    # h_stat = st.columns([1, 2])
    # h_stat[0].selectbox(
    #     'Fitness level',
    #     [
    #         "Beginner",
    #         "Intermediate",
    #         "Advanced"
    #     ]
    # )
    # h_stat[0].text_area("")
    # h_stat[1].text_area('Medical condition')