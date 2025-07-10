import streamlit as st 
from utils import load_model
from pathlib import Path

st.set_page_config("Mental Health Predictor",layout="wide")

st.title("Mental Heath Predictor App")

st.markdown("""Welcome to the **Mental Health Predictor App ** dashboard.  
Use the sidebar to explore the following:
- 📊 **EDA Dashboard**: Insights into the dataset and Exploratory Data Analysis
- 🧠 **Treatment Predictor**: MCQ-style quiz to predict if you may need mental health treatment
""")

model_path = Path("/Users/nilaysingh/Desktop/Mental-Health-Predictor-App/models/Mental_Health_Prediction_model.cbm")
model = load_model(model_path)

st.markdown("""---  
Made with ❤️ using Streamlit | [GitHub](https://github.com/yourusername/mental_health_app)
""")


