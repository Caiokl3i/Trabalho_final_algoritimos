from participant_data import participants_list
from event_data import events_list
from InquirerPy import inquirer

def search_participant_for_cpf(cpf):
    '''
    Função auxiliar que busca o participante por cpf, assim fica mais fácil de
    manipular os dados, sem precisar fazer isso várias vezes
    '''
    
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
    
    print(f'\n----- BUSCAR USUÁRIO ATRAVÉS DO CPF -----\n')
    
    while True:
        try:
            cpf = int(input('\nDigite o CPF do Aluno: '))
            if len(str(cpf)) == 11:
                break
            else:
                print('CPF Inválido!')
        except ValueError:
            print('Digite apenas números')
    
    participant = search_participant_for_cpf(cpf)
    
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
    ( Arrumar preferencias temáticas )
    '''
    
    participant = info_participant_for_cpf()
    
    if not participant:
        print(f'Participante não encontrado!')
        return None
    
    print('\n----- INSIRA OS NOVOS DADOS DO PARTICIPANTE -----\n')
    
    nome = inquirer.text(
        message='NOME: ',
        validate=lambda result: len(result) > 0 or 'É obrigatório preencher esse campo!'
    ).execute()
    email = inquirer.text(
        message='EMAIL: ',
        validate=lambda result: len(result) > 0 or 'É obrigatório preencher esse campo!'
    ).execute()
    themes_preffer = inquirer.text(
        message='PREFERÊNCIA TEMÁTICA: ',
        validate=lambda result: len(result) > 0 or 'É obrigatório preencher esse campo!'
    ).execute()

    participant['nome'] = nome
    participant['email'] = email
    participant['preferencias_tematicas'] = [themes_preffer]

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

