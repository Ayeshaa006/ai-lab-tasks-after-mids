from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)
def train_model():
    try:
        data = pd.read_csv('amazon.csv')
        data = data[data['rating'] != '|']
        for col in ['discounted_price', 'actual_price', 'discount_percentage', 'rating_count']:
            data[col] = data[col].astype(str).str.replace('₹', '').str.replace(',', '').str.replace('%', '')
            data[col] = pd.to_numeric(data[col], errors='coerce')
        data = data.dropna()
        X = data[['discounted_price', 'actual_price', 'discount_percentage', 'rating_count']]
        y = pd.factorize(data['rating'].astype(str))[0]
        model = RandomForestClassifier(n_estimators=10) 
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
ml_model = train_model()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if ml_model is None:
        return render_template('index.html', prediction_text="Error: Model not trained.")
    features = [float(x) for x in request.form.values()]
    prediction = ml_model.predict([features])  
    return render_template('index.html', prediction_text=f'Predicted Rating Category: {prediction[0]}')
if __name__ == "__main__":
    app.run(debug=True)
