from collections import Counter
from event_data import events_list

'''
    Funcionalidade ainda em desenvolvimento.
Counter - para contar quantos eventos tem.
dict - para tranformar o que o Counter retorna para um dicionario.
.item() - para retornar chave e valor para serem usados na parte visivel.
    Iniciando uso de list comprehension
'''

def report_frequency():
    temas = [tema['tema_central'] for tema in events_list]

    contagem = dict(Counter(temas))

    print('Quantidade de eventos por tema: \n')
    for nome, qtde in contagem.items():
        print(f'{nome} - {qtde} eventos')

report_frequency()