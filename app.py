import streamlit as st
from PIL import Image
image=Image.open(bank1.jpeg)
st.image(image,caption='Welcome to XYZ Bank')
st.title('Loan calculator')
st.header('XYZ Bank of India')
x=st.number_input('Enter Your amount')
y=st.number_input('Enter your salary')
if y>=50000:
    st.write('Congratulations')
    st.balloons()
else:
    st.write('Sorry')
z=st.radio('Are you a Govt. emp',options=['yes','no'])
st.checkbox('Do you have a credit card')
st.sidebar.header('Schemes from Loan Dept.')

