from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/data', methods=['GET'])
def get_data():
       return jsonify(data)

    
@app.route('/search', methods=['GET'])
def search_data():
    # If a condition query parameter is provided, filter data by condition
    condition = request.args.get('condition')
    if condition:
        condition = condition.lower()
        # Split the search condition into individual words
        search_terms = condition.split()
        # Filter data based on partial matches with any word in the condition
        filtered_data = [{'condition': entry['condition'], 'medication_and_care': entry['medication_and_care']} for entry in data if any(term in entry['condition'].lower() for term in search_terms)]
        return jsonify(filtered_data)
    else:
        return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
