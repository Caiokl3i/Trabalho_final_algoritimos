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
