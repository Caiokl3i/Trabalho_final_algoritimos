from InquirerPy import inquirer
from event_data import events_list
from collections import Counter
import utils

def show_event_list():
    '''
    Exibe todos os eventos cadastrados com nome, data e tema central.
    - Se a lista de eventos estiver vazia, exibe uma mensagem de aviso e encerra a função.
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    print('\n------- LISTA DE EVENTOS -------\n')
    for i, item in enumerate(events_list):
        print()
        print(f'{i + 1} - Evento: {item["nome"]}')

def show_participants_by_event():
    '''
    Exibe a lista de eventos para que o usuário escolha um,
    e então mostra os participantes do evento escolhido.
    '''
    
    show_event_list()
    
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

    print(f'\n- Os participantes do evento - {events_list[n - 1]["nome"].upper()} - são: \n')
    
    for participant in events_list[n - 1]["participantes_event"]:
        print(f'Nome: {participant["nome"]}')
        print(f'Email: {participant["email"]} \n')

def new_event_register():
    '''
    Cadastra um novo evento na lista de eventos.
    '''
    
    temas_eventos = [
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
    nome = inquirer.text(
        message='NOME: ',
        validate=lambda result: len(result) > 0 or "É obrigatorio preencher esse campo"
    ).execute()
    print()
    
    while True:
        data = inquirer.text(
            message='DATA DD/MM/AAAA: '
        ).execute()
        
        if not utils.validar_data(data):
            print('Formato inválido! (Ex. 12/03/2025)')
        else:
            break
    print()
    
    tema_central = inquirer.select(
        message='TEMA: ',
        choices=temas_eventos
    ).execute()
    print()
    
    evento = {
        'nome': nome,
        'data': data,
        'tema_central': tema_central
    }
    
    events_list.append(evento)
    
    print(f"\nEvento - {nome} - cadastrado com sucesso!!\n")

def event_remove():
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

def show_events_by_theme():
    '''
    Exibe todos os eventos organizados pelo tema escolhido.
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
        print('Nenhum tema disponível')
        return
    
    print()
    tema_escolhido = inquirer.select(
        message='Qual é o tema para consultar os eventos\n',
        choices=themes_list
    ).execute()
    
    event_name = [
        event['nome'] 
        for event in events_list
        if tema_escolhido in event['tema_central']
    ]
    
    print(f'\nEventos sobre - {tema_escolhido} - :\n')
    for event in event_name:
        print(f'- {event}')
    print()

def number_events_by_theme():
    '''
    Exibe a quantidade de eventos que cada tema possui
    '''
    
    if not events_list:
        print('\nNão há eventos no momento!\n')
        return
    
    theme_counted = dict(Counter([event['tema_central'] for event in events_list]))
    
    print()
    print('----- QUANTIDADE DE EVENTOS POR TEMA -----\n')
    for tema, qtde in theme_counted.items():
        print(f'{tema} : {qtde} evento(s)')
