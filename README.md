# Cotação de Moedas 

Este é um projeto simples para buscar a cotação de moedas utilizando uma API pública de cotações de moedas. A interface gráfica é construída com PySimpleGUI, e as cotações são obtidas a partir de requisições HTTP usando a biblioteca `requests`.

## Funcionalidades

- **Seleção de Moedas**: O usuário pode selecionar uma moeda de uma lista pré-definida de siglas conhecidas.
- **Consulta de Cotação**: Após selecionar uma moeda, o usuário pode obter a cotação atual dessa moeda em relação ao Real Brasileiro (BRL).
- **Interface Gráfica Simples**: Usamos `PySimpleGUI` para criar uma interface intuitiva e fácil de usar.
- **Tratamento de Erros**: O sistema lida com erros como moedas não encontradas ou problemas de conexão com a API.


### Bibliotecas e tecnologias:

- **![PySimpleGUI](https://img.shields.io/badge/PySimpleGUI-008080?style=for-the-badge&logo=pysimplegui&logoColor=white)** PySimpleGUI
- **![Requests](https://img.shields.io/badge/Requests-0078D7?style=for-the-badge&logo=python&logoColor=white)** Requests
- **![AwesomeAPI](https://img.shields.io/badge/AwesomeAPI-4CAF50?style=for-the-badge&logo=api&logoColor=white)** AwesomeAPI
- **![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)** Python


### Funcionalidades Principais:

1. **`pegar_cotacoes(codigo_moeda)`**:
   - **Descrição**: Função responsável por fazer a requisição da cotação de uma moeda específica utilizando a API pública da AwesomeAPI.
   - **Parâmetros**: `codigo_moeda` (str) – Sigla da moeda (ex: USD, EUR).
   - **Retorno**: Retorna o valor da cotação como um `float`, ou `None` em caso de erro.
   - **Tratamento de Erros**: Caso a API não retorne uma moeda válida ou ocorra algum erro, é exibida uma mensagem de erro no console.

   ```python
   def pegar_cotacoes(codigo_moeda):
       try:
           requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')
           requisicao_dic = requisicao.json()
           cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
           return float(cotacao)
       except:
           print('Código de moeda inválido')
           return None
    ```
