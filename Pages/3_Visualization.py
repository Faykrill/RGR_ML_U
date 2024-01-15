import streamlit as st
import matplotlib as mp
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config('Visualization')

df = pd.read_csv('C:\\Users\\Максим\\RGRML\\Datasets\\ss3.csv')
variable_1 = st.sidebar.radio('Choose a variable', ('Path Traveled', 'Trip Duration', 'Hour'))
variable_2 = st.sidebar.radio('Choose a variable', ('Path Traveled', 'Trip Duration', 'Hour'),
index=2)

st.sidebar.write('Type of chart: ')
if st.sidebar.button('Line'):
    st.line_chart(df, x= variable_1, y= variable_2)
    
if st.sidebar.button('Bar Chart'):
    st.bar_chart(df, x= variable_1, y= variable_2)
    
if st.sidebar.button('Area Chart'):
    st.area_chart(df, x= variable_1, y= variable_2)
    
if st.sidebar.button('Scatter'):
    st.scatter_chart(df, x= variable_1, y= variable_2)
# st.sidebar.checkbox('Line', st.line_chart(df, x='Path Traveled', y='Trip Duration'))
# st.sidebar.checkbox('Bar Chart', st.bar_chart(df, x='Trip Duration', y='Path Traveled'))


