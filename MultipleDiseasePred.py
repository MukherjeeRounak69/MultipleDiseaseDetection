# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:27:37 2024

@author: ROUNAK
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabetes_model=pickle.load(open('C:/Users/ROUNAK/Desktop/Multiple Disease Prediction/diabetes_model.sav','rb'))
heart_model=pickle.load(open('C:/Users/ROUNAK/Desktop/Multiple Disease Prediction/heart_model.sav','rb'))
park_model=pickle.load(open('C:/Users/ROUNAK/Desktop/Multiple Disease Prediction/parl_model.sav','rb'))
with st.sidebar:
    selected=option_menu('Your One Stop Health CheckUp Site!',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Disease Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
    
if selected=='Diabetes Prediction':
    
    st.title('Diabetes Prediction using Machine Learning')
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input('Number of pregnancies')
    with col2:
        glucose=st.text_input('Glucose Level')
    with col3:
        bp=st.text_input('Blood Pressure Value')
    with col1:
        skinthick=st.text_input('Skin Thickness Value')
    with col2:
        insulin=st.text_input('Insulin Level')
    with col3:
        bmi=st.text_input('Body Mass Index')
    with col1:
        diabetespedigreefunc=st.text_input('Diabetes Pedigree Function Value')
    with col2:
        age=st.text_input('Age')
    
    diab_diagnosis=''
    if st.button('Am I diabetic?'):
        diab_prediction=diabetes_model.predict([[pregnancies,glucose,bp,skinthick,insulin,bmi,diabetespedigreefunc,age]])
        if diab_prediction[0]==0:
            diab_diagnosis='Not diabetic (yet)!'
        else:
            diab_diagnosis='Quit sweets or you will die!'
    st.success(diab_diagnosis)
  
    
  
if selected=='Heart Disease Prediction':
    
    st.title('Heart Disease Prediction using Machine Learning')
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input('Age')
    with col2:
        glucose=st.text_input('Sex')
    with col3:
        bp=st.text_input('Chest Pain Type (4 values)')
    with col1:
        skinthick=st.text_input('Resting Blood Pressure')
    with col2:
        insulin=st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        bmi=st.text_input('Fasting Blood Sugar 120 mg/dl')
    with col1:
        diabetespedigreefunc=st.text_input('Resting ElectroCardioGraphic Results (lvl 0/1/2')
    with col2:
        age=st.text_input('Maximum Heart Rate')
    with col3:
        b=st.text_input('Excercise Induced Angina')
    with col1:
        c=st.text_input('oldpeak=ST depression induced by excercise relative to rest')
    with col2:
        a=st.text_input('Slope of the peak excercise ST segment')
    with col3:
        p=st.text_input('Number of major vessels coloured by fluroscopy (0/1/2/3)')
    with col1:
        s=st.text_input('Thal (0-normal/1-fixed defect/2-reversible defect)')
    
    heart_diagnosis=''
    if st.button('Will I have a heart attack?'):
        heart_prediction=heart_model.predict([[pregnancies,glucose,bp,skinthick,insulin,bmi,diabetespedigreefunc,age,b,c,a,p,s]])
        if heart_prediction[0]==0:
            heart_diagnosis='Safe, for now.'
        else:
            heart_diagnosis='Heart Attack in 3...2...1..'
    st.success(heart_diagnosis)
    
    
    
    
    
    
    
if selected=='Parkinsons Disease Prediction':
    st.title('Parkinsons Disease Prediction using Machine Learning')
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input('MDVP:Fo(Hz)')
    with col2:
        glucose=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        bp=st.text_input('MDVP:Flo(Hz)')
    with col1:
        skinthick=st.text_input('MDVP:Jitter(%)')
    with col2:
        insulin=st.text_input('MDVP:Jitter(Abs)')
    with col3:
        bmi=st.text_input('MDVP:RAP')
    with col1:
        diabetespedigreefunc=st.text_input('MDVP:PPQ')
    with col2:
        age=st.text_input('Jiteer:DDP')
    with col3:
        b=st.text_input('MDVP:Shimmer')
    with col1:
        c=st.text_input('MDVP:Shimmer(dB)')
    with col2:
        a=st.text_input('Shimmer:APQ3')
    with col3:
        p=st.text_input('Shimmer:APQ5')
    with col1:
        s=st.text_input('MDVP:APQ')
    with col2:
        a1=st.text_input('Shimmer:DDA')
    with col3:
        a2=st.text_input('NHR')
    with col1:
        a3=st.text_input('HNR')
    with col2:
        a4=st.text_input('RPDE')
    with col3:
        a5=st.text_input('DFA')
    with col1:
        a6=st.text_input('Spread1')
    with col2:
        a7=st.text_input('Spread2')
    with col3:
        a8=st.text_input('D2')
    with col1:
        a9=st.text_input('PPE')
    
    park_diagnosis=''
    if st.button('Do I have Parkinsons?'):
        park_prediction=park_model.predict([[pregnancies,glucose,bp,skinthick,insulin,bmi,diabetespedigreefunc,age,b,c,a,p,s,a1,a2,a3,a4,a5,a6,a7,a8,a9]])
        if park_prediction[0]==0:
            park_diagnosis='Negative <3'
        else:
            park_diagnosis='Positive!'
    st.success(park_diagnosis)