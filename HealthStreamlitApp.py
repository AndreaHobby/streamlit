import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st

st.title('Chronic Kidney Disease Prediction')

#adds image 
image = Image.open('./image/fnalkidney-comp_1087848275.png')
st.image(image, caption='Sunrise by the mountains')

name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')
x = st.slider('Select an integer x', 0, 10, 1)
y = st.slider('Select an integer y', 0, 10, 1)
df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(df)

#create sidebar
st.sidebar.title("Pick Your Feature")

# Now, add demographic variables for predictiion
sqft = row2_3.number_input('Living Space - Sqft', min_value=381, max_value=5000, value=4800, help="Min=381, Max=5000")
median_price_sqft_cluster = row2_4.number_input('Median sqft Price',min_value=207, max_value=850, value=720, help="Min=207, Max=850")
gsRating = row2_4.number_input('GreatSchools Rating', min_value=1, max_value=10, value=9, help="Min=1, Max=10, [GreatSchools.org](https://www.greatschools.org/)")
median_income = row2_4.number_input('Annual Income', min_value=45000, max_value=182000, value=170000, help="Min=$25K, Max=$182K")
lot_size = row2_3.number_input('Lot Size', min_value=0, max_value=18000, value=4800, help="Min=0, Max=18000")
property_type = row2_3.selectbox('Property Type', ('Single Family Residential', 'Condo/Co-op', 'Townhouse'), index=0)
beds = row2_3.selectbox('Num of Bedrooms', (1, 2, 3, 4, 5), index=3)
zipcode = row2_4.selectbox('Zip Code', (94506,94507,94509,94518,94519,94521,94523,94526,94531,94541,94544,94545,
                                       94546,94550,94551,94553,94565,94566,94568,94577,94578,94582,94583,94588,
                                       94595,94597,94598,94801,94804,95050,95051), index=18)
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



