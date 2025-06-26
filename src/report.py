from collections import Counter
from event_data import events_list
from participant_data import participants_list

def frequency_report():
    '''
    - Funcionalidade ainda em desenvolvimento.
    Counter - para contar quantos eventos tem.
    dict - para tranformar o que o Counter retorna para um dicionario.
    .item() - para retornar chave e valor para serem usados na parte visivel.
    - Iniciando uso de list comprehension
    '''
    
    temas = [tema['tema_central'] for tema in events_list]

    contagem = dict(Counter(temas))
    print(contagem)

    print('Quantidade de eventos por tema: \n')
    for nome, qtde in contagem.items():
        print(f'{nome} - {qtde} eventos')

def active_participants_report():
    '''
    - Funcionalidade ainda em desenvolvimento.
    Adiciona CPFs em uma lista de cpfs
    RElaciona o CPF com o nome
    Counter conta quantas vezes o cpf repetiu
    '''
    
    cpfs = []
    for evento in events_list:
        for participante in evento['participantes_event']:
            cpfs.append(participante["cpf"])
    
    cpf_para_nome = {}
    for participante in participants_list:
        cpf_para_nome[participante['cpf']] = participante['nome']
    
    count = Counter(cpfs)
    
    print('Quantidade de evento de cada participante: \n')
    for chave, valor in count.most_common():
            print(f'{cpf_para_nome[chave]} - {valor} eventos')
