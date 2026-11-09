import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Assistant",layout="wide")

diabet_model = pickle.load(open(r"C:/Users/Hp/Desktop/ML and DL/Diabet_SVC.pkl","rb"))
insurance_model = pickle.load(open(r"C:/Users/Hp/Desktop/ML and DL/Medical_Insurance.pkl","rb"))

with st.sidebar :

    selected = option_menu("Health Care System",["Diabet System ","Insurance_Cost"],icons=["lungs","cash"],default_index=0)



if selected == "Diabet System ":

    st.title("Diabetes Prediction Diagnose System ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        preg = st.slider("Pregnancies", 0, 20, 0)
        Glucose = st.number_input("Glucose level", min_value=0.0)
        Age = st.number_input("Age", min_value=1)

    with col2:
        Blood = st.slider("Blood Pressure level", 0, 400, 120)
        Insulin = st.number_input("Insulin level", min_value=0.0)
        thick = st.number_input("Thickness level", min_value=0.0)

    with col3:
        BMI = st.slider("BMI", 0.0, 100.0, 24.0)
        DiabetPedigreefunction = st.number_input(
            "Diabetes Pedigree Function Value",
            min_value=0.0
        )

    if st.button("Diabet test result"):

        user_input = [
            preg,
            Glucose,
            Blood,
            thick,
            Insulin,
            BMI,
            DiabetPedigreefunction,
            Age
        ]

        diab_pred = diabet_model.predict([user_input])

        if diab_pred[0] == 1:
            st.success("The person is diabetic")
        else:
            st.success("The person is non-diabetic")

if selected == "Insurance_Cost" :
    st.title("Insurance Cost Prediction System")

    age = st.text_input("Enter the age")
    sex = st.text_input("Enter the gender")
    sex = sex.lower().strip()
    if sex == "male" :
        sex_number = 1
    else :
        sex_number = 0
    smoker = st.text_input("Are you smoking ? yes/no")
    smoker = smoker.lower().strip()
    if smoker == "yes" :
        smoker_number = 1
    else :
        smoker_number = 0
    bmi = st.text_input("Enter BMI")
    children = st.text_input("Number of children")
    region = st.text_input("The region you live rightnow southeast/northeast/southwest/northwest")
    if region == "southeast":
        region_number = 0
    elif region == "northeast":
        region_number = 1
    elif region == "southwest":
        region_number = 2
    elif region == "northwest":
        region_number = 3
    charges = ''
    if st.button("Charge test result") :
        user_input = [age,sex_number,bmi,children,smoker_number,region_number]
        user_input = [float(x) for x in user_input]

        st.success(f"The predicted charge value = {insurance_model.predict([user_input])}")

    

            





    


