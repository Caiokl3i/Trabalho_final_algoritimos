from participant_data import participants_list
from event_data import events_list
from InquirerPy import inquirer
from collections import Counter

def search_participant_for_cpf():
    '''
    Função auxiliar que busca o participante por cpf, assim fica mais fácil de
    manipular os dados, sem precisar fazer isso várias vezes
    '''
    
    while True:
        try:
            cpf = int(input('\nDigite o CPF do Aluno: '))
            if len(str(cpf)) == 11:
                break
            else:
                print('CPF Inválido!')
        except ValueError:
            print('Digite apenas números')
    
    if not participants_list:
        print('A lista de participantes está vazia')
        return None
    
    for participant in participants_list:
        if cpf == participant["cpf"]:
            return participant
    return None

def info_participant_for_cpf():
    '''
    - Exibe as informações do participante através da busca pelo CPF
    '''
    
    participant = search_participant_for_cpf()
    
    print(f'\nInformações do participante: \n')
    print(f' CPF: {participant["cpf"]}')
    print(f' Nome: {participant["nome"]}')
    print(f' Email: {participant["email"]}')
    print(f' Preferências Temáticas: {participant["preferencias_tematicas"]}\n')
    
    return participant

def edit_participant_data():
    '''
    Exibe os dados do participante atraves do CPF e permite editar os
    dados por um menu interativo.
    '''
    
    participant = info_participant_for_cpf()
    
    if not participant:
        print(f'Participante não encontrado!')
        return None
    
    themes = set([event['tema_central'] for event in events_list])
    
    print('\n----- INSIRA OS NOVOS DADOS DO PARTICIPANTE -----\n')
    
    nome = inquirer.text(
        message='NOME: ',
        validate=lambda result: len(result) > 0 or 'É obrigatório preencher esse campo!'
    ).execute()
    while True:
        email = inquirer.text(
            message='EMAIL: ',
            validate=lambda result: len(result) > 0 or 'É obrigatório preencher esse campo!'
        ).execute()
        email = email.replace(" ", "")
        
        if email[0] == '@' or email[len(email)-1] == '@':
            print('Digite um email válido')
        elif not '@' in email:
            print('Digite um email válido')
        else:
            break

    themes_preffer = inquirer.select(
        message='PREFERÊNCIA TEMÁTICA: ',
        choices=themes
    ).execute()

    participant['nome'] = nome
    participant['email'] = email
    participant['preferencias_tematicas'] = [themes_preffer]
    
    print()

def detect_duplicate_participants(cpf, event_name):
    '''
    Verifica se o CPF informado já está inscrito no evento.

    Retorna:
        True  – se o participante ainda não estiver no evento (pode adicionar)
        False – se o participante já estiver inscrito (duplicata)
    '''

    for evento in events_list:
        if evento['nome'] == event_name:
            for participante in evento['participantes_event']:
                if cpf == participante['cpf']:
                    return False
    return True

def show_events_by_participant():
    '''
    Mostra todos os eventos em que um participante está inscrito (com base no CPF).
    '''
    
    while True:
        try:
            cpf = int(input('\nDigite o CPF do aluno: '))
            if len(str(cpf)) == 11:
                break
            else:
                print('CPF Inválido!')
        except ValueError:
            print('Digite apenas números')
    
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

def events_each_partic():
    '''
    Exibe a quantidade de eventos em que cada participante esteve presente, 
    ordenando do mais ativo para o menos ativo.
    '''
    
    cpfs = []
    for evento in events_list:
        for participante in evento['participantes_event']:
            cpfs.append(participante["cpf"])
    
    cpf_para_nome = {}
    for participante in participants_list:
        cpf_para_nome[participante['cpf']] = participante['nome']
    
    count = Counter(cpfs)
    
    print('Quantidade de evento de cada participante: \n')
    for chave, valor in count.most_common():
            print(f'{cpf_para_nome[chave]} - {valor} eventos')

def add_participant_in_event():
    '''
    Inscreve o aluno selecionado pelo CPF no evento escolhido
    '''
    
    while True:
        try:
            cpf = int(input('\nDigite o CPF do Aluno: \n'))
            if len(str(cpf)) == 11:
                break
            else:
                print('CPF Inválido!')
        except ValueError:
            print('Digite apenas números')
    
    if not participants_list:
        print('A lista de participantes está vazia')
        return None
    
    events = [event['nome'] for event in events_list]
    event_name = inquirer.select(
        message='Escolha o evento para cadastrar o participante:\n',
        choices=events
    ).execute()
    
    if not detect_duplicate_participants(cpf, event_name):
        print('Esse aluno já está participando deste evento!\n')
        return
    
    participant = next((partic for partic in participants_list if cpf == partic['cpf']))
    
    for event in events_list:
        if event['nome'] == event_name:
            event['participantes_event'].append(participant)
