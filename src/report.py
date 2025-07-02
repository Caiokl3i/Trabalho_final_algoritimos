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
        print(f'- {name:<30}. {qtd} evento(s) com esse tema')
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

def average_theme():
    '''
    Exibe a taxa média de participações por temas
    '''
    
    # quantidade de eventos por tema
    themes_count = dict(Counter([events['tema_central'] for events in events_list]))
    
    # total de participantes no evento
    soma_partic = {}
    for theme_name in themes_count.keys():
        for event in events_list:
            if event['tema_central'] == theme_name:
                if theme_name in soma_partic:
                    soma_partic[theme_name] += len(event['participantes_event'])
                else:
                    soma_partic[theme_name]= len(event['participantes_event'])
    
    # faz a media de participação por tema
    media_dict = {}
    for nome, soma in soma_partic.items():
        taxa_media = soma / themes_count[nome]
        media_dict[nome]=taxa_media
    
    print('\n---- MÉDIA DE PARTICIPAÇÃO POR TEMA ----\n')
    for nome, taxa in media_dict.items():
        print(f'{nome:<30} . {taxa}')

def less_than_2_partic():
    '''
    Exibe os eventos com menos de dois participantes (para posssível cancelamento)
    '''
    
    events_qtde = {}
    for event in events_list:
        events_qtde[event['nome']]= len(event['participantes_event'])
    
    print(f'\n---- EVENTOS COM MENOS DE 3 PARTICIPANTES ----')
    print('- Possível cancelamento desses eventos futuramente -\n')
    for chave, valor in events_qtde.items():
        if valor < 3:
            print(f'Evento: {chave :<35} . {valor} participante(s)')
    print()
