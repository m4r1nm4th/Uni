from flask import Flask, request, jsonify, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

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

@app.route('/plot', methods=['POST'])
def plot():
    data = request.json
    series_data = data.get('series')
    series = pd.Series(series_data)

    fig, ax = plt.subplots()
    series.plot.box(ax = ax)
    plt.title("Box Plot of Series")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return send_file(img,mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
