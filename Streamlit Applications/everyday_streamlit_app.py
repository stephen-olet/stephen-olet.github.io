import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Everyday Python - Streamlit App")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "Quick Calculations", "Code Examples", "Visualizations", "About"]
)

# Home Page
if page == "Home":
    st.header("Welcome to the Everyday Python App!")
    st.write(
        """
        This app created and designed by Stephen Olet demonstrates the capabilities of Python and Streamlit through simple examples.
        Navigate using the sidebar to explore various features.
        """
    )
    st.image(
        "https://www.python.org/static/community_logos/python-logo.png", 
        width=300, 
        caption="Powered by Python & Streamlit"
    )

# Quick Calculations Page
elif page == "Quick Calculations":
    st.header("Quick Calculations")
    
    st.subheader("Arithmetic Operations")
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    operation = st.selectbox(
        "Choose an operation:",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    result = None
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

    if st.button("Calculate"):
        st.write(f"The result of {operation.lower()} is: **{result}**")

# Code Examples Page
elif page == "Code Examples":
    st.header("Code Examples")
    
    st.subheader("Example: Fibonacci Sequence")
    st.write("This function generates the first N numbers in the Fibonacci sequence.")

    code = '''
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
    '''
    st.code(code, language="python")

    n = st.slider("Generate Fibonacci sequence up to N:", min_value=5, max_value=20, value=10)
    if st.button("Generate Fibonacci Sequence"):
        def fibonacci(n):
            sequence = [0, 1]
            for i in range(2, n):
                sequence.append(sequence[i-1] + sequence[i-2])
            return sequence
        
        st.write(f"Fibonacci sequence up to {n}:")
        st.write(fibonacci(n))

# Visualizations Page
elif page == "Visualizations":
    st.header("Visualizations")
    st.subheader("Random Data Plot")

    chart_type = st.selectbox(
        "Select a chart type:",
        ["Line Chart", "Bar Chart", "Area Chart"]
    )

    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A", "B", "C"]
    )

    if chart_type == "Line Chart":
        st.line_chart(data)
    elif chart_type == "Bar Chart":
        st.bar_chart(data)
    elif chart_type == "Area Chart":
        st.area_chart(data)

# About Page
elif page == "About":
    st.header("About This App")
    st.write(
        """
        This app demonstrates Python functionalities and Streamlit's interactive components.
        It's inspired by the Everyday Python app and designed for learning and practice.
        """
    )
    st.info("Developed by [Stephen Olet].")
