from flask import Flask, jsonify
import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftTable

app = Flask(__name__)

@app.route('/')
def home():
    return "Evidently AI in Docker!"

@app.route('/drift')
def drift():
    ref_data = pd.DataFrame({"feature": [1, 2, 3, 4, 5]})
    curr_data = pd.DataFrame({"feature": [1, 2, 6, 7, 8]})
    
    report = Report(metrics=[DataDriftTable()])
    report.run(reference_data=ref_data, current_data=curr_data)
    
    return jsonify(report.as_dict())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

