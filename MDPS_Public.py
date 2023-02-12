# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:17:23 2022

@author: Sagar Waykar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))

Heart_Disease_model = pickle.load(open('Heart_Disease_model.sav', 'rb'))

Liver_Disease_model = pickle.load(open('Liver_Disease_model.sav', 'rb'))

Parkinsons_model = pickle.load(open('Parkinsons_model.sav', 'rb'))
                                    


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Health Diagnosis Prediction System using Machine Learning Model',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person-bounding-box','person'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value(mm Hg)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value(mm)')
    
    with col2:
        Insulin = st.text_input('Insulin Level(mu U/ml)')
    
    with col3:
        BMI = st.text_input('BMI value(weight in kg/(height in m)^2)')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person in years')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = Diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 0):
          diab_diagnosis = 'The person is not diabetic'
        else:
          diab_diagnosis = 'The person is diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age in years')
        
    with col2:
        sex = st.text_input('Sex (1 = male; 0 = female)')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('Thalium stress result (0=normal;1=fixed defect;2=reversable defect)')
        
   
    
   
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = Heart_Disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 0):
          heart_diagnosis = 'The Person does not have a Heart Disease'
        else:
          heart_diagnosis = 'The Person Has Heart Disease'
        
    st.success(heart_diagnosis)
        
    
    



# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):
    
    # page title
    st.title('Liver Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age in years')
        
    with col2:
        Gender = st.text_input('Gender (1 = male; 0 = female)')
        
    with col3:
        Total_Bilirubin = st.text_input('Total Billirubin in mg/dL')
        
    with col1:
        Direct_Bilirubin = st.text_input('Direct Bilirubin in mg/dL')
        
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase in IU/L')
        
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase in IU/L')
        
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase in IU/L')
        
    with col2:
        Total_Protiens = st.text_input('Total Protiens in g/dL')
        
    with col3:
        Albumin = st.text_input('Albumin in g/dL')
        
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')
        

        
   
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Liver Disease Test Result'):
        liver_prediction = Liver_Disease_model.predict([[age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])                          
        
        if (liver_prediction[0] <= 0.5):
          liver_diagnosis = 'person does not have a liver disease'
        else:
          liver_diagnosis = 'Person has a liver disease'
        
    st.success(liver_diagnosis)






# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = Parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 0):
          parkinsons_diagnosis = "The Person does not have Parkinsons Disease"
        else:
          parkinsons_diagnosis = "The Person has Parkinsons"
        
    st.success(parkinsons_diagnosis)
