pip install matplotlib
import streamlit as st
import pandas as pd

# Check for matplotlib availability
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    st.error("Matplotlib is not installed. Please install it using 'pip install matplotlib'.")
    st.stop()

# Load the dataset
uploaded_file = "https://github.com/vaidyamohit/Marketing-Dashboard/raw/main/Dataset%20Marketing.xlsx"
try:
    df = pd.read_excel(uploaded_file, engine="openpyxl")
except Exception as e:
    st.error("Failed to load the dataset. Please check the file path or internet connection.")
    st.stop()

# Set up Streamlit app
st.title("Marketing Dashboard")
st.sidebar.title("Navigation")

# Navigation options
options = ["Overview", "Data Summary", "Visualizations"]
choice = st.sidebar.selectbox("Choose an option", options)

if choice == "Overview":
    st.header("Overview of the Dataset")
    st.write("### First 5 rows of the dataset")
    st.dataframe(df.head())
    st.write("### Dataset Information")
    st.write(f"Shape of the dataset: {df.shape}")
    st.write("### Descriptive Statistics")
    st.write(df.describe())

elif choice == "Data Summary":
    st.header("Data Summary")
    st.write("### Column Names")
    st.write(df.columns.tolist())
    st.write("### Missing Values")
    st.write(df.isnull().sum())
    st.write("### Unique Values in Each Column")
    st.write({col: df[col].nunique() for col in df.columns})

elif choice == "Visualizations":
    st.header("Visualizations")
    
    st.write("### Column Selection")
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)
    
    chart_type = st.radio("Select Chart Type", ["Bar", "Line", "Scatter"])
    
    try:
        if chart_type == "Bar":
            fig, ax = plt.subplots()
            ax.bar(df[x_axis], df[y_axis])
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            st.pyplot(fig)
        
        elif chart_type == "Line":
            fig, ax = plt.subplots()
            ax.plot(df[x_axis], df[y_axis])
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            st.pyplot(fig)
        
        elif chart_type == "Scatter":
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis])
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error in visualization: {e}")
