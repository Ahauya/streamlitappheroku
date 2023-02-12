# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:08:01 2022

@author: arthu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the save prediction models

diabetes_model = pickle.load(open(r"C:\Users\arthu\OneDrive\Desktop\Multiple prediction systems\trained_model.sav","rb"))

heart_model = pickle.load(open(r"C:\Users\arthu\OneDrive\Desktop\Multiple prediction systems\saved models\heart_trained_model.sav","rb"))        

parkisons_model = pickle.load(open(r"C:\Users\arthu\OneDrive\Desktop\Multiple prediction systems\saved models\parkinson_trained_model.sav","rb"))      
breast_model = pickle.load(open(r"C:\Users\arthu\OneDrive\Desktop\Multiple prediction systems\breast_trained_model.sav", "rb"))
#Sidebar of web app

with st.sidebar:
    selected = option_menu("Multiple Disease Predection System",
                           ["Diabetes Predection",
                           "Heart Disease Predection",
                           "Parkisons Predection",
                           "Breast Cancer Prediction"],
                           icons=["activity", "suit-heart-fill", "person","gender-female"],
                           default_index=0
                           )


# Diabetes Predection Page      
if (selected=="Diabetes Predection"):
    st.title("Diabetes Predection using ML")
    
    ## Getting the input from the user
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
       Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("BloodPressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the person")
    
    #Predection Code
    diab_dignosis=""
    
    # Predection Buttun
    if st.button("Diabetes Test Results"):
        prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (prediction [0] == 1):
            diab_dignosis ="The Person Have Diabetes"
        else:
            diab_dignosis="The Person Doesn't Have Diabetes"
    st.success(diab_dignosis)
            
        
        
    
   
   

#age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
#Heart Disease Page
if (selected=="Heart Disease Predection"):
    st.title("Heart Predection using ML")
    
    ## Getting the input from the user
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
       sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Type")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesteral in Mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blodd Pressure > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting Electrocordiagraphic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang = st.text_input("Exercise Induted Angina")  
    with col1:
        oldpeak = st.text_input("St depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise")
    with col3:
        ca = st.text_input("Major Vessels colored by floursopy")    
    with col1:
         thal = st.text_input("thal: 0=normal; 1=fixed defect; 2= reversable defect")
        
        
      #Predection Code
    heart_dignosis=""
      
      # Predection Buttun
    if st.button("Heart Condition Test Results"):
          prediction= heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
          
          if (prediction [0] == 1):
              heart_dignosis ="The Person Have a Heart condition"
          else:
              heart_dignosis="The Person Doesn't have a Heart Condition"
    st.success(heart_dignosis)
        
        
        
        
#Parkisons Disease Page
if (selected=="Parkisons Predection"):
    st.title("Parkisons Predection using ML")
    
    
    # page title
    
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
        parkinsons_prediction = parkisons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

    #Parkisons Disease Page
if (selected=="Breast Cancer Prediction"):
        st.title("Breast Cancer Prediction using ML")
    
    # page title
  
        col1, col2, col3, col4, col5 = st.columns(5)  
    
        with col1:
            radius_mean = st.text_input('Radius_mean')
        
        with col2:
            texture_mean = st.text_input('Texture_mean')
        
        with col3:
            perimeter_mean = st.text_input('Perimeter_mean')
        
        with col4:
            area_mean = st.text_input('Area_mean')
        
        with col5:
            smoothness_mean = st.text_input('smoothness_mean')
        
        with col1:
            compactness_mean = st.text_input('Compactness_mean')
        
        with col2:
            concavity_mean = st.text_input('Concavity mean')
        
        with col3:
          concave_points_mean = st.text_input('Concave points mean')
        
        with col4:
            points_mean = st.text_input('Points mean')
        
        with col5:
            symmetry_mean = st.text_input('Symmetry mean')
#,
        
        with col2:
            radius_se = st.text_input('Radius se')
        
        with col3:
          texture_se = st.text_input('Texture se')
        
        with col4:
            perimeter_se = st.text_input('Perimeter se')
        
        with col5:
            area_se = st.text_input('Area se')
 
       
        with col1:
            smoothness_se = st.text_input('Smoothness se')
        
        with col2:
            compactness_se = st.text_input('Compactness se')
        
        with col3:
            concavity_se = st.text_input('Concavity se')
        
        with col4:
            concave_points_se = st.text_input('Concave points se')
        
        with col5:
            symmetry_se = st.text_input('Symmetry se')
        
        with col1:
            fractal_dimension_se = st.text_input('Fractal dimension se')
        
        with col2:
            radius_worst = st.text_input('radius_worst')
        
        with col1:
             texture_worst = st.text_input('Texture worst')
         
        with col2:
             perimeter_worst = st.text_input('Perimeter worst')
         
        with col3:
            area_worst = st.text_input("area_worst")
         
        with col4:
             smoothness_worst = st.text_input('Smoothness worst')
         
        with col5:
             compactness_worst = st.text_input('Compactness worst')

        with col1:
             concavity_worst = st.text_input('Concavity worst')
         
        with col5:
             concave_points_worstt = st.text_input('con points worst')
         
        with col3:
            symmetry_worst = st.text_input("Symmetry worst")
         
        with col4:
             fractal_dimension_worst = st.text_input('Fractal dim worst')
             
             
    # code for Prediction
        breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
        if st.button("Breast cancer Test Result"):
           breast_prediction = breast_model.predict([[]])
           
           if (breast_prediction[0] == 1):
                   breast_cancer_diagnosis = " Maligant Breast cancer present"
           else:
             breast_cancer_diagnosis = "  Benign Breast cancer present"
           
        st.success(breast_cancer_diagnosis)
           
           
           
           
                       
        
        










