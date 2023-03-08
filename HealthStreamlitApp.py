import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
import numpy as np
import pickle
import os 

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


#load data
#loaded_model = pickle.load(open('Trained_DT_model.sav', 'rb'))
 
# Define options for selectboxes
def main():
 st.text('Demographics')   
 age_options = ["<40", "40-49", "50-59", "60-69", "70+"]
 gender_options = ["Male", "Female"]
 racegrp_options = ["White", "Black", "Hispanic", "Asian", "Other"]
 education_options = ["<High School", "High School/GED", "Some College", "College Graduate"]
 marital_status_options = ["Married", "Widowed", "Divorced", "Separated", "Never Married"]
 income_options = ["<20k", "20-34k", "35-49k", "50-74k", "75-99k", "100k+"]
 caresource_options = ["Doctor's Office/Clinic", "Hospital Inpatient", "Emergency Room"]
 health_insurance_options = ["Yes", "No"]
 weight_options = ["Underweight", "Normal", "Overweight", "Obese"]
 height_options = ["<5ft", "5ft-5ft5in", "5ft5in-6ft", ">6ft"]
 sbp_options = ["<120", "120-129", "130-139", "140-149", "150+"]
 dbp_options = ["<80", "80-84", "85-89", "90-99", "100+"]
 hdl_options = ["<40", "40-49", "50-59", "60+"]
 ldl_options = ["<100", "100-129", "130-159", "160-189", "190+"]
 total_chol_options = ["<200", "200-239", "240-279", "280+"]
 dyslipidemia_options = ["Yes", "No"]
 pvd_options = ["Yes", "No"]
 activity_options = ["Inactive", "Moderately Active", "Active"]
 poor_vision_options = ["Yes", "No"]
 smoker_options = ["Current Smoker", "Former Smoker", "Never Smoked"]
 hypertension_options = ["Yes", "No"]
 fam_hypertension_options = ["Yes", "No"]
 diabetes_options = ["Yes", "No"]
 fam_diabetes_options = ["Yes", "No"]
 stroke_options = ["Yes", "No"]
 cvd_options = ["Yes", "No"]
 fam_cvd_options = ["Yes", "No"]
 chf_options = ["Yes", "No"]
 anemia_options = ["Yes", "No"]
 age = st.selectbox("Age", age_options)
 gender = st.selectbox("Gender", gender_options)
 racegrp = st.selectbox("Racegrp", racegrp_options)
 education = st.selectbox("Education", education_options)
 marital_status = st.selectbox("Marital Status", marital_status_options)
 income = st.selectbox("Income", income_options)
 caresource = st.selectbox("CareSource", caresource_options)
 health_insurance = st.selectbox('Health Insurance', health_insurance_options)
 weight = st.selectbox('Weight', weight_options)
 height = st.selectbox('Height', height_options)
 sbp = st.selectbox('SBP', (0, 20, 40, 60, 80, 100))
 dbp = st.selectbox('DBP', (0, 20, 40, 60, 80, 100))
 HDL = st.selectbox('HDL', [0, 1, 2, 3])
 LDL = st.selectbox('LDL', [0, 1, 2, 3])
 Total_Cholesterol = st.selectbox('Total Cholesterol', [0, 1, 2, 3])
 Dyslipidemia = st.selectbox('Dyslipidemia', [0, 1])
 PVD = st.selectbox('PVD', [0, 1])
 Activity = st.selectbox('Activity', [0, 1, 2])
 Poor_Vision = st.selectbox('Poor Vision', [0, 1])
 Smoker = st.selectbox('Smoker', [0, 1])
 Hypertension = st.selectbox('Hypertension', [0, 1])
 Fam_Hypertension = st.selectbox('Fam Hypertension', [0, 1])
 Diabetes = st.selectbox('Diabetes', [0, 1])
 Fam_Diabetes = st.selectbox('Fam Diabetes', [0, 1])
 Stroke = st.selectbox('Stroke', [0, 1])
 CVD = st.selectbox('CVD', [0, 1])
 Fam_CVD = st.selectbox('Fam CVD', [0, 1])
 CHF = st.selectbox('CHF', [0, 1])
 Anemia = st.selectbox('Anemia', [0, 1])


diagnosis=''

st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    
   # Create button to run model
if st.button("CKD Risk Result"):
    #input_data = [[Age, Gender, Racegrp, Education, Marital status, Income, CareSource, health Insure, weight, Height, SBP,  DBP, HDL, LDL, Total Chol, Dyslipidemia, PVD , Activity, PoorVision, Smoker, Hypertension, Fam Hypertension, Diabetes, Fam Diabetes, Stroke, CVD, Fam CVD, CHF, Anemia]]  # Add more demographic variables...
    #input_data_scaled = scaler.transform(input_data)
    #prediction = model.predict(input_data_scaled)
    st.write("The predicted kidney disease status is", diagnosis)      #change to prediction

#create sidebar
st.sidebar.title("About CKD App")


with st.sidebar:
    st.write("""
            Please see your doctor for an accurate risk prediction. This tool is for learning purposes.  
            
            Please note that this tool is a work in progress. Contact me [here](mailto:ahobby@healthdatasciencenewsletter) or consider checking out [GitHub](https://github.com/AndreaHobby/CKD-Prediction/blob/main/Predicting%20Chronic%20Kidney%20Disease.ipynb) repository with any suggestions or questions.     
        """)




