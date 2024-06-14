import streamlit as st

st.title('Formulaire')

# Création du formulaire
with st.form('Form2'):

    # Nom
    user_name = st.text_input('Tape your name :')

    # Age
    user_age = st.select_slider("Select your age", 
                                options=range(18, 99)
                                )

    # Niveau d'étude
    user_graduated = st.selectbox("Select your graduation : ",
                                ("BAC", "BAC+2", "BAC+5", "BAC+8"))

    # Bouton envoyer
    if st.form_submit_button('Send'):
        st.write('Form Submited')