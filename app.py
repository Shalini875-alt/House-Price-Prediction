from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('house_price_model.pkl', 'rb'))  # Change path as per your model location

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        mainroad = int(request.form['mainroad'])  # assuming 1 for 'yes' and 0 for 'no'
        guestroom = int(request.form['guestroom'])
        basement = int(request.form['basement'])
        hotwaterheating = int(request.form['hotwaterheating'])
        airconditioning = int(request.form['airconditioning'])
        parking = int(request.form['parking'])
        prefarea = int(request.form['prefarea'])
        furnishingstatus = int(request.form['furnishingstatus'])  # assuming categorical encoded value

        # Prepare input data as DataFrame
        input_data = pd.DataFrame([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, 
                                    hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]],
                                  columns=[
                                      'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
                                      'basement', 'hotwaterheating', 'airconditioning', 'parking', 
                                      'prefarea', 'furnishingstatus'
                                  ])

        # Predict the house price
        prediction = model.predict(input_data)
        predicted_price = prediction[0]

        return render_template('index.html', prediction_text=f'Predicted House Price: ${predicted_price:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
