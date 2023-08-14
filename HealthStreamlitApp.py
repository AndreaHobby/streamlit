import streamlit as st
from PIL import Image
import numpy as np
import pickle

st.set_page_config(layout='wide', page_title='CKD App')
st.title('Chronic Kidney Disease Prediction')
image = Image.open('./image/fnalkidney-comp_1087848275.png')
st.image(image, caption='Kidney')

model = pickle.load(open('model.pkl', 'rb'))

# Define the options and their corresponding float values here

age_options = ["<40", "40-49", "50-59", "60-69", "70+"]
age_float = list(map(float, range(len(age_options))))

gender_options = ["Male", "Female"]
gender_float = list(map(lambda x: float(1.0) if x == "Male" else float(0.0), gender_options))

racegrp_options = ["White", "Black", "Hispanic", "Asian", "Other"]
racegrp_float = list(map(float, range(len(racegrp_options))))

education_options = ["<High School", "High School/GED", "Some College", "College Graduate"]
education_float = list(map(float, range(len(education_options))))

marital_status_options = ["Married", "Widowed", "Divorced", "Separated", "Never Married"]
marital_status_float = list(map(float, range(len(marital_status_options))))

income_options = ["<20k", "20-34k", "35-49k", "50-74k", "75-99k", "100k+"]
income_float = list(map(float, range(len(income_options))))
caresource_options = ["Doctor's Office/Clinic", "Hospital Inpatient", "Emergency Room"]
caresource_float = list(map(float, range(len(caresource_options))))
health_insurance_options = ["Yes", "No"]
health_insurance_float = list(map(float, range(len(health_insurance_options))))

weight_options = ["Underweight", "Normal", "Overweight", "Obese"]
weight_float = list(map(float, range(len(weight_options))))

height_options = ["<5ft", "5ft-5ft5in", "5ft5in-6ft", ">6ft"]
height_float = list(map(float, range(len(height_options))))

sbp_options = ["<120", "120-129", "130-139", "140-149", "150+"]
sbp_float = list(map(float, range(len(sbp_options))))

dbp_options = ["<80", "80-84", "85-89", "90-99", "100+"]
dbp_float = list(map(float, range(len(dbp_options))))

hdl_options = ["<40", "40-49", "50-59", "60+"]
hdl_float = list(map(float, range(len(hdl_options))))

ldl_options = ["<100", "100-129", "130-159", "160-189", "190+"]
ldl_float = list(map(float, range(len(ldl_options))))

total_chol_options = ["<200", "200-239", "240-279", "280+"]
total_chol_float = list(map(float, range(len(total_chol_options))))

dyslipidemia_options = ["Yes", "No"]
dyslipidemia_float = list(map(float, range(len(dyslipidemia_options))))

pvd_options = ["Yes", "No"]
pvd_float = list(map(float, range(len(pvd_options))))

activity_options = ["Inactive", "Moderately Active", "Active"]
activity_float = list(map(float, range(len(activity_options))))

poor_vision_options = ["Yes", "No"]
poor_vision_float = list(map(float, range(len(poor_vision_options))))
smoker_options = ["Current Smoker", "Former Smoker", "Never Smoked"]
smoker_float = list(map(float, range(len(smoker_options))))

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
age = st.selectbox("Age", age_options)
gender = st.selectbox("Gender", gender_options)
racegrp = st.selectbox("Race", racegrp_options)
education = st.selectbox("Education", education_options)
marital_status = st.selectbox("Marital Status", marital_status_options)
income = st.selectbox("Income", income_options)

st.subheader('Healthcare')
caresource = st.selectbox("Where do you usually receive your healthcare?", caresource_options)
health_insurance = st.selectbox('Do you have health insurance?', health_insurance_options)
weight = st.selectbox('What is your Weight?', weight_options)
height = st.selectbox('What is your Height?', height_options)
sbp = st.selectbox('What is your systolic blood pressure?', sbp_options)
dbp = st.selectbox('What is your diastolic blood pressure?', dbp_options)
HDL = st.selectbox('What is your HDL?', hdl_options)
LDL = st.selectbox('What is your LDL?', ldl_options)
Total_Cholesterol = st.selectbox('What is your Total Cholesterol?', total_chol_options)
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

if st.button("CKD Risk Result"):
    input_data = np.array([
        age_float[age_options.index(age)],
        gender_float[gender_options.index(gender)],
        racegrp_float[racegrp_options.index(racegrp)],
        education_float[education_options.index(education)],
        marital_status_float[marital_status_options.index(marital_status)],
        income_float[income_options.index(income)],
        caresource_float[caresource_options.index(caresource)],
        health_insurance_float[health_insurance_options.index(health_insurance)],
        weight_float[weight_options.index(weight)],
        height_float[height_options.index(height)],
        sbp_float[sbp_options.index(sbp)],
        dbp_float[dbp_options.index(dbp)],
        hdl_float[hdl_options.index(HDL)],
        ldl_float[ldl_options.index(LDL)],
        total_chol_float[total_chol_options.index(Total_Cholesterol)],
        dyslipidemia_float[dyslipidemia_options.index(Dyslipidemia)],
        pvd_float[pvd_options.index(PVD)],
        activity_float[activity_options.index(Activity)],
        poor_vision_float[poor_vision_options.index(Poor_Vision)],
        smoker_float[smoker_options.index(Smoker)],
        hypertension_float[hypertension_options.index(Hypertension)],
        diabetes_float[diabetes_options.index(Diabetes)],
        stroke_float[stroke_options.index(Stroke)],
        cvd_float[cvd_options.index(CVD)],
        chf_float[chf_options.index(CHF)],
        anemia_float[anemia_options.index(Anemia)],
        fam_hypertension_float[fam_hypertension_options.index(Fam_Hypertension)],
        fam_diabetes_float[fam_diabetes_options.index(Fam_Diabetes)],
        fam_cvd_float[fam_cvd_options.index(Fam_CVD)]
    ])

    input_data = input_data.reshape(1, -1)
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        diagnosis = "CKD"
    else:
        diagnosis = "No CKD"

    st.markdown("The predicted kidney disease status is **{}**".format(diagnosis))
