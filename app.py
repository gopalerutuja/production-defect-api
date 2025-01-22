from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import os
import joblib

app = Flask(__name__)

# Global variables to store dataset and model
data = None
model = None

# Endpoint: Upload Dataset
@app.route('/upload', methods=['POST'])
def upload_dataset():
    global data
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        data = pd.read_csv(file)
        return jsonify({'message': 'File uploaded successfully', 'columns': data.columns.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint: Train Model
@app.route('/train', methods=['POST'])
def train_model():
    global data, model
    if data is None:
        return jsonify({'error': 'No dataset uploaded. Please upload a dataset first.'}), 400

    try:
        # Extract features and target
        features = request.json.get('features')
        target = request.json.get('target')

        if not features or not target:
            return jsonify({'error': 'Features and target must be specified.'}), 400

        X = data[features]
        y = data[target]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a model (Logistic Regression as default)
        model_type = request.json.get('model', 'logistic_regression')
        if model_type == 'logistic_regression':
            model = LogisticRegression()
        elif model_type == 'decision_tree':
            model = DecisionTreeClassifier()
        else:
            return jsonify({'error': 'Unsupported model type.'}), 400

        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')

        # Save the trained model
        joblib.dump(model, 'model.pkl')

        return jsonify({'message': 'Model trained successfully', 'accuracy': accuracy, 'f1_score': f1}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint: Predict
@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({'error': 'Model not trained. Please train a model first.'}), 400

    try:
        input_data = request.json.get('data')
        if not input_data:
            return jsonify({'error': 'No input data provided.'}), 400

        input_df = pd.DataFrame(input_data)
        predictions = model.predict(input_df)

        return jsonify({'predictions (1 = defective/0 = not defective)': predictions.tolist()}), 200


    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

