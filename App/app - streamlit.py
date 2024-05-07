import streamlit as st

from io import BytesIO

from emlParser import emailParser

import pickle
model_path = r'../Models/model.sav'


class ModelPredictor:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)

    def predict(self, email):
        return self.model.predict([email])[0]

model_predictor = ModelPredictor(model_path)

def main():
    st.title("Spam Detection App")
    uploaded_file = st.file_uploader("Select an email file for spam detection", type=['eml'])
    spam_text = st.text_area("Paste email contents here")

    prediction = None

    if uploaded_file is not None:
        file_content = uploaded_file.read()

        stream = BytesIO(file_content)

        email = emailParser(stream)

        prediction = model_predictor.predict(email)

    elif spam_text:
        prediction = model_predictor.predict(spam_text)

    if prediction is not None:
        if prediction == 1:
            st.write("This email is predicted to be Spam.")
        else:
            st.write("This email is predicted to be NOT Spam.")
        

if __name__ == '__main__':
    main()
