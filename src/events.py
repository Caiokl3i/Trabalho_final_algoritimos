from InquirerPy import inquirer
from event_data import event_list
from collections import Counter
import utils

def display_event_list():
    '''
    Exibe todos os eventos cadastrados com nome, data e tema central.
    - Se a lista de eventos estiver vazia, exibe uma mensagem de aviso e encerra a função.
    '''
    
    if not event_list:
        print('\nNão há eventos no momento!\n')
        return
    
    print('\n------- LISTA DE EVENTOS -------\n')
    for i, event in enumerate(event_list):
        print()
        print(f'{i + 1} - Evento: {event["nome"]}')

def display_particpants_by_event():
    '''
    Exibe a lista de eventos para que o usuário escolha um,
    e então mostra os participantes do evento escolhido.
    '''
    
    display_event_list()
    
    print()
    
    if not event_list:
        print('\nNão há eventos no momento!\n')
        return
    
    while True:
        try:
            n = int(input(f'Digite o número do evento para ver os participantes (1 a {len(event_list)}) \n'))
            if 1 <= n <= len(event_list):
                break
            else:
                print(f'Digite um número de 1 a {len(event_list)} \n')
                
        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros\n')

    print(f'\n- Os participantes do evento - {event_list[n - 1]["nome"].upper()} - são: \n')
    
    for participant in event_list[n - 1]["participantes_event"]:
        print(f'Nome: {participant["nome"]}')
        print(f'Email: {participant["email"]} \n')

def new_event_register():
    '''
    Cadastra um novo evento na lista de eventos.
    '''
    
    event_themes= [
    "Inteligência Artificial",
    "Desenvolvimento Web",
    "Segurança da Informação",
    "DevOps",
    "Experiência do Usuário (UX/UI)",
    "Desenvolvimento Mobile",
    "Banco de Dados",
    "Ciência de Dados",
    "Computação em Nuvem",
    "Internet das Coisas (IoT)",
    "Robótica",
    "Desenvolvimento de Jogos",
    "Programação para Iniciantes",
    "Empreendedorismo Digital",
    "Inclusão Digital",
    "Ética e Tecnologia",
    "Carreira e Mercado Tech",
    "Tecnologias Emergentes",
    "Automação e RPA",
    "Comunicação e Soft Skills no Mundo Tech"
    ]
    
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
        choices=event_themes
    ).execute()
    print()
    
    event = {
        'nome': name,
        'data': date,
        'tema_central': central_theme
    }
    
    event_list.append(event)
    
    print(f"\nEvento - {name} - cadastrado com sucesso!!\n")

def delete_event():
    '''
    Exclui o evento escolhido da lista de eventos
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    choices = [evento['nome'] for evento in events_list]
    
    
    evento_excluir = inquirer.select(
        message='\nQual evento deseja excluir? \n',
        choices=choices
    ).execute()
    
    for i, evento in enumerate(events_list):
        if evento['nome'] == evento_excluir:
            del events_list[i]
            print(f'\nEvento - {evento_excluir.upper()} - excluído com sucesso!\n')
    print()

def display_events_by_theme():
    '''
    Exibe todos os eventos organizados pelo tema escolhido.
    '''
    
    if not event_list:
        print('\nNão há eventos no momento!\n')
        return
    
    themes_list = sorted({
        theme
        for event in event_list
        for theme in [event['tema_central']]
    })
    
    if not themes_list:
        print('\nNenhum tema disponível\n')
        return
    
    print()
    chosen_theme = inquirer.select(
        message='Qual é o tema para consultar os eventos\n',
        choices=themes_list
    ).execute()
    
    event_name = [
        event['nome'] 
        for event in event_list
        if chosen_theme in event['tema_central']
    ]
    
    print(f'\nEventos sobre - {chosen_theme} - :\n')
    for event in event_name:
        print(f'- {event}')
    print()

def number_events_by_theme():
    '''
    Exibe a quantidade de eventos que cada tema possui
    '''
    
    if not event_list:
        print('\nNão há eventos no momento!\n')
        return
    
    counted_themes = dict(Counter([event['tema_central'] for event in event_list]))
    
    print()
    print('----- QUANTIDADE DE EVENTOS POR TEMA -----\n')
    for theme, quantity in counted_themes.items():
        print(f'{theme} : {quantity} evento(s)')
