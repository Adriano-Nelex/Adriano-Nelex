import requests

# lista de idiomas e suas respectivas siglas
languages = {'Portuguese': 'br', 'English': 'en', 'Spanish': 'es'}

# função para traduzir texto utilizando a API do Google Translate
def translate_text(text, target_language):
    api_url = "https://translate.googleapis.com/translate_a/single"
    params = {'client': 'gtx', 'sl': 'auto', 'tl': target_language, 'dt': 't', 'q': text}
    response = requests.get(api_url, params=params)
    translation = response.json()[0][0][0]
    return translation

# loop para adicionar as bandeiras de idioma no README
for language, code in languages.items():
    flag_url = f"https://raw.githubusercontent.com/hampusborgos/country-flags/master/svg/{code}.svg"
    markdown_code = f"![{language}]({flag_url})\n\n"
    with open('README.md', 'a') as file:
        file.write(markdown_code)

# exemplo de como traduzir o seu perfil para o idioma desejado (no caso, espanhol)
profile_text = "Hello! My name is ChatGPT."
target_language = 'es'
translated_text = translate_text(profile_text, target_language)
print(translated_text)
