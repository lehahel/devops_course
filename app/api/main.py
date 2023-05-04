from flask import request, Response, Flask
import requests
import json

api_key = 'dict.1.1.20230428T191625Z.e0b02868aa9915c5.2abf165db1b56f36fa716bf9ff7eb984917cceaf'

app = Flask("TranslatorApp")

@app.route('/api/translation/get', methods=['GET'])
def process_translation():
    word = request.args.get('word')
    json_response = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={api_key}&lang=en-ru&text={word}").json()
    translation = json_response['def'][0]['tr'][0]['text']
    print(translation)
    result = {'text': translation}
    return Response(json.dumps(result, ensure_ascii=False).encode('utf8'), status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)