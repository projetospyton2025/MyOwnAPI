from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoint para buscar o resultado mais recente da Mega-Sena
@app.route('/api/megasena', methods=['GET'])
def get_megasena_latest():
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/"
    
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": "Não foi possível buscar os resultados", "detalhes": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
