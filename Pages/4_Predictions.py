import streamlit as st
import pandas as pd
import pickle
from category_encoders.binary import BinaryEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np
#from sklearn.metrics import r2_score
#from tensorflow import keras

df = pd.read_csv('C:\\Users\\Максим\\RGRML\\Datasets\\ss3.csv')

df = df.drop(columns = ['Unnamed: 0', 'ID', 'Vendor ID', 'Pickup Datetime', 'Dropoff Datetime', 
                        'Passenger Count', 'Pickup Longitude', 'Pickup Latitude', 'Dropoff Longitude',
                        'Dropoff Latitude'])
st.write(df)

st.header("Получение прогноза для конкретного экземпляра")
hour_slider = st.slider("Время(ч)", 0,  df["Hour"].max())
minute_slider = st.slider("Время(мин)", 0,  df["Minute"].max())
weekday_slider = st.slider("День недели", 0,  df["Weekday"].max())
pt_num_in = st.number_input('Пройденный путь(0 - 1240.51)', df['Path Traveled'].min(), df['Path Traveled'].max())
trip_slider = st.slider('Продолжительность', 0, df['Trip Duration'].max())
new_df = pd.DataFrame(
    [[
        trip_slider,
        hour_slider,
        minute_slider,
        weekday_slider,
        
        
        pt_num_in
    ]],
    columns=df.columns,
)

st.subheader("Введённые данные")
st.write(new_df)

predictions = []
btn = st.button("Рассчитать")

if btn:
    with open('C:\\Users\\Максим\\RGRML\\Models\\TreeReg_model.pkl', 'rb') as f:
        reg = pickle.load(f)
        pred = reg.predict(new_df)[0]
        predictions.append(pred)
        st.write("Древовидная регрессия: " + str(round(pred)))
 
    with open('C:\\Users\\Максим\\RGRML\\Models\\BaggingR_model.pkl', 'rb') as f:
        reg = pickle.load(f)
        pred = reg.predict(new_df)[0]
        predictions.append(pred)
        st.write("Bagging: " + str(round(pred)))
               
    with open('C:\\Users\\Максим\\RGRML\\Models\\GradientBR_model.pkl', 'rb') as f:
        reg = pickle.load(f)
        pred = reg.predict(new_df)[0]
        predictions.append(pred)
        st.write("Градиентный бустинг: " + str(round(pred)))
        
    with open('C:\\Users\\Максим\\RGRML\\Models\\KMeans_clast.pkl', 'rb') as f:
        reg = pickle.load(f)
        pred = reg.predict(new_df)[0]
        predictions.append(pred)
        st.write("Kmeans(кластеризация): " + str(round(pred)))
        
    with open('C:\\Users\\Максим\\RGRML\\Models\\MLPR_NC.pkl', 'rb') as f:
        reg = pickle.load(f)
        pred = reg.predict(new_df)[0]
        predictions.append(pred)
        st.write("MLP: " + str(round(pred)))
        
    # with open('C:\\Users\\Максим\\RGRML\\Models\\Kmeans_NC.pkl', 'rb') as f:
    #     reg = pickle.load(f)
    #     pred = reg.predict(new_df)[0]
    #     predictions.append(pred)
    #     st.write("Kmeans НС: " + str(round(pred)))
    
