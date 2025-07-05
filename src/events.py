from InquirerPy import inquirer
from event_data import events_list
from collections import Counter
import utils

def display_event_list():
    '''
    Displays all registered events with name, date, and main theme.
    - If the event list is empty, shows a warning message and exits the function.
    '''
    
    utils.clear_screen()
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    print('\n------- LISTA DE EVENTOS -------\n')
    for i, event in enumerate(events_list):
        print()
        print(f'{i + 1} - Evento: {event["nome"]}')

def display_participants_by_event():
    '''
    Displays a list of events for user selection, 
    then shows the participants of the selected event.
    '''
    
    display_event_list()
    
    print()
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    while True:
        try:
            n = int(input(f'Digite o número do evento para ver os participantes (1 a {len(events_list)}) \n'))
            if 1 <= n <= len(events_list):
                break
            else:
                print(f'Digite um número de 1 a {len(events_list)} \n')
                
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros\n')
    
    if not events_list[n - 1]["participantes_event"]:
        print('\n - Não há participantes no evento - \n')
        return
    
    print(f'\n- Os participantes do evento - {events_list[n - 1]["nome"].upper()} - são: \n')
    for participant in events_list[n - 1]["participantes_event"]:
        print(f'Nome: {participant["nome"]}')
        print(f'Email: {participant["email"]} \n')

def new_event_register():
    '''
    Adds a new event to the list of events.
    '''
    
    print(f'\n===== CADASTRO DE UM NOVO EVENTO =====\n')
    name = inquirer.text(
        message='NOME: ',
        validate=lambda result: len(result) > 0 or "É obrigatorio preencher esse campo"
    ).execute()
    print()
    
    while True:
        date = inquirer.text(
            message='DATA DD/MM/AAAA: '
        ).execute()
        
        if not utils.validar_data(date):
            print('Formato inválido! (Ex. 12/03/2025)')
        else:
            break
    print()
    
    central_theme = inquirer.select(
        message='TEMA: ',
        choices=utils.event_themes
    ).execute()
    print()
    
    events_list.append(
        {
        'nome': name,
        'data': date,
        'tema_central': central_theme,
        'participantes_event': []
        }
    )
    
    print(f"\nEvento - {name} - cadastrado com sucesso!!\n")

def delete_event():
    '''
    Removes the selected event from the event list
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    choices = [evento['nome'] for evento in events_list]
    
    utils.clear_screen()
    
    evento_excluir = inquirer.select(
        message='\nQual evento deseja excluir? \n',
        choices=choices
    ).execute()
    
    for i, evento in enumerate(events_list):
        if evento['nome'] == evento_excluir:
            del events_list[i]
            print(f'\nEvento - {evento_excluir.upper()} - excluído com sucesso!\n')

def display_events_by_theme():
    '''
    Displays all events organized by the selected theme.
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    themes_list = sorted({
        theme
        for event in events_list
        for theme in [event['tema_central']]
    })
    
    if not themes_list:
        print('\nNenhum tema disponível\n')
        return
    
    utils.clear_screen()
    print()
    chosen_theme = inquirer.select(
        message='Qual é o tema para consultar os eventos\n',
        choices=themes_list
    ).execute()
    
    event_name = [
        event['nome'] 
        for event in events_list
        if chosen_theme in event['tema_central']
    ]
    
    print(f'\nEventos sobre - {chosen_theme} - :\n')
    for event in event_name:
        print(f'- {event}')
    print()

def number_events_by_theme():
    '''
    Displays the number of events for each theme
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    counted_themes = dict(Counter([event['tema_central'] for event in events_list]))
    
    utils.clear_screen()
    
    print()
    print('----- QUANTIDADE DE EVENTOS POR TEMA -----\n')
    for theme, quantity in counted_themes.items():
        print(f'{theme :<30} : {quantity} evento(s)')
