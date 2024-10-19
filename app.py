import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create input fields for the two numbers
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)

# Create a dropdown for selecting the operation
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    
    st.write("Result:", result)
