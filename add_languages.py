import requests
from googletrans import Translator

# Define as bandeiras disponíveis e suas URLs
bandeiras = {
    'português': 'https://raw.githubusercontent.com/hampusborgos/country-flags/master/png1000px/br.png',
    'inglês': 'https://raw.githubusercontent.com/hampusborgos/country-flags/master/png1000px/us.png',
    'espanhol': 'https://raw.githubusercontent.com/hampusborgos/country-flags/master/png1000px/es.png'
}

# Pede ao usuário que selecione uma língua
lingua = input('Selecione uma língua (português, inglês, espanhol): ')

# Obtém a URL da bandeira correspondente à língua selecionada
url_bandeira = bandeiras.get(lingua)

# Verifica se a língua selecionada está disponível
if url_bandeira is None:
    print('Língua não disponível')
else:
    # Obtém a imagem da bandeira e salva em um arquivo
    response = requests.get(url_bandeira)
    with open('bandeira.png', 'wb') as file:
        file.write(response.content)
    print('Bandeira salva com sucesso')

    # Traduz o nome da língua selecionada para o inglês
    translator = Translator()
    lingua_ingles = translator.translate(lingua, dest='en').text

    # Exibe o nome da língua selecionada em inglês
    print(f'Você selecionou: {lingua_ingles}')
