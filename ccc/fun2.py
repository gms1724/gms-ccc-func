import streamlit as st

class button:
    def __init__(self, button_name):
        if st.button(f"button number is {button_name}"):
            st.toast(button_name*button_name)
for i in range(12):
    button(i)  