import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing,encoder_Application_mode, encoder_Course, encoder_Debtor,encoder_Displaced,encoder_Educational_special_needs,encoder_Gender,encoder_International,encoder_Marital_status,encoder_Previous_qualification,encoder_Scholarship_holder,encoder_Tuition_fees_up_to_date,encoder_attendance
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('graduation analysis App (Prototype)')
#####

data = pd.DataFrame()
  
col1, col2, col3, col4 = st.columns(4)
  
with col1:
    Application_mode = st.selectbox(label='Application_mode', options=encoder_Application_mode.classes_, index=1)
    data["Application_mode"] = [Application_mode]
  
with col2:
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=1)
    data["Course"] = [Course]
  
with col3:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=1)
    data["Debtor"] = [Debtor]

with col4:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=1)
    data["Displaced"] = [Displaced]
#
col1, col2, col3, col4 = st.columns(4)
  
with col1:
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=1)
    data["Educational_special_needs"] = [Educational_special_needs]
  
with col2:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=1)
    data["Gender"] = [Gender]
  
with col3:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=1)
    data["International"] = [International]

with col4:
    Marital_status = st.selectbox(label='Marital_status', options=encoder_Marital_status.classes_, index=1)
    data["Marital_status"] = [Marital_status]
#
col1, col2, col3, col4 = st.columns(4)
  
with col1:
    Previous_qualification = st.selectbox(label='Previous_qualification', options=encoder_Previous_qualification.classes_, index=1)
    data["Previous_qualification"] = [Previous_qualification]
  
with col2:
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=1)
    data["Scholarship_holder"] = [Scholarship_holder]
  
with col3:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=1)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]

with col4:
    attendance = st.selectbox(label='attendance', options=encoder_attendance.classes_, index=1)
    data["attendance"] = [attendance]

####################################
col1, col2 = st.columns(2)
  
with col1:
        
    Admission_grade = int(st.number_input(label='Admission_grade', value=0))
    data["Admission_grade"] = [Admission_grade]
  
with col2:
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=0))
    data["Age_at_enrollment"] = [Age_at_enrollment]
   
# 
col1, col2, col3 = st.columns(3)
  
with col1:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=0))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]
  
with col2:
    # st.header("Kolom 1")
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', value=0))
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]
  
with col3:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=0))
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]
  
#  
col1, col2, col3 = st.columns(3)
  
with col1:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=0))
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]
  
with col2:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade', value=0))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]
  
with col3:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]
  
#  
col1, col2, col3 = st.columns(3)
  
with col1:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approvedy', value=0))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]
  
with col2:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=0))
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]
  
with col3:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0))
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

#  
col1, col2, col3 = st.columns(3)
  
with col1:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0))
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]
  
with col2:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=0))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]
  
with col3:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]

#  
col1 = st.columns(1)
  

Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=0))
data["Previous_qualification_grade"] = [Previous_qualification_grade]


with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("status prediction: {}".format(prediction(new_data)))