# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:05:06 2023

@author: saite
"""

import pickle 
import numpy as np
import streamlit as st

#loading the ml model
loaded_model=pickle.load(open(r"C:\Users\saite\Trained_wine","rb"))
def wine_prediction(input_data):
    input_data_asarray=np.asarray(input_data)
    input_data_reshape=input_data_asarray.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction[0]==1):
        print("Good quality wine")
    else:
        print("Bad quality wine")

def main():
    #giving the title
    st.title("Wine prediction")
    fixedAcidity=st.text_input('fixedAcidity')
    volatileAcidity=st.text_input('VolatileAcidity')
    citricAcid=st.text_input('CitricAcid')
    residualSugar=st.text_input('ResidualSugar')
    chlorides=st.text_input('Chlorides')
    freeSulpherDioxide=st.text_input('freeSulphurDioxide') 
    totalSulpherDioxide=st.text_input('totalSulphurDioxide')
    density=st.text_input('Density')
    ph=st.text_input('PH')
    sulphates=st.text_input('Sulphates')
    alchohol=st.text_input('alchohol')
    #code for prediction
    Qualityofalchohol=""
    if st.button('Test Result: '):
        Qualityofalchohol=wine_prediction(fixedAcidity,volatileAcidity,citricAcid,residualSugar,chlorides,freeSulpherDioxide,totalSulpherDioxide,density,ph,sulphates,alchohol)
    st.success(Qualityofalchohol)

if __name__=="__main__":
    main()
    