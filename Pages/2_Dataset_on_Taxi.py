import streamlit as st
import pandas as pd

st.set_page_config('Dataset on Taxi')

st.write('### Dataset из 3 лабороторной')
st.write('___')
st.write('Данный набор данных посвящён поездкам в такси. '
         'Целевым признаком для модели регрессии являлось время в поездке.')
st.markdown('+ ID - ID поездки\n '
            '+ Vendor ID - ID поставщика\n '
            '+ Pickup Datetime - Время посадки\n '
            '+ Dropoff Datetime - Время высадки\n '
            '+ Passenger Count - Количество поссажиров\n '
            '+ Pickup Longitude - Долгота в начале поездки\n '
            '+ Pickup Latitude - Широта в начале поездки\n '
            '+ Dropoff Longitude - Долгота в конце поездки\n '
            '+ Dropoff Latitude - Широта в конце поездки\n '
            '+ Trip Duration - Время поездки(сек)\n ')

st.markdown('В процессе предобработки данных были удалены все пропущенные значения и добавлены столбцы: \n'
            '+ Hour - Время начала поездки(ч)\n '
            '+ Minute - Время начала поездки(мин)\n '
            '+ Weekday - Дата начала поездки(день недели)\n '
            '+ Path Traveled - Пройденное расстояние(км)\n '
            '\n'
            'Также почищены выбросы у важных для регрессии данных.')

df = pd.read_csv('C:\\Users\\Максим\\RGRML\\Datasets\\ss3.csv')
st.write(df.head(10))
