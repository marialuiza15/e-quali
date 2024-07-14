
# biblioteca da openai
import openai

# chave de API da openai
openai.api_key = 'chave'

# modelo do GPT
modelo = 'gpt-3.5-turbo'

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
        model=modelo, # modelo usado pra gerar respostas, já foi definido acima
        messages=messages, # A lista de mensagens que será passada para o modelo, no formato esperado pela API, uma lista de dicionários, cada um com chaves como role e content.
        max_tokens=500  # O número máximo de tokens (palavras ou partes de palavras) que a resposta gerada pode ter.
    )
    return response.choices[0].message['content'].strip() # o indice 0 indica que escolhemos a primeira resposta que a API gerou. (ela gera uma lista)

# Função principal do assistente
def main():
    # Define as instruções para o chatgpt
    instructions = '''

    Ao sugerir mudanças na descrição da vaga lembre-se de respeitar o estilo próprio da marca e o tom de voz original, ao mesmo tempo que torna a linguagem mais inclusiva para mulheres e adapta a descrição de requisitos e destaques sobre flexibilidade e progressão de carreira dentro das estratégias de 1 a 5.

    Demonstrar que a vaga tem atributos de flexibilidade e incentivo ao Desenvolvimento Contínuo
    Foco nos Requisitos Indispensáveis para evitar a eliminação de mulheres
    Valorização de Habilidades Interpessoais, de Gestão e de Organização
    Evitar Palavras sem Ambiguidade de Gênero - Exemplo: Substitua Diretor por Diretor(a)
    Destacar Benefícios e Políticas de Inclusão, apenas se for informado - Exemplo: Plano de saúde, Licença maternidade e políticas de promoção de lideranças diversas que a empresa já possui.
    
    Evitar o uso do termo "avançado"
    Não usar informações que o usuario não te deu.
    Em um paragrafo diferente, citar os aspéctos que foram corrigidoe e porque eles distanciam as mulheres da vaga. Nesse trecho, por favor, use substantivos femininos.

    Quando a vaga tiver muitós tópicos, organizar em formato de listagem, um tópico por linha. Para Melhorar a visualização da informação
  

    '''

    # Cria uma lista de mensagens começando com a mensagem do sistema
    messages = [create_system_message(instructions)]

    # Dialogos de exemplo para o treinamento
    examples = [
        {"role": "user", "content": "A equipe da AB InBev Analytics está procurando um cientista de dados motivado e analítico que queira fazer parte de um ambiente de estilo de startup."},
        {"role": "assistant", "content": "Estamos em busca de um(a) Cientista de Dados motivado(a) e analítico(a) para integrar nossa equipe de Analytics na AB InBev. Valorizamos a flexibilidade de horário e o desenvolvimento contínuo de carreira, oferecendo um ambiente dinâmico e inovador, voltado para o crescimento profissional e o equilíbrio entre vida pessoal e profissional. \n\nAspectos que foram corrigidos e por que foram corrigidos: Foco em um ambiente de estilo de startup pode ser percebido como desafiador para quem procura equilíbrio entre vida profissional e pessoal."},
        {"role": "user", "content": "Você trabalhará na interseção de aplicação de soluções de aprendizado de máquina/aprendizado profundo, insights acionáveis a partir de grandes conjuntos de dados diversos e usar práticas recomendadas de DevOps."},
        {"role": "assistant", "content": "Você fará parte da equipe de Gerenciamento de Categorias da AB InBev, responsável por construir soluções competitivas diferenciadas para melhorar a lucratividade, receita ou economizar custos em nossas capacidades de vendas (otimização de sortimento, preços e promoções, espaço de prateleira, e-commerce, entre outros). Como Cientista de Dados, você aplicará soluções de aprendizado de máquina/aprendizado profundo e gerará insights acionáveis a partir de grandes conjuntos de dados. Utilizando práticas recomendadas de DevOps, você desenvolverá novos recursos de produtos do início ao fim e colaborará com equipes de engenharia para influenciar projetos e arquiteturas. \n\nAspectos que foram corrigidos e por que foram corrigidos: Descrição técnica pode intimidar candidatos que não se sentem completamente qualificados, especialmente mulheres que tendem a se subestimar."},
        {"role": "user", "content": "Bacharelado ou Mestrado em Engenharia, Estatística ou Economia; Experiência no mundo real na construção de modelos de Machine Learning; Forte experiência em codificação Python; Boa base em modelos de ML supervisionados e não supervisionados; Exposição ao trabalho em IDEs como VSC ou PyCharm; Experiência em versionamento de código usando Git (ou similar), mantendo base de código modularizada para múltiplas implantações; Experiência em trabalhar em ambiente ágil; Conhecimento básico de design orientado a objetos e conceitos; Esperamos que você desafie o status quo com a mentalidade de dono sobre o que pode quebrar e pense em consertar proativamente; Solução das necessidades de negócios; Inglês e Espanhol avançado (obrigatório); Mão na massa com experiência comprovada na construção e fornecimento de soluções analíticas; Experiente no fornecimento de modelos complexos de ML; Experiente na entrega de projetos com impacto na cadeia de valor; Boa capacidade de comunicação e negociação; Executa com disciplina, colaboração, motivação, capacidade de construir relacionamentos fortes e trabalhar de forma transversal com stakeholders internos e externos, liderando pelo exemplo; A abordagem de solução de problemas deve ser capaz de identificar sistematicamente a causa raiz e definir planos de ação; Capaz de trabalhar como agente de mudança construindo MVPs e PoCs e propondo novas abordagens para manter nossa estratégia de análise sempre na vanguarda tecnológica; Experiência com frameworks ágeis, entendimento de SDLC."},
        {"role": "assistant", "content": "\n- Formação em Engenharia, Estatística, Economia ou áreas correlatas. \n- Experiência prática na construção de modelos de Machine Learning. \n- Conhecimento em codificação Python. \n- Experiência em versionamento de código usando Git ou similar. \n- Capacidade de trabalhar em ambiente ágil. \n- Inglês e Espanhol avançado. \n\nAspectos que foram corrigidos e por que foram corrigidos: Lista extensa e técnica de requisitos pode desencorajar mulheres que não se sentem 100% qualificadas, levando a autoeliminação do processo seletivo."},
        {"role": "user", "content": "Vale refeição ou alimentação ifood; Vale transporte; Bônus; Plano de saúde e Telemedicina; Convênio odontológico; Convênio Farmácia; Self Learning (auxílio em cursos, certificações e idiomas); Seguro de vida; Instituto Ambev de Previdência Privada; Auxílio Material Escolar; Cesta de Natal e Kit Congelado; Brinquedos de Natal; Empresa cidadã (licença maternidade e paternidade) e presente do bebê; Desconto mensal em produtos AMBEV; Banco de horas; Gympass; Fretado; Abono anual referente a um salário."},
        {"role": "assistant", "content": "Na AB InBev, valorizamos o bem-estar e o desenvolvimento de nossos colaboradores. Oferecemos uma ampla gama de benefícios e políticas de inclusão, incluindo: \n- Vale refeição ou alimentação iFood \n- Vale transporte \n- Bônus \n- Plano de saúde e Telemedicina \n- Convênio odontológico e farmácia \n- Auxílio para cursos, certificações e idiomas \n- Seguro de vida \n- Instituto Ambev de Previdência Privada \n- Auxílio material escolar \n- Cesta de Natal e Kit Congelado \n- Brinquedos de Natal \n- Empresa cidadã (licença maternidade e paternidade) e presente do bebê \n- Desconto mensal em produtos AMBEV \n- Banco de horas \n- Gympass \n- Fretado \n- Abono anual referente a um salário. \n\nAspectos que foram corrigidos e por que foram corrigidos: Benefícios são um ponto positivo, mas a apresentação poderia ser melhor destacada para enfatizar a preocupação com bem-estar e inclusão."},
        {"role": "user", "content": "A Webmotors não destacou benefícios específicos na descrição original."},
        {"role": "assistant", "content": "Na Webmotors, respeito e inclusão fazem parte dos nossos itens de série. Oferecemos um ambiente de trabalho acolhedor e incentivamos candidaturas de pessoas #pretas, #mulheres, #PCD, #LGBTQIA+ e #melhoridade. Entre os benefícios oferecidos, destacamos: - Ambiente de trabalho flexível. - Incentivos para desenvolvimento profissional contínuo. - Políticas de inclusão e diversidade. - Benefícios alinhados ao bem-estar dos colaboradores. - Oportunidade de trabalhar em uma empresa inovadora e líder de mercado. \n\nAspectos que foram corrigidos e por que foram corrigidos: A falta de destaque para benefícios e políticas de inclusão pode fazer com que as candidatas não percebam a empresa como um lugar acolhedor e inclusivo."}
        
    ]

    messages.extend(examples)

    print("Por favor, forneça a descrição da vaga que gostaria de adaptar, e farei as alterações necessárias para torná-la mais atrativa para mulheres. Farei isso utilizando o formato e as estratégias especialmente desenvolvidas pela e-quali a partir de estudos sobre a relação entre mulheres diversas e o mercado de trabalho.")

    while True:
        # Recebe uma mensagem do usuário
        user_input = input("\nVoce:")
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
        print(f"\nAssistente: {assistant_response}")

if __name__ == '__main__':
    main()
