import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

class HousePriceModel:
    def __init__(self):
        self.model = self.train_model()

    def train_model(self):
        # Check if model file exists
        model_path = 'house_price_model.pkl'
        if os.path.exists(model_path):
            print("Model already exists. Skipping training.")
            with open(model_path, 'rb') as f:
                return pickle.load(f)
        else:
            print("Training model...")
            # Load dataset
            data = pd.read_csv('data/Housing.csv')
            data.columns = data.columns.str.strip()

            # Manual encoding for categorical variables
            mapping = {
                'yes': 1, 'no': 0,
                'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2
            }

            categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                                   'airconditioning', 'prefarea', 'furnishingstatus']
            for column in categorical_columns:
                data[column] = data[column].str.strip().str.lower().map(mapping)

            # Features and target
            features = ['area', 'bedrooms', 'bathrooms', 'stories', 
                        'mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                        'airconditioning', 'parking', 'prefarea', 'furnishingstatus']
            X = data[features]
            y = data['price']

            # Train/test split
            X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Save model
            with open(model_path, 'wb') as f:
                pickle.dump(model, f)

            return model

    def predict(self, input_data):
        try:
            model = self.model
        except AttributeError:
            # Load the model if it wasn't already loaded
            with open('house_price_model.pkl', 'rb') as f:
                model = pickle.load(f)

        # Prepare input
        input_df = pd.DataFrame([input_data], columns=[ 
            'area', 'bedrooms', 'bathrooms', 'stories', 
            'mainroad', 'guestroom', 'basement', 'hotwaterheating', 
            'airconditioning', 'parking', 'prefarea', 'furnishingstatus'
        ])

        # Manual encoding
        mapping = {
            'yes': 1, 'no': 0,
            'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2
        }
        categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 
                               'airconditioning', 'prefarea', 'furnishingstatus']

        for column in categorical_columns:
            input_df[column] = input_df[column].apply(lambda x: mapping.get(str(x).replace('"', '').strip().lower(), 0))

        # Predict the house price
        prediction = model.predict(input_df)
        return prediction[0]
