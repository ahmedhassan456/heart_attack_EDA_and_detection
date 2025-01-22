import pandas as pd

def GetPredictions(model, inputs):

    df = pd.DataFrame([inputs])
    
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Region'] = df['Region'].map({'Urban': 0, 'Rural': 1, 'Suburban': 0.5})
    df['Exercise_Level'] = df['Exercise_Level'].map({'Low': 0, 'High': 1, 'Moderate': 0.5})
    df['Diet'] = df['Diet'].map({'Unhealthy': 0, 'Healthy': 1, 'Mixed': 0.5})
    df['Occupation'] = df['Occupation'].map({'Unemployed': 0, 'Employed': 2, 'Student': 1, 'Retired': 3})
    df['Income_Level'] = df['Income_Level'].map({'Low': 0, 'High': 1, 'Middle': 0.5})
    df['Physical_Activity'] = df['Physical_Activity'].map({'Low': 0, 'High': 1, 'Moderate': 0.5})
    df['Education_Level'] = df['Education_Level'].map({'Primary': 0, 'Higher': 2, 'Secondary': 1})
    df['Marital_Status'] = df['Marital_Status'].map({'Single': 0, 'Married': 1, 'Divorced': 2, 'Widowed': 3})
    df['Smoking'] = df['Smoking'].map({'True': 1, 'False': 0})
    df['Diabetes'] = df['Diabetes'].map({'True': 1, 'False': 0})
    df['Family_History'] = df['Family_History'].map({'True': 1, 'False': 0})
    df['Angina'] = df['Angina'].map({'True': 1, 'False': 0})
    df['Heart_Disease_History'] = df['Heart_Disease_History'].map({'True': 1, 'False': 0})
    df['Medication'] = df['Medication'].map({'True': 1, 'False': 0})
    df['Obesity'] = df['Obesity'].map({'True': 1, 'False': 0})


    prediction = model.predict([df.to_numpy()[0]])[0]

    return prediction