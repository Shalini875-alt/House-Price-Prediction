# House-Price-Prediction
# 🏠 House Price Prediction Web App

This is a simple Flask web application that predicts house prices based on user input features like area, number of bedrooms, bathrooms, presence of amenities, and more. The model uses a trained machine learning algorithm to provide price predictions.

## 🚀 Features

- User-friendly form-based interface
- Takes in 12 input parameters (area, bedrooms, bathrooms, etc.)
- Real-time price prediction
- Responsive design with background image
- Flask backend with machine learning model integration

## 📂 Project Structure

```
house-price-prediction/
├── app.py                 # Main Flask backend
├── model.pkl              # Trained ML model
├── templates/
│   └── index.html         # Frontend HTML form
├── static/
│   ├── style.css          # CSS styles
│   └── img.jpg            # Background image
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🧠 ML Model Details

- Algorithm: Linear Regression / Random Forest (customizable)
- Features used:
  - Area (in sqft)
  - Number of bedrooms
  - Number of bathrooms
  - Number of stories
  - Presence of main road, guest room, basement, etc. (binary inputs)
  - Furnishing status (binary input)

## 🛠 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
python app.py
```

5. **Open in browser**
Visit `http://127.0.0.1:5000` in your web browser.

## 📷 Screenshot

![Web Interface](static/img.jpg)  
_A stylish form with a background image and intuitive input fields._

## 📦 Requirements

- Python 3.7+
- Flask
- scikit-learn
- pandas
- joblib or pickle

> All dependencies are listed in `requirements.txt`.

## ✏️ How to Use

1. Fill in the form with house details.
2. Click **Predict**.
3. View the estimated house price instantly below the form.

## 📌 Notes

- Ensure the background image (`img.jpg`) is present in the `static/` directory.
- You can replace `model.pkl` with your own trained regression model.

## 🤝 Contributing

Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

MIT License. See [LICENSE](LICENSE) for more information.

---

> Made with ❤️ for learning and demonstration purposes.