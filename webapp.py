import streamlit as st 
import pandas as pd
import joblib

st.title('Insurance Cross Sell Prediction')


# reading the dataset to fill the values in the dropdown list
df=pd.read_csv('train_hackathon.csv')

#creating the input fields
Gender=st.selectbox("Gender",pd.unique(df['Gender']))
Age=st.number_input("Age")
Driving_License=st.selectbox("Driving_License",pd.unique(df['Driving_License']))
Region_Code=st.selectbox("Region_Code",pd.unique(df['Region_Code']))
Previously_Insured=st.selectbox("Previously_Insured",pd.unique(df['Previously_Insured']))
Vehicle_Age=st.selectbox("Vehicle_Age",pd.unique(df['Vehicle_Age']))
Vehicle_Damage=st.selectbox("Vehicle_Damage",pd.unique(df['Vehicle_Damage']))
Annual_Premium=st.number_input("Annual_Premium")
Policy_Sales_Channel=st.selectbox("Policy_Sales_Channel",pd.unique(df['Policy_Sales_Channel']))
Vintage=st.number_input("Vintage")

if Gender=='Male':
    Gender=1
else:
    Gender=0
    
if Vehicle_Age=='< 1 Year':
    Vehicle_Age=0
elif Vehicle_Age=='1-2 Year':
    Vehicle_Age=1
else:
    Vehicle_Age=2
    
if Vehicle_Damage=='Yes':
    Vehicle_Damage=1
else:
    Vehicle_Damage=0
    

#converting the input values to a dictionary

inputs = {
    "Gender":Gender,
    "Age":Age,
    "Driving_License":Driving_License,
    "Region_Code":Region_Code,
    "Previously_Insured":Previously_Insured,
    "Vehicle_Age":Vehicle_Age,
    "Vehicle_Damage":Vehicle_Damage,
    "Annual_Premium":Annual_Premium,
    "Policy_Sales_Channel":Policy_Sales_Channel,
    "Vintage":Vintage
 
    }

# click button for prediction

if st.button("Predict"):
    model=joblib.load("insurance_cross_sell_predictionmodel.pkl")
    #input to the fields
    X_input = pd.DataFrame(inputs, index=[0])
    #model prediction
    prediction = model.predict(X_input)
    #display the prediction
    st.markdown(f"### Prediction: `{prediction}`")


    
    

