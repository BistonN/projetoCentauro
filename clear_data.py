import pandas as pd

def formatarPreco(valor):
    valor = valor.replace('\n', '').split('R$')
    return float(valor[-1].replace(',', '.'))

def formatarParcelamento(parcelamento):
    parcelas = i[3].split('x')[0].split(' ')[-1]
    valor_a_verificar = i[3].split('R$')[-1].replace('\n', '').replace(',', '.')
    valor = ''
    for caractere in valor_a_verificar:
        if caractere.isdigit() or caractere == '.':
            valor += caractere
    return parcelas + ' x ' + valor

def formatarMarca(marca):
    try:
        dados = marca.lower().split('\n')
        return dados[dados.index('marca') + 1]
    except:
        return None

produtos = pd.read_excel('produtos.xlsx').to_numpy()
for i in produtos:
    titulo = i[1]
    preco = formatarPreco(i[2])
    parcelamento = formatarParcelamento(i[3])
    marca = formatarMarca(i[4])
    print(i)