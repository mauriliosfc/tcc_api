from flask import Flask
from flask_cors import CORS
from tcc.services.carrega_dados import carrega_dados
from flask import request
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/buscar", methods=['POST'])
def post():
  carregar = carrega_dados('./tcc/G1.xlsx')
  body_unicode = request.data.decode('utf-8')  
  res = json.loads(body_unicode)
  # print(res['body'])
  dic = res['body']
  valor = carregar.buscar_valor(dic)
  return valor

if __name__ == "__main__":
  app.run(port=8080)