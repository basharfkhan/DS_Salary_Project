import flask
from flask import Flask, request, jsonify
import json
from data_input import data_in
import numpy as np
import pandas as pd
import pickle


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
        columns = data['columns']
    return model,columns

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        request_json = request.get_json(force=True)
        x = request_json['input']
        model, columns = load_models()
        full_input = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)
        full_input.iloc[0, :len(x)] = x
        prediction = model.predict(full_input)[0]
        response = {'response': float(prediction)}
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    application.run(debug=True)