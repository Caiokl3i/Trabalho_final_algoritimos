from participant_data import participants_list
from event_data import events_list
from InquirerPy import inquirer
from collections import Counter

def search_participant_for_cpf():
    '''
    Função auxiliar que busca o participante por cpf
    '''
    # arrumar como recebe o cpf
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

def display_info_participant_for_cpf():
    '''
    - Exibe as informações do participante através da busca pelo CPF
    '''
    
    participant = search_participant_for_cpf()
    
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
    Exibe os dados do participante atraves do CPF e permite editar os
    dados por um menu interativo.
    '''
    
    participant = search_participant_for_cpf()
    
    if not participant:
        print(f'Participante não encontrado!')
        return None
    
    print('\n----- INSIRA OS NOVOS DADOS DO PARTICIPANTE -----\n')
    
    name = inquirer.text(
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
    
    themes = set([event['tema_central'] for event in events_list])
    
    thematic_preferences = inquirer.select(
        message='PREFERÊNCIA TEMÁTICA: ',
        choices=themes
    ).execute()
    
    # arrumar
    participant['nome'] = name
    participant['email'] = email
    participant['preferencias_tematicas'] = [thematic_preferences]
    
    print()

def detect_duplicate_participants(cpf, event_name):
    '''
    Verifica se o CPF informado já está inscrito no evento.

    Retorna:
        True  – se o participante ainda não estiver no evento (pode adicionar)
        False – se o participante já estiver inscrito (duplicata)
    '''

    for event in events_list:
        if event['nome'] == event_name:
            for participant in event['participantes_event']:
                if cpf == participant['cpf']:
                    return False
    return True

def display_events_by_participant():
    '''
    Exibe todos os eventos em que um participante está inscrito (com base no CPF).
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
    Inscreve o aluno selecionado pelo CPF no evento escolhido
    '''
    
    while True:
        try:
            cpf = int(input('\nDigite o CPF do Aluno: \n'))
            if len(str(cpf)) == 11:
                break
            else:
                print('CPF Inválido!\n')
        except ValueError:
            print('Digite apenas números\n')
    
    if not participants_list:
        print('\nA lista de participantes está vazia\n')
        return None
    
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

def register_new_participant():
    '''
    Cadastra um novo participante no "banco de dados" de participantes
    '''
    
    while True:
        cpf = inquirer.text(
            message='CPF do novo participante (apenas números): '
        ).execute()
        
        if not cpf.isdigit():
            print('\n - CPF inválido! Digite apenas números\n')
            continue
        elif len(cpf) != 11:
            print('\n - CPF inválido! Deve ter 11 digitos\n')
            continue
        
        ixisting_cpf = any([partic['cpf'] == cpf for partic in participants_list])
        if ixisting_cpf:
            print('\n - O CPF já está cadastrado')
            continue
        
        break
    while True:
        name = inquirer.text(
            message='\nNome do participante:'
        ).execute()
        
        name = name.strip()
        
        if any(letter.isdigit() for letter in name):
            print('\nO nome não pode conter números\n')
            continue
        if not name:
            print('O nome não pode ser vazio')
            continue
        break
    
    while True:
        #tem forma melhor
        email = inquirer.text(
                message='\nEmail do participante:'
            ).execute()
            
        if any(caracters == ' ' for caracters in email):
            print('Email inválido')
            continue
        
        if not '@' in email:
            print('\nEmail inválido!')
        elif not '.' in email:
            print('\nEmail inválido!')
            continue
        
        break
    
    event_themes = [
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
    while True:
        chosen_theme = inquirer.select(
            message='\nPreferêcia temática:\n',
            choices=event_themes
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
