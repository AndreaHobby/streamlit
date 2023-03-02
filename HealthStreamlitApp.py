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
with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


