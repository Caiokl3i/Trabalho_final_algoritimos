from collections import Counter
from event_data import events_list
from participant_data import participants_list

def themes_frequency_report():
    '''
    Exibe os temas mais frequentes entre os eventos cadastrados.
    A lista é ordenada do mais frequente para o menos frequente.
    '''
    
    counted_themes = Counter([event['tema_central'] for event in events_list])
    
    counted_themes = dict(counted_themes.most_common())
    
    print('\nFrequência de temas:\n')
    for name, quantity in counted_themes.items():
        print(f'- {name:<30}. {quantity} evento(s) com esse tema')
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

    cpf_to_nome = {partic['cpf']: partic['nome'] for partic in participants_list}
    
    print('\nParticipantes mais ativos:\n')
    for key, value in cpfs.most_common(3):
            print(f'{cpf_to_nome[key] :<20} . participou de {value} eventos')

def average_theme():
    '''
    Exibe a taxa média de participações por temas
    '''
    
    # quantidade de eventos por tema
    counted_themes = dict(Counter([event['tema_central'] for event in events_list]))
    
    # total de participantes no evento
    partic_sum = {}
    for theme_name in counted_themes.keys():
        for event in events_list:
            if event['tema_central'] == theme_name:
                if theme_name in partic_sum:
                    partic_sum[theme_name] += len(event['participantes_event'])
                else:
                    partic_sum[theme_name]= len(event['participantes_event'])
    
    # faz a media de participação por tema
    dict_average = {}
    for name, sum in partic_sum.items():
        average_rate = sum / counted_themes[name]
        dict_average[name]=average_rate
    
    print('\n---- MÉDIA DE PARTICIPAÇÃO POR TEMA ----\n')
    for name, rate in dict_average.items():
        print(f'{name:<30} . {rate}')

def less_than_2_partic():
    '''
    Exibe os eventos com menos de dois participantes (para posssível cancelamento)
    '''
    
    events_quantity = {}
    for event in events_list:
        events_quantity[event['nome']]= len(event['participantes_event'])
    
    print(f'\n---- EVENTOS COM MENOS DE 3 PARTICIPANTES ----')
    print('- Possível cancelamento desses eventos futuramente -\n')
    for key, value in events_quantity.items():
        if value < 3:
            print(f'Evento: {key :<35} . {value} participante(s)')
    print()
