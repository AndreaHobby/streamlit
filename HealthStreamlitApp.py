#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[3]:


import matplotlib.pyplot as plt

# Generate a plot using matplotlib
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

# Display the plot in the Streamlit app
st.pyplot()


# In[5]:


import streamlit as st

# Add a button to the app
if st.button('Say hello'):
    st.write('Hello!')

# Add a text input field
name = st.text_input('Enter your name')
st.write('Hello, {}!'.format(name))


# In[6]:




