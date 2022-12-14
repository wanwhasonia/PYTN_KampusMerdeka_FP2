import pickle
import streamlit as st

model= pickle.load(open('svm.pkl','rb'))

def main():
    st.title('Prediksi Kejadian Hujan Esok Hari')

    #input variables
    Rainfall = st.text_input('Rainfall : ')
    Sunshine = st.text_input('Sunshine : ')
    WindGustSpeed = st.text_input('WindGustSpeed')
    Humidity3pm = st.text_input('Humidity3pm')
    Pressure9am = st.text_input('Pressure9am')
    RainToday = st.text_input('RainToday')
    
    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[Rainfall, Sunshine, WindGustSpeed, Humidity3pm, Pressure9am, RainToday]])
        output=makeprediction[0]
        st.success('Besok tidak turun hujan')

if __name__=='__main__':
    main()