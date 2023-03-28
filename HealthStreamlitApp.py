import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import pickle
import os
import sklearn
from sklearn.feature_selection import SelectFromModel



st.set_page_config(layout='wide', page_title='CKD App')



st.title('Chronic Kidney Disease Prediction')

#adds image
image = Image.open('./image/fnalkidney-comp_1087848275.png')
st.image(image, caption='Kidney')



st.write('''Chronic kidney disease (CKD) is when the kidneys are damaged and cannot correctly filter waste and excess fluids from the blood.
About 37 million people in the United States have Chronic Kidney Disease (CKD). Early detection and diagnosis of CKD are essential to
preventing its progression to kidney failure. Machine learning models can assist in predicting CKD. This project is the user interface for
a previous project of mine that uses National Center for Health Statistics (NCHS) data. Variables such as age, gender, medical history, and laboratory
test results will be used. By identifying patterns in the data, models can predict a patient's risk of developing CKD, allowing for early intervention and management.''')


#load model
model = pickle.load(open('model.pkl', 'rb'))

# Define options for selectboxes



hypertension_options = ["Yes", "No"]
hypertension_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), hypertension_options))

diabetes_options = ["Yes", "No"]
diabetes_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), diabetes_options))

stroke_options = ["Yes", "No"]
stroke_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), stroke_options))

cvd_options = ["Yes", "No"]
cvd_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), cvd_options))

chf_options = ["Yes", "No"]
chf_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), chf_options))

anemia_options = ["Yes", "No"]
anemia_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), anemia_options))

fam_hypertension_options = ["Yes", "No"]
fam_hypertension_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_hypertension_options))

fam_diabetes_options = ["Yes", "No"]
fam_diabetes_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_diabetes_options))

fam_cvd_options = ["Yes", "No"]
fam_cvd_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_cvd_options))

st.subheader('Demographics')


st.subheader('Healthcare')

Hypertension = st.selectbox('Do you have hypertension?', hypertension_options)
Diabetes = st.selectbox('Do you have diabetes?', diabetes_options)
Stroke = st.selectbox('Have you had a stroke before?', stroke_options)
CVD = st.selectbox('Do you have a history of cardiovascular disease?', cvd_options)
CHF = st.selectbox('Do you have a history of congestive heart failure?', chf_options)
Anemia = st.selectbox('Do you have a history of anemia?', anemia_options)

st.subheader('Family History')
Fam_Hypertension = st.selectbox('Do you have a family history of Hypertension?', fam_hypertension_options)
Fam_Diabetes = st.selectbox('Do you have a family history of Diabetes?', fam_diabetes_options)
Fam_CVD = st.selectbox('Do you have a family history of cardiovascular disease?', fam_cvd_options)


# define diagnosis variable and set it to a default value
diagnosis = "Unknown"

# Create button to run model
if st.button("CKD Risk Result"):
    input_data = [
age_float,
gender_float,
racegrp_float,
education_float,
marital_status_float,
income_float,
caresource_float,
health_insurance_float,
weight_float,
height_float,
sbp_float,
dbp_float,
hdl_float,
ldl_float,
total_cholesterol_float,
dyslipidemia_float,
pvd_float,
activity_float,
poor_vision_float,
smoker_float,
hypertension_float,
diabetes_float,
stroke_float,
cvd_float,
chf_float,
anemia_float,
fam_hypertension_float,
fam_diabetes_float,
fam_cvd_float]
    prediction = model.predict(input_data)

    # set the diagnosis based on the prediction result
    if prediction == 1:
        diagnosis = "CKD"
    else:
        diagnosis = "No CKD"

    st.write("The predicted kidney disease status is", diagnosis)


#create sidebar
st.sidebar.title("About CKD App")


with st.sidebar:
    st.write("""
            Please see your doctor for an accurate risk prediction. This tool is for learning purposes.

            Please note that this tool is a work in progress. Contact me [here](mailto:ahobby@healthdatasciencenewsletter) or consider checking out [GitHub](https://github.com/AndreaHobby/CKD-Prediction/blob/main/Predicting%20Chronic%20Kidney%20Disease.ipynb) repository with any suggestions or questions.
        """)
