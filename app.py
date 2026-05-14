import streamlit as st

st.title("My First Streamlit App")

st.write("Hello Vikas 👋")
st.write("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}!")

age = st.number_input("Enter your age", min_value=1, max_value=100)

if age:
    st.write(f"Your age is {age}")

button = st.button("Click Me")

if button:
    st.balloons()
    st.write("Button clicked!")