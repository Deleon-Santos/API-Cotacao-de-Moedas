import PySimpleGUI as sg
import requests


def pegar_cotacoes(codigo_cotacao):
    try:
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_cotacao}-BRL')
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_cotacao}BRL']['bid']
        print(cotacao)
        return cotacao
        
    except:
        print('codigo de moeda invalido')
        return None


#todos os comandos isados depois de "sg" começam com letra maiuscula
pagina=[
    [sg.Text("Pegar Cotação da Moeda")],#texto da janela
    [sg.InputText(key='nome_cotação')],# input de entrada de texto com o valor armazenado na chave "cota"
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],#criação dos dois botoes
    [sg.Text("",key='text_cotacao')]#nesse caompodeve entra a chave key e um texto de cotação
]#coluna com 3 lista de comendo representados em lista dentro de lista

janela = sg.Window("COTAÇÃO DE MOEDA DO DIA",pagina)#a janela recebe uma window(leyout) com lista da 'pagina'
while True: #comçam as acoes e o requerimento de valores que serão trtados na janela
    acao, valores= janela.read()#faz a leitura da tela
    if acao == sg. WIN_CLOSED or acao =="Cancelar":#tocando no "x" encerra o programa
        break

    if acao == "Pegar Cotação":
        codigo_cotacao = valores['nome_cotação']#na variavel codigo de cotação pegamos o valor da cotação
        cota = pegar_cotacoes(codigo_cotacao)
        janela['text_cotacao']. update(f'A Cotação do {codigo_cotacao} no dia de hoje é R$ {cota}')
janela.close()