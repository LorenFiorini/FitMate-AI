
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def basic_information():
    basic_info = st.columns(2)
    basic_info[0].text_input('Full Name')
    basic_info[1].date_input('Date of birth')
    return basic_info


def fit_mate():
    st.set_page_config(
        page_title="FitMate AI",
        page_icon="💪",
        initial_sidebar_state="collapsed"
    )
    st.write("# Welcome to FitMate AI! 👋")
    st.write("##### FitMate AI can provide you a personalized workout programe and nutritional advice based on your need.")
    st.write("#### Basic Information")
    basic_info = basic_information()
    inputs = [""] * 4
    inputs[0] = st.text_input(
        label="Fitness goals",
        help="What do you want to achieve?"
    )
    st.radio('Pick one:', ['nose','ear'])


if __name__ == "__main__":
    fit_mate()


    # st.write("##### Are you wainting to lose some weight, put on some muscle or just start to move around a bit? Provide the following info:")
