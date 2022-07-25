#Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

#Title of the web app
st.title("Iris Dataset Flower Classifier/Predictor")
df = pd.read_csv('/Users/aravind/Desktop/CS:DS Projects/ml_web_app/iris.csv')
#Enables to the user to check or uncheck a box that shows the data
if st.checkbox('Show dataset below'):
    st.write(df)
st.subheader('Scatter plot')

#Enables the user to view the features they desire to use to make the model
species_set = st.multiselect('Showing iris per variety', df['variety'].unique())
column_1 = st.selectbox('Feature on x', df.columns[0:4])
column_2 = st.selectbox('Feature on y', df.columns[0:4])

#Dataframe with features used to create a scatter plot to show the different data points in the data set
new_df_for_features = df[(df['variety'].isin(species_set))]
st.write(new_df_for_features)
figure_1 = px.scatter(new_df_for_features, x=column_1, y=column_2, color='variety')
st.plotly_chart(figure_1)
st.subheader("Histogram")

#Drop-down created to select features to put on columns to classify the data
feature_selector = st.selectbox('Which feature?', df.columns[0:4])
new_filtered_df = df[(df['variety'].isin(species_set))][feature_selector]

#Histogram created to show the distribution of the dataset
figure_2 = px.histogram(new_df_for_features, x=feature_selector, color='variety', marginal='rug')
st.plotly_chart(figure_2)

#Machine Learning Models to classify the whole dataset based on training and validation data and according to the split given below
st.subheader('Machine Learning models')
features_of_the_flower = df[['sepal.length', 'sepal.length', 'petal.length', 'petal.width']].values
histogram_labels = df['variety'].values

#Splits the data into training and validation data to check the model's accuracy
X_train, X_test, y_train, y_test = train_test_split(features_of_the_flower, histogram_labels, train_size=0.7, random_state=1)

#Algorithms used to see the accuracy of classification
algorithm = ['Decision Tree', 'Support Vector Machine']

#Dropdown to select which algorithm the user would like to use to classify the flowers into their categories correctly
required_classifier = st.selectbox('What algorithm would you like to use?', algorithm)

#Determines accuracy of the Decision Tree model if the user selects it
if required_classifier == 'Decision Tree':
    decision_tree_algorithmic_classifier = DecisionTreeClassifier()
    decision_tree_algorithmic_classifier.fit(X_train, y_train)
    algorithm_accuracy = decision_tree_algorithmic_classifier.score(X_test, y_test)
    st.write('Accuracy of the model: ', str(100 * algorithm_accuracy) + "%")
    prediction_decision_tree_algorithm = decision_tree_algorithmic_classifier.predict(X_test)
    confusion_matrix_creator = confusion_matrix(y_test, prediction_decision_tree_algorithm)
    st.write('Confusion matrix shown below: ', confusion_matrix_creator)

#Determines accuracy of the Support Vector Machine model if the user selects it
elif required_classifier == 'Support Vector Machine':
    support_vector_machine = SVC(kernel='linear')
    support_vector_machine.fit(X_train, y_train)
    algorithm_accuracy = SVC.score(X_test, y_test)
    true_algorithm_accuracy = 100 * algorithm_accuracy
    st.write('Accuracy of the model:  ', str(round(true_algorithm_accuracy, 2)))
    prediction_SVM = SVC.predict(X_test)
    confusion_matrix_creator = confusion_matrix(y_test, prediction_SVM)
    st.write('Confusion matrix shown below: ', confusion_matrix_creator)
