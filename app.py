# app.py
import streamlit as st

# App title and credits
st.title("Simple Calculator")
st.write("Made by Shahzaib, assisted by Dr. Usman Nazir, inspired by Mr. Ahmad Liaqat.")

# Sidebar for operation selection
operation = st.sidebar.selectbox("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

# Input fields for numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of division is: {result}")
        else:
            st.error("Error: Cannot divide by zero.")

# Additional info in the sidebar
st.sidebar.write("Use this simple calculator for basic operations. Enjoy calculating!")
