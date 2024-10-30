from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def calculate_statistics(series_data):
    series = pd.Series(series_data)
    stats = {
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std_dev": float(series.std()),
        "var": float(series.var()),
        "min": float(series.min()),
        "max": float(series.max()),
    }
    return stats

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    series_data = data.get("series")
    stats = calculate_statistics(series_data)
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)
