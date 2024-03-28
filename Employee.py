import pandas as pd
import streamlit as st
import joblib


model = joblib.load('EmployeeAtt.pkl')
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition (2).csv')

st.markdown("<h1 style = 'color: #5F0F40; text-align: center; font-family:TaHoma'>EMPLOYEE ATTRITION PREDICTION</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FFB0B0; text-align: center; font-family: cursive '>Built By ibrahim lawal </h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com(56).png')

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

# Input User ImOver18 
st.sidebar.image('pngwing.com(23).png', caption = 'Welcome User')

# Apply space in the sidebar 
st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)



# Declare user Input variables 
st.sidebar.subheader('Input Variables', divider= True)
bus_travel = st.sidebar.selectbox('BusinessTravel', df['BusinessTravel'].unique())
dept = st.sidebar.selectbox('Department', df['Department'].unique())
edu_field = st.sidebar.selectbox('EducationField', df['EducationField'].unique())
gender = st.sidebar.selectbox('Gender', df['Gender'].unique())
job_role = st.sidebar.selectbox('JobRole', df['JobRole'].unique())
mar_sta = st.sidebar.selectbox('MaritalStatus', df['MaritalStatus'].unique())
over18= st.sidebar.selectbox('Over18', df['Over18'].unique())
over_time = st.sidebar.selectbox('OverTime', df['OverTime'].unique())


# display the users input
input_var = pd.DataFrame()


input_var['BusinessTravel'] = [bus_travel]
input_var['Department'] = [dept]
input_var['EducationField'] = [edu_field ]
input_var['Gender'] = [gender]
input_var['JobRole'] = [job_role]
input_var['MaritalStatus'] = [mar_sta]
input_var['Over18'] = [over18]
input_var['OverTime'] =[over_time]


st.markdown("<br>", unsafe_allow_html= True)
# display the users input variable 
st.subheader('Users Input Variables')
st.dataframe(input_var)


bus_travel = joblib.load('BusinessTravel_encoder.pkl')
dept = joblib.load('Department_encoder.pkl')
edu_field = joblib.load('EducationField_encoder.pkl')
gender = joblib.load('Gender_encoder.pkl')
job_role = joblib.load('JobRole_encoder.pkl')
mar_sta = joblib.load('MaritalStatus_encoder.pkl')
over18 = joblib.load('Over18_encoder.pkl')
over_time= joblib.load('OverTime_encoder.pkl')


# transform the users input with the imported scalers 
input_var['BusinessTravel'] = bus_travel.transform(input_var[['BusinessTravel']])
input_var['Department'] = dept.transform(input_var[['Department']])
input_var['EducationField'] = edu_field.transform(input_var[['EducationField']])
input_var['Gender'] = gender.transform(input_var[['Gender']])
input_var['JobRole'] = job_role.transform (input_var[['JobRole']])
input_var['MaritalStatus'] = mar_sta.transform (input_var[['MaritalStatus']])
input_var['Over18'] = over18.transform(input_var[['Over18']]) 
input_var['OverTime'] = over_time.transform(input_var[['OverTime']]) 

st.markdown("<br>", unsafe_allow_html= True)
st.divider()


model = joblib.load('EmployeeAtt.pkl')
predicted = model.predict(input_var)

if st.button('Predict Attrition'):
    if predicted == 0:
        st.failure('Employee Has LEFT')
    else:
        st.success('Employee still works for Us')