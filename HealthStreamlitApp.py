import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st

st.title('Chronic Kidney Disease Prediction')

#adds image 
image = Image.open('./image/fnalkidney-comp_1087848275.png')
st.image(image, caption='Sunrise by the mountains')

st.write(f'Chronic kidney disease (CKD) is when the kidneys are damaged and cannot correctly filter waste and excess fluids from the blood. 
About 37 million people in the United States have Chronic Kidney Disease (CKD). Early detection and diagnosis of CKD are essential to
preventing its progression to kidney failure. Machine learning models can assist in predicting CKD. This project is the user interface for 
a previous project of mine that uses National Center for Health Statistics (NCHS) data. Variables such as age, gender, medical history, and laboratory
test results will be used. By identifying patterns in the data, models can predict a patient's risk of developing CKD, allowing for early intervention and management.')

name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)

#create sidebar
st.sidebar.title("Pick Your Feature")

st.sidebar.subheader("Choose classifier")
classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")
        
        st.write("""
            ## About
            The CKD Prediction Tool is..... . 
            
            Please note that this tool is a work in progress. Contact us [here](mailto:ahobby@healthdatasciencenewsletter) or consider checking out [GitHub](https://github.com/AndreaHobby/CKD-Prediction/blob/main/Predicting%20Chronic%20Kidney%20Disease.ipynb) repository with any suggestions or questions.     
        """)

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")



