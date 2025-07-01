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

def more_actives_partic():
    '''
    Exibe os 3 participantes mais ativos em participações nos eventos.
    '''
    
    cpfs = Counter(
        partic['cpf']
        for event in events_list
        for partic in event['participantes_event']
    )

    cpf_para_nome = {partic['cpf']: partic['nome'] for partic in participants_list}
    
    print('\nParticipantes mais ativos:\n')
    for chave, valor in cpfs.most_common(3):
            print(f'{cpf_para_nome[chave] :<20} . participou de {valor} eventos')
