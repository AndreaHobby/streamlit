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

age_options = ["<40", "40-49", "50-59", "60-69", "70+"]
age_options_float = list(map(float, age_options))

gender_options = ["Male", "Female"]
gender_float = list(map(lambda x: float(1.0) if x == "Male" else float(0.0), gender_options))

racegrp_options = ["White", "Black", "Hispanic", "Asian", "Other"]
education_options = ["<High School", "High School/GED", "Some College", "College Graduate"]
marital_status_options = ["Married", "Widowed", "Divorced", "Separated", "Never Married"]

income_options = ["<20k", "20-34k", "35-49k", "50-74k", "75-99k", "100k+"]
income_options_float = list(map(float, [i[:-1] for i in income_options]))

 
  
caresource_options = ["Doctor's Office/Clinic", "Hospital Inpatient", "Emergency Room"]
caresource_options_float = list(map(float, range(len(caresource_options))))

health_insurance_options = ["Yes", "No"]
health_insurance_options_float = list(map(float, range(len(health_insurance_options))))

weight_options = ["Underweight", "Normal", "Overweight", "Obese"]
weight_options_float = list(map(float, range(len(weight_options))))

height_options = ["<5ft", "5ft-5ft5in", "5ft5in-6ft", ">6ft"]
height_options_float = list(map(float, range(len(height_options))))

sbp_options = ["<120", "120-129", "130-139", "140-149", "150+"]
sbp_options_float = list(map(float, range(len(sbp_options))))

dbp_options = ["<80", "80-84", "85-89", "90-99", "100+"]
dbp_options_float = list(map(float, range(len(dbp_options))))

hdl_options = ["<40", "40-49", "50-59", "60+"]
hdl_options_float = list(map(float, range(len(hdl_options))))

ldl_options = ["<100", "100-129", "130-159", "160-189", "190+"]
ldl_options_float = list(map(float, range(len(ldl_options))))

total_chol_options = ["<200", "200-239", "240-279", "280+"]
total_chol_options_float = list(map(float, range(len(total_chol_options))))

dyslipidemia_options = ["Yes", "No"]
dyslipidemia_options_float = list(map(float, range(len(dyslipidemia_options))))

pvd_options = ["Yes", "No"]
pvd_options_float = list(map(float, range(len(pvd_options))))

activity_options = ["Inactive", "Moderately Active", "Active"]
activity_options_float = list(map(float, range(len(activity_options))))

poor_vision_options = ["Yes", "No"]
poor_vision_options_float = list(map(float, range(len(poor_vision_options))))

smoker_options = ["Current Smoker", "Former Smoker", "Never Smoked"]
smoker_options_float = list(map(float, range(len(smoker_options))))

hypertension_options = ["Yes", "No"]
hypertension_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), hypertension_options))

diabetes_options = ["Yes", "No"]
diabetes_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), diabetes_options))

stroke_options = ["Yes", "No"]
stroke_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), stroke_options))

cvd_options = ["Yes", "No"]
cvd_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), cvd_options))

chf_options = ["Yes", "No"]
chf_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), chf_options))

anemia_options = ["Yes", "No"]
anemia_options_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), anemia_options))
 
fam_hypertension_options = ["Yes", "No"]
fam_hypertension_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_hypertension_options))

fam_diabetes_options = ["Yes", "No"]
fam_diabetes_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_diabetes_options))

fam_cvd_options = ["Yes", "No"]
fam_cvd_float = list(map(lambda x: float(1.0) if x == "Yes" else float(0.0), fam_cvd_options))
 
st.subheader('Demographics')   
age = st.selectbox("Age", age_options)
gender = st.selectbox("Gender", gender_options)
racegrp = st.selectbox("Race", racegrp_options)
education = st.selectbox("Education", education_options)
marital_status = st.selectbox("Marital Status", marital_status_options)
income = st.selectbox("Income", income_options)
 
st.subheader('Healthcare') 
caresource = st.selectbox("Where do you usually receive you healthcare?", caresource_options)
health_insurance = st.selectbox('Do you have health insurance?', health_insurance_options)
weight = st.selectbox('What is your Weight?', weight_options)
height = st.selectbox('What is your Height?', height_options)
sbp = st.selectbox('What is your systolic blood pressure? Normal: Below 120/80 Elevated: 120 to 129/less than 80. Stage 1 high blood pressure: 130 to 139/80 to 89. Stage 2 high blood pressure: 140 and above/90 and above. Hypertension crisis: above 180/above 120. https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings', sbp_options)
dbp = st.selectbox('What is your diastolic blood pressure?', dbp_options)
HDL = st.selectbox('What is your HDL? Normal: 35 to 65 mg/dL for men, 35 to 80 mg/dL for women.', hdl_options)
LDL = st.selectbox('What is your LDL? Less than 100 mg/dL (This is the goal for people with diabetes or heart disease.) Near optimal: 100 to 129 mg/dL. Borderline high: 130 to 159 mg/dL.', ldl_options)
Total_Cholesterol = st.selectbox('What is your Total Cholesterol? Normal: less than 200 mg/dL. Borderline high: 200 to 239 mg/dL. High: at or above 240 mg/dL.', total_chol_options)
Dyslipidemia = st.selectbox('Do you have Dyslipidemia?', dyslipidemia_options)
PVD = st.selectbox('Do you have a history Peripheral Artery Disease?', pvd_options)
Activity = st.selectbox('What is your level of physical activity every week?', activity_options)
Poor_Vision = st.selectbox('Do you have poor vision that cannot be corrected with glasses, contact lenses, or surgery?', poor_vision_options)
Smoker = st.selectbox('Are you a current or former smoker?', smoker_options)
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
    input_data = [age_float,
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
HDL_float,
LDL_float,
Total_Cholesterol_float,
Dyslipidemia_float,
PVD_float,
Activity_float,
Poor_Vision_float,
Smoker_float,
Hypertension_float,
Diabetes_float,
Stroke_float,
CVD_float,
CHF_float,
Anemia_float,
Fam_Hypertension_float,
Fam_Diabetes_float,
Fam_CVD_float]  
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



