from InquirerPy import inquirer
from event_data import events_list

def show_event_list():
    '''
    A função mostra a lista dos eventos com data e tema que ainda pode ser aprimorada
    '''
    
    for i, item in enumerate(events_list):
        print(f'{i + 1} - Evento: {item["nome"]}')
        print(f'  Data: {item["data"]}')
        print(f'  Tema: {item["tema_central"]}\n')

def show_participants_event():
    '''
    A função mostra, primeiramente a lista dos eventos para que o usuário possa escolher o evento no
    qual deseja ver os participantes inseridos. Há uma verificação com if-else que poderá ser aprimorada.
    '''
    
    show_event_list()
    
    print('--> VERIFICAR PARTICIPANTES DO EVENTO <--\n')
    n = int(input('Digite o número do evento para ver os participantes (Apenas Números) \n'))
    
    if 1 <= n <= len(events_list):
        print(f'\nOs participantes do evento {events_list[n - 1]["nome"]} são: \n')
        
        for participants in events_list[n - 1]["participantes_event"]:
            print(f'Nome: {participants["nome"]}')
            print(f'Email: {participants["email"]} \n')
    else:
        pass

def new_event_register():
    '''
    - Funcionalidade em desenvolvimento
    Implementação inicial do cadastro de um novo evento usando inquirer.
    Procurar forma de vincular participantes ao evento
    Arrumar formatação da data
    mudar forma de escolher o tema central
    '''
    
    print(f'===== CADASTRO DE UM NOVO EVENTO =====')
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
    
    evento = {
        'nome': nome,
        'data': data,
        'tema_central': tema_central
    }
    
    events_list.append(evento)
    
    print(f"Evento {nome} cadastrado com sucesso!!")

def event_remove():
    '''
    - Funcionalidade em desenvolvimento.
    Implementação inicial da remoção de evento.
    Ajustar funcionalidade para facilitar o entendimento do usuário.
    '''
    
    choices = []
    for evento in events_list:
        choices.append(evento['nome'])
    
    evento_excluir = inquirer.select(
        message='Qual evento deseja excluir? \n',
        choices=choices
    ).execute()
    
    for evento in events_list:
        for chave in evento.values():
            if chave == evento_excluir:
                events_list.remove(evento)
    
    show_event_list()

event_remove()