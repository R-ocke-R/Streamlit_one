import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App

This app predicts the Iris Flower type !
         
         """)

# Alerts and Messages
st.success("Some information about the dataset used.")
st.info("""
        The Iris Dataset
This data sets consists of 3 different types of irises’ 
        (Setosa, Versicolour, and Virginica) 
        petal and sepal length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being:
         Sepal Length, Sepal Width, Petal Length and Petal Width.

The below plot uses the first two features. See here for more information on this dataset.

        """)

st.sidebar.header("User Input Paramaters")

# custom function used to accept 4 input paramaters.
def user_input_features():
    sepal_length = st.sidebar.slider('sepal_length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('petal_length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width' : sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features
# it will create a pandas dataframe <3

df = user_input_features()


c1, c2 = st.columns(2)
with c1:
    st.subheader('User Input parameters')
    st.dataframe(df, width = 800)
    st.write("◀⬅You can change the input the parameters from the sidebar widgets ◀⬅")


iris = datasets.load_iris()

X = iris.data
Y = iris.target

# st.write((iris.data[:20]))

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

with c2: 
    st.subheader('Class Labels and Corresponding index number')
    st.dataframe(iris.target_names, width = 400)

st.text("")
st.text("")
# Display the subheader with centered text and rainbow divider
st.markdown("<h3 style='text-align: center;'>Prediction based on Input Parameters</h3>", unsafe_allow_html=True)
st.subheader('', divider='rainbow')

st.text("")
st.text("")


c3, c4 = st.columns(2)

with c3:    
    st.subheader('Prediction')
    st.write(iris.target_names[prediction])
with c4:
    st.subheader('Prediction Probability')
    st.write(prediction_proba)

