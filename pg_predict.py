import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('file.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_pg_predict():  # sourcery skip
    st.title("Predict Developer's Salary")

    st.write("""### Information needed to predict the salary""")

    education = (
        "Less than a Bachelors",
        "Bachelor's degree",
        "Master's degree",
        "Post graduate"
    )

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden"
    )


    education = st.selectbox("Education Level", education)
    country = st.selectbox("Country", countries)

    experience = st.slider("Experience Range(Years)", 0, 50, 3)

    ok = st.button("Salary Calculation")
    if ok:
        person_info = np.array([[country, education, experience]])
        person_info[:, 0] = le_country.transform(person_info[:, 0])
        person_info[:, 1] = le_education.transform(person_info[:, 1])
        person_info = person_info.astype(float)
        
        salary = regressor.predict(person_info)
        st.subheader(f"Salary Estimated  ${salary[0]:.2f}")