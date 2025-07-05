from participant_data import participants_list
from event_data import events_list
from InquirerPy import inquirer
from collections import Counter
import utils

def get_participant_for_cpf():
    '''
    Função auxiliar que busca o participante por cpf
    '''
    
    if not participants_list:
            print('A lista de participantes está vazia')
            return
    
    cpf = utils.cpf_validate()
    
    for participant in participants_list:
        if cpf == participant["cpf"]:
            return participant
        
    return None

def search_participant_for_cpf():
    '''
    Displays participant information by searching with CPF
    '''
    
    participant = get_participant_for_cpf()
    
    if participant is None:
        print(f'O participante não existe!')
        return
    
    print(f'\nInformações do participante: \n')
    print(f' CPF: {participant["cpf"]}')
    print(f' Nome: {participant["nome"]}')
    print(f' Email: {participant["email"]}')
    print(f' Preferências Temáticas: {participant["preferencias_tematicas"]}\n')

def edit_participant_data():
    '''
    Display participant information using CPF and enables editing via an interactive menu.
    '''
    
    participant = search_participant_for_cpf()
    
    if not participant:
        print(f'Participante não encontrado!')
        return None
    
    print('\n----- INSIRA OS NOVOS DADOS DO PARTICIPANTE -----\n')
    
    name = utils.name_validate()
    
    email = utils.validate_email()
    
    themes = set([event['tema_central'] for event in events_list])
    
    thematic_preferences = inquirer.select(
        message='PREFERÊNCIA TEMÁTICA: ',
        choices=themes
    ).execute()
    
    participant['nome'] = name
    participant['email'] = email
    participant['preferencias_tematicas'] = [thematic_preferences]
    
    print()

def detect_duplicate_participants(cpf, event_name):
    '''
    Helper function that checks if the given CPF is already registered for the event.

    Returns:
        True  – if the participant is not yet registered (can be added)
        False – if the participant is already registered (duplicate)
    '''

    for event in events_list:
        if event['nome'] == event_name:
            for participant in event['participantes_event']:
                if cpf == participant['cpf']:
                    return False
    return True

def display_events_by_participant():
    '''
    Displays all events a participant is registered in (based on CPF).
    '''
    
    cpf = utils.email_validate()
    
    events_name_by_partic = [
        (event['nome'], event['data'])
        for event in events_list
        for partic in event['participantes_event']
        if cpf == partic['cpf']
    ]
    
    # uso de tuplas para chave e valor -- mais leve e mais prático -- 
    
    print(f'\n----- EVENTOS DO PARTICIPANTE -----\n')
    for name, data in events_name_by_partic:
        print(f'- {name}\n   Data: {data}\n')

def display_events_each_partic():
    '''
    Exibe a quantidade de eventos em que cada participante esteve presente, 
    ordenando do mais ativo para o menos ativo.
    '''
    # tranformar em list comprehension
    cpfs = []
    for event in events_list:
        for participant in event['participantes_event']:
            cpfs.append(participant["cpf"])
    
    cpf_to_name = {}
    for participant in participants_list:
        cpf_to_name[participant['cpf']] = participant['nome']
    
    cpf_counted = Counter(cpfs)
    
    print('Quantidade de evento de cada participante: \n')
    for key, value in cpf_counted.most_common():
            print(f'{cpf_to_name[key]} - {value} eventos')

def add_participant_in_event():
    '''
    Registers the student identified by CPF for the selected event.
    '''
    
    cpf = utils.cpf_validate()
    
    if not participants_list:
        print('\nA lista de participantes está vazia\n')
        return
    
    if not events_list:
        print('\nA lista de eventos está vazia\n')
        return
    
    events = [event['nome'] for event in events_list]
    event_name = inquirer.select(
        message='\nEscolha o evento para cadastrar o participante:\n',
        choices=events
    ).execute()
    
    if not detect_duplicate_participants(cpf, event_name):
        print('\nEsse aluno já está participando deste evento!\n')
        return
    
    participant = next((partic for partic in participants_list if cpf == partic['cpf']))
    
    for event in events_list:
        if event['nome'] == event_name:
            event['participantes_event'].append(participant)
    
    print(f' - {participant} - cadastrado no evento - {event_name} - com sucesso !')

def register_new_participant():
    '''
    Registers a new participant in the participants' database.
    '''
    
    cpf = utils.cpf_validate()
        
    name = utils.name_validate()
    
    email = utils.email_validate()
    
    while True:
        chosen_theme = inquirer.select(
            message='\nPreferêcia temática:\n',
            choices=utils.event_themes
        ).execute()
        
        tematics_preferences = []
        if not chosen_theme in tematics_preferences:
            tematics_preferences.append(chosen_theme)
        
        option = inquirer.select(
            message='\nQuer escolher mais um tema?',
            choices=['Sim', 'Não']
        ).execute()
        
        if option == 'Sim':
            continue
        elif option == 'Não':
            break
    
    participants_list.append(
        {
        'cpf': cpf,
        'nome': name,
        'email': email,
        'preferencias_tematicas': tematics_preferences
        }
    )
    
    print(f'Participante {name} cadastrado com sucesso')
