import streamlit as st

# Supports MD
st.write("## This is a H2 Title")
st.write("Hello World")

x = st.text_input("Favorite Movie?")
st.write(f"Your Favorite Movie is: {x}")

# Creating Button
is_clicked=st.button("CLick Me")