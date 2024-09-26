import requests
import json

# Token de autenticação
access_token = "colocar o token de acesso"

# URL da API v3 para cadastro de produtos
url = "https://api.bling.com.br/v3/produtos"

# Cabeçalhos da requisição
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Dados do produto a serem enviados para a API
produto_data = {
    "produto": {
        "nome": "Produto Simples",
        "codigo": "CODE_001",
        "preco": 1.0,
        "tipo": "P",
        "situacao": "A",
        "formato": "S"
    }
}


def create_product(produto_data):
    response = requests.post(url, headers=headers, data=json.dumps(produto_data))
    return response

def handle_response(response):
    if response.status_code == 200:
        print("Produto cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar o produto:", response.status_code)
        print(response.json())

# Enviar a requisição para a API
response = create_product(produto_data)
handle_response(response)