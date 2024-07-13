
# biblioteca da openai
import openai

# chave de API da openai
openai.api_key = 'chaveAPI'

# modelo do GPT
MODELO = 'gpt-3.5-turbo'

# mensagem de sistema com instruções personalizadas
def create_system_message(instructions):
    return {
        'role': 'system', #'role': Define o papel da mensagem como 'system'.
        'content': instructions #'content': Contém as instruções ou conteúdo que são passados quando a função é chamada.
    }

# mensagem do usuário
def create_user_message(content):
    return {
        'role': 'user', #'role': Define o papel da mensagem como 'user'.
        'content': content #'content': Contém as instruções ou conteúdo que são passados quando a função é chamada.
    }

# resposta do assistente
def generate_response(messages):
    response = openai.ChatCompletion.create(
        model=MODELO, # modelo usado pra gerar respostas, já foi definido acima
        messages=messages, # A lista de mensagens que será passada para o modelo, no formato esperado pela API, uma lista de dicionários, cada um com chaves como role e content.
        max_tokens=150  # O número máximo de tokens (palavras ou partes de palavras) que a resposta gerada pode ter.
    )
    return response.choices[0].message['content'].strip() # o indice 0 indica que escolhemos a primeira resposta que a API gerou. (ela gera uma lista)

# Função principal do assistente
def main():
    # Define as instruções para o chatgpt
    instructions = "Você é um assistente útil e amigável. Corrija, nos textos enviados, vieses machistas."

    # Cria uma lista de mensagens começando com a mensagem do sistema
    messages = [create_system_message(instructions)]

    print("Ola! Eu sou um assistente. Qual conteudo devo analisar?")

    while True:
        # Recebe uma mensagem do usuário
        user_input = input("Voce: ")
        if user_input.lower() in ['sair', 'exit', 'quit', 'fim' , 'tchau', 'adeus']:
            print("Assistente: Até logo! :)")
            break

        # Adiciona a mensagem do usuário à lista de mensagens
        messages.append(create_user_message(user_input))

        # Gera uma resposta com base nas mensagens
        assistant_response = generate_response(messages)

        # Adiciona a resposta do assistente às mensagens
        messages.append({'role': 'assistant', 'content': assistant_response})

        # Mostra a resposta do assistente
        print(f"Assistente: {assistant_response}")

if __name__ == '__main__':
    main()
