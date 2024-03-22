# My GitHub: https://github.com/Thiago-hf
# To get the API key, you need to create an account on OpenAI's website and generate an API key.
# You need do download the OpenAI library to run this code. You can do this by running the command "pip install openai" on your terminal.

import openai

chave_api = "sua_api_key_aqui"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens = []):

    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )

    return resposta["choices"][0]["message"]

lista_mensagens = []

while True: 
    texto = input("Escreva aqui sua mensagem: ")

    if texto == "sair" or texto == "Sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot: ", resposta["content"]) 