import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

number = st.slider("Pick a number", 0, 100)
st.write(f"You selected: {number}")