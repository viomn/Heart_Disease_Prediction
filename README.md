# Heart Disease Prediction App

This project is a *Heart Disease Prediction* application that uses machine learning to predict the likelihood of heart disease based on a set of health parameters.

## Overview

The app takes input data related to a person's health (such as age, blood pressure, cholesterol, etc.) and predicts whether they are at *high risk* of heart disease. The model was trained using a dataset containing multiple attributes, and the prediction is generated based on the data provided by the user.

## Features

- Predict the likelihood of heart disease based on user input.
- Inputs include health parameters like age, blood pressure, cholesterol, and others.
- Displays a simple and aesthetic interface built using *Streamlit*.

## Technologies Used

- *Streamlit*: For building the interactive user interface.
- *Scikit-learn*: For the machine learning model and data preprocessing.
- *Pickle*: For saving and loading the trained model.
- *Pandas, NumPy*: For data manipulation.

## Requirements

- Python 3.6+
- Install the required libraries using:

  bash
  pip install -r requirements.txt
## Setup and Installation

1.  **Clone the Repository**:
    
    bash
    git clone https://github.com/<your-username>/heart-disease-prediction.git
    
    
2.  **Navigate to the Project Directory**:
    
    bash
    cd heart-disease-prediction
    
    
3.  **Install the Dependencies**:
    
    bash
    pip install -r requirements.txt
    
    
4.  **Run the Application**:
    
    bash
    streamlit run app.py
    ```
    
    This will launch the app in your browser.

## How It Works

1.  *Input Data*: The user is prompted to enter health parameters like age, blood pressure, cholesterol levels, etc.
2.  *Prediction: Based on the inputs, the model predicts whether the person is at **high risk* or *low risk* for heart disease.
3.  *Output*: The result is displayed with an explanation of the prediction.

## Example Inputs

Here are some sample inputs you can use to test the application:

*   *Age*: 55
*   *Sex*: Male
*   *Chest Pain Type*: Typical Angina
*   *Resting Blood Pressure*: 140
*   *Serum Cholesterol*: 250
*   *Fasting Blood Sugar*: Yes
*   *Resting Electrocardiographic Results*: Normal
*   *Maximum Heart Rate Achieved*: 150
*   *Exercise Induced Angina*: Yes
*   *Oldpeak (ST Depression)*: 1.2
*   *Slope of Peak Exercise ST Segment*: Upsloping
*   *Number of Major Vessels*: 0
*   *Thalassemia*: Normal

## Conclusion

This application serves as a tool to predict the risk of heart disease based on health data. It uses machine learning models to analyze and generate predictions, which can be helpful for individuals to assess their health.

## Future Enhancements

*   *Add more data*: Use more features or a larger dataset for training.
*   *Improve Model*: Explore other machine learning models for potentially better accuracy.
*   *User Authentication*: Allow users to create accounts and store their predictions.
