from participant_data import participants_list
from InquirerPy import inquirer

def search_participant_for_cpf():
    '''
    Funcionalidade ainda em desenvolvimento.
    Falta ajustar a o layout do menu.
    '''
    
    print('\n ---> VERIFICAÇÃO DOS DADOS DOS PARTICPANTES <--- \n')
    cpf = int(input('Digite o cpf do participante: \n'))
    
    for participants in participants_list:
        if cpf == participants["cpf"]:
            print(f'\nInformações do participante: \n')
            print(f' CPF: {participants["cpf"]}')
            print(f' Nome: {participants["nome"]}')
            print(f' Email: {participants["email"]}')
            print(f' Prefereências Temáticas: {participants["preferencias_tematicas"]}\n')

def edit_participant_data():
    '''
    - Funcionalidade em desenvolvimento.
    Exibe os dados do participante atraves do CPF e permite editar os
    dados por um menu interativo.
    '''
    
    cpf = int(input('Digite o cpf do participante: \n'))
    
    for participants in participants_list:
        if cpf == participants["cpf"]:
            print(f'\nInformações do participante: \n')
            print(f' CPF: {participants["cpf"]}')
            print(f' Nome: {participants["nome"]}')
            print(f' Email: {participants["email"]}')
            print(f' Preferências Temáticas: {participants["preferencias_tematicas"]}\n')
    
    print('\n----- INSIRA OS NOVOS DADOS DO PARTICIPANTE -----\n')
    
    for participant in participants_list:
        if cpf == participant['cpf']:
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
            participant['preferencias_tematicas'] = themes_preffer
            
            print(participant)