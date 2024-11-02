from controllor.LoadModel import LoadModel
from controllor.GetPredection import GetPredection
import streamlit as st


st.title('Iris Flower Prediction App')
st.write('Enter the characteristics of the iris flowers')

SepalLength = st.number_input('SepalLengthCm', min_value=0.0, max_value=10.0, step=0.1)
SepalWidth = st.number_input('SepalWidthCm', min_value=0.0, max_value=10.0, step=0.1)
PetalLength = st.number_input('PetalLengthCm', min_value=0.0, max_value=10.0, step=0.1)
PetalWidth = st.number_input('PetalWidthCm', min_value=0.0, max_value=10.0, step=0.1)



model = LoadModel('model/iris_model.pkl')

if st.button('predict'):
    predection =GetPredection(model, [SepalLength, SepalWidth, PetalLength, PetalWidth])
    st.write(f'this prediction class of the iris flower is : {predection}')