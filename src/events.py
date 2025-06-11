from event_data import events_list

def show_events():
    for item in events_list:
        print(f'Evento: {item["nome"]} \n  Data: {item["data"]}\n  Tema: {item["tema_central"]}\n')

