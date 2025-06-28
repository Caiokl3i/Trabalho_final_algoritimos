from InquirerPy import inquirer
from event_data import events_list

def show_event_list():
    '''
    Exibe todos os eventos cadastrados com nome, data e tema central.
    - Se a lista de eventos estiver vazia, exibe uma mensagem de aviso e encerra a função.
    '''
    
    if not events_list:
        print('! A lista está vazia !')
        return
    
    print('\nLista de eventos:\n')
    for i, item in enumerate(events_list):
        print('-' * 50)
        print(f'{i + 1} - Evento: {item["nome"]}')
        print(f'  Data: {item["data"]}')
        print(f'  Tema: {item["tema_central"]}\n')

def show_participants_by_event():
    '''
    Exibe a lista de eventos para que o usuário escolha um,
    e então mostra os participantes do evento escolhido.
    '''
    
    show_event_list()
    
    print('--> VERIFICAR PARTICIPANTES DO EVENTO <--\n')
    
    if not events_list:
        print('! A lista está vazia !')
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

    print(f'\nOs participantes do evento {events_list[n - 1]["nome"]} são: \n')
    
    for participant in events_list[n - 1]["participantes_event"]:
        print(f'Nome: {participant["nome"]}')
        print(f'Email: {participant["email"]} \n')

def new_event_register():
    '''
    - Funcionalidade em desenvolvimento
    Implementação inicial do cadastro de um novo evento usando inquirer.
    Procurar forma de vincular participantes ao evento.
    Arrumar formatação da data.
    mudar forma de escolher o tema central.
    '''
    
    print(f'\n===== CADASTRO DE UM NOVO EVENTO =====\n')
    nome = inquirer.text(
        message='NOME: ',
        validate=lambda result: len(result) > 0 or "É obrigatorio preencher esse campo"
    ).execute()
    data = inquirer.text(
        message='DATA: '
    ).execute()
    tema_central = inquirer.text(
        message='TEMA: '
    ).execute()
    
    print()
    
    evento = {
        'nome': nome,
        'data': data,
        'tema_central': tema_central
    }
    
    events_list.append(evento)
    
    print(f"Evento {nome} cadastrado com sucesso!!")
    
    show_event_list()

def event_remove():
    '''
    - Funcionalidade em desenvolvimento.
    Implementação inicial da remoção de evento.
    Ajustar funcionalidade para facilitar o entendimento do usuário.
    '''
    
    choices = [evento['nome'] for evento in events_list]
    
    evento_excluir = inquirer.select(
        message='Qual evento deseja excluir? \n',
        choices=choices
    ).execute()
    
    for i, evento in enumerate(events_list):
        if evento['nome'] == evento_excluir:
            del events_list[i]
            print(f'\nEvento {evento_excluir} excluído com sucesso!')
    
    show_event_list()