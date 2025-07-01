from collections import Counter
from event_data import events_list
from participant_data import participants_list

def themes_frequency_report():
    '''
    Exibe os temas mais frequentes entre os eventos cadastrados.
    A lista é ordenada do mais frequente para o menos frequente.
    '''
    
    themes_count = Counter([event['tema_central'] for event in events_list])
    
    themes_count = dict(themes_count.most_common())
    
    print('\nFrequência de temas:')
    for name, qtd in themes_count.items():
        print(f'- {name:<30}: {qtd}x')
    print()

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
