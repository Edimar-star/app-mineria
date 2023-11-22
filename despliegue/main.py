from flask import Flask, request, jsonify
from flask_cors import CORS
from model_score import score_prediction

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/', methods=['GET'])
def home():
    ind_prestamo = request.args.get('ind_prestamo')
    ind_salario = request.args.get('ind_salario')
    ind_formacion = request.args.get('ind_formacion')
    result = score_prediction(ind_prestamo, ind_salario, ind_formacion)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)