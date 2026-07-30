import streamlit as st

def load_example() -> list:
    st.session_state['Age'] = st.number_input("How old are you?", min_value=0, max_value=100, step=1)
    st.session_state['RestingBP'] = st.number_input('What is your resting blood pressure?', min_value=0)
    st.session_state['Cholesterol'] = st.number_input('What is your Cholesterol level?', min_value=0)
    wasFasting = st.selectbox('Is your fasting blood sugar > 120mg/dl?', options =['Yes', 'No'])
    if wasFasting: 
        st.session_state['FastingBS'] = 1
    else:
        st.session_state['FastingBS'] = 0
    
    st.session_state['MaxHR'] = st.number_input('What is your maximum heart rate?', min_value=0)
    st.session_state['Oldpeak'] = st.number_input('What is your Oldpeak?')
    st.write('Oldpeak = ST[Numeric value measured in depression]')

    asy_desc = """
     ASY - Asymptomatic. No chest pain at all, closer to subtle indicators 
     like shortness of breath, unusual fatigue, or mild pressure.
    """
    ata_desc = """
     ATA - Atypical Angina, not textbook. Chest discomfort that has only 2 of the 3 features 
     of typical angina.
    """
    nap_desc = """
        NAP - Non-Anginal Pain Squeezing pain behind the breast bone that may extend to the neck, back, 
        or left arm. A person may also experience other symptoms such as heartburn
        or regurgitation alongside the chest pain. - MedicalNewsToday Article
    """
    ta_desc = """
        TA - Typical Angina. Pressure, squeezing, heaviness in the chest. Triggered by exercise or 
        emotional stress. Relieved by rest. 
        May spread to the left arm, jaw, neck, shoulder, or back. 
    """
    chest_pain_desc = asy_desc + "\n" + ata_desc + "\n" + nap_desc + "\n" + ta_desc
    st.session_state['ChestPainType'] = st.selectbox("What type of chest pain do you have?", options=['ASY', 'ATA', 'NAP', 'TA'])
    st.write(chest_pain_desc)
    st.session_state['RestingECG'] = st.selectbox("What were your resting Electrocardiogram results?", options=['Normal', 'ST', 'LVH'])
    st.write("ST - having ST-T wave abnormality")
    st.write("LVH - showing probable or definite left ventricular hypertrophy by Estes' criteria")
    st.session_state['ST_Slope'] = st.selectbox("What was the slope of the peak exercise ST segment?", options=['Up', 'Flat', 'Down'])
    st.session_state['Sex'] = st.selectbox("Are you a Male or Female?", options=['Male', 'Female'])
    st.session_state['ExerciseAngina'] = st.selectbox('Do you have Exercise-induced Angina?', options=['Yes', 'No'])
    
    fields_required = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS',
    'MaxHR','Oldpeak','ChestPainType','RestingECG','ST_Slope', 'Sex', 'ExerciseAngina'
    ]
    if st.button(label='Submit'):
        returnlist = []
        for field in fields_required:
            returnlist.append(st.session_state[field])
        return returnlist
def make_prediction():
    
st.write("Welcome! I'll try to predict if you have a heart disease!")
st.write("""
Be mindful that this is not professional advice, this was an attempt to
showcase a Machine Learning Model I built a week or two ago.
""")


if "show_questions" not in st.session_state:
    st.session_state["show_questions"] = False
if st.button("Get Started!"):
    st.session_state["show_questions"] = True
if "show_questions" in st.session_state and st.session_state["show_questions"]:
    st.session_state['to_predict'] = load_example()
if st.session_state['to_predict']:
    make_prediction()

