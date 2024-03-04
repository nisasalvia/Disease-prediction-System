# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:46:01 2024

@author: Admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/heart_disease_model.sav', 'rb'))
ckd_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/ckd_model.sav', 'rb'))
hepatitis_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/hepatitis_model.sav', 'rb'))
cancer_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/Cancer_model.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/Admin/OneDrive/Desktop/Multiple disease prediction system/saved models/parkinson_model .sav', 'rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction','Chronic kidney disease prediction','Cancer prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'file-earmark-medical-fill','person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

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
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

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

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
# ckd prediction page
if selected == 'Chronic kidney disease prediction':
    # page title
    st.title('CKD Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 ,col4 = st.columns(4)
    
    with col1:
        Id = st.text_input('patient ID')

    with col2:
        age = st.text_input('Age')

    with col3:
        bp = st.text_input('Blood Pressure')

    with col4:
        al = st.text_input('Albumin')

    with col1:
        su = st.text_input('Sugar Level')

    with col2:
        bgr = st.text_input('Blood Glucose Random(BGR)')

    with col3:
        bu = st.text_input('Blood Urea')

    with col4:
        sc = st.text_input('Serum Creatinine')
        
    with col1:
        sod = st.text_input('Sodium Level')
        
    with col2:
        hemo = st.text_input('Hemoglobin (Hb) Level')
        
    with col3:
        pcv = st.text_input('Packed Cell Volume(PCV)')
        
        
    # code for Prediction
    ckd_diagnosis = ''

    # creating a button for Prediction

    if st.button('CKD Test Result'):

        user_input = [Id,age,bp,al,su,bgr,bu,sc,sod,hemo,pcv]

        user_input = [float(x) for x in user_input]

        ckd_prediction = ckd_model.predict([user_input])

        if ckd_prediction[0] == 1 :
            ckd_diagnosis = 'THE PATIENT HAS CHRONIC KIDNEY DISEASE'
        else:
            ckd_diagnosis = 'THE PATIENT DOES NOT HAVE CHRONIC KIDNEY DISEASE'

    st.success(ckd_diagnosis)
    
    
# Cancer Prediction Page
if selected == 'Cancer prediction':

    # page title
    st.title('Cancer prediction using ML')

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        Age = st.text_input('Age')

    with col2:
        AirPollution = st.text_input('Air Pollution in your area')

    with col3:
        Alcoholuse = st.text_input('Alcohol Intake')

    with col4:
        DustAllergy = st.text_input('Dust Allergy')

    with col1:
        GeneticRisk = st.text_input('Genetic Risk')

    with col2:
        Obesity = st.text_input('Obesity')

    with col3:
        Snoring = st.text_input('Snoring')

    with col4:
        FrequentCold = st.text_input('Frequent Cold')
        
    with col1:
        ChestPain = st.text_input('Chest Pain')

    with col2:
        Fatigue = st.text_input('Fatigue')

    with col3:
        Smoking = st.text_input('Smoking')

    with col4:
        SwallowingDifficulty = st.text_input('Swallowing Difficulty')

    with col1:
        ShortnessofBreath = st.text_input('Shortness of Breath')  
        
    with col2:
       PassiveSmoker = st.text_input('Passive Smoking')

    with col3:
        WeightLoss = st.text_input('Weight Loss')

    with col4:
        ClubbingofFingerNails = st.text_input('Clubbing of Finger Nails')

    with col1:
        DryCough = st.text_input('Dry Cough')


    # code for Prediction
    can_diagnosis = ''

    # creating a button for Prediction

    if st.button('Cancer Test Result'):

        user_input = [Age,AirPollution,Alcoholuse,DustAllergy,GeneticRisk,Obesity,
                      Smoking,PassiveSmoker,ChestPain,Fatigue,WeightLoss,ShortnessofBreath,
                      SwallowingDifficulty,ClubbingofFingerNails,FrequentCold,DryCough,Snoring]

        user_input = [float(x) for x in user_input]

        can_prediction = cancer_model.predict([user_input])

        if can_prediction[0] == 1:
            can_diagnosis = 'CANCER'
        else:
            can_diagnosis = 'NO CANCER'

    st.success(can_diagnosis)    
    
