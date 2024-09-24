import PySimpleGUI as sg
import requests
#istale antes as bibliotecas

def pegar_cotacoes(codigo_moeda):#função para requisitar a cotação
    try:
        #o metodo get retorna a cotação de acordo com moeda pesquisada
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL')#estamos consumindo de uma API gratuita
        requisicao_dic = requisicao.json()#requisição foi convertido com o metodo json antes de ser manipulado
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']# cotação foi convertida numa string formatada com o codigo e o valor e real
        return float(cotacao)
    except:
        print('codigo de moeda invalido')
        return None


#Inicio dos atributos da janela
sigla_moeda=["","BTC-BitCoin","USD-Dolar","EUR-Euro","CAD-DolarCanadense","JPY-IeneJapones"]#uma lista de abreviações de moedas conhecidas
pagina=[
    [sg.P(),sg.Text("PEGAR COTAÇÂO DA MOEDA", font=('Ariel',15)),sg.P()],
    [sg.T("Cotação de:")],
    [sg.DD(default_value="",values=sigla_moeda,key='nome_cotação',size=(40,1))],
    [sg.Button("Pegar Cotação",size=(15,1)),sg.P(), sg.Button("Sair",size=(15,1),button_color='red')],
    [sg.Text("",key='text_cotacao')]
]

janela = sg.Window("COTAÇÃO DE MOEDA DO DIA",pagina)
while True:
    try: 
        acao, valores= janela.read()
        if acao == sg. WIN_CLOSED or acao =="Sair":
            break

        if acao == "Pegar Cotação":
            codigo_cotacao = valores['nome_cotação'][:3].upper() #estou pegando apenas as primeira tres letra e convertendo pa maiusculas
            cotacao = pegar_cotacoes(codigo_cotacao)
            cotacao_formatada = f'{cotacao:,.2f}'.replace(',', '.')# estou delimitando com pontos os centavos e unidades de milhar
            janela['text_cotacao']. update(f'A Cotação do {codigo_cotacao} no dia de hoje é R$ {cotacao_formatada}')
    except:
        janela['text_cotacao'].update('Moeda Não Localizada')#os possiveis erros serão tratados de forma generica para nao quebra o sistema

janela.close()