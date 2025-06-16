from participant_data import participants_list

def search_code_partcipant():
    '''
    Funcionalidade ainda em desenvolvimento.
    Falta ajustar a o layout do menu.
    '''
    
    print('\n ---> VERIFICAÇÃO DOS DADOS DOS PARTICPANTES <--- \n')
    cpf = int(input('Digite o cpf do participante: \n'))
    
    for i, participants in enumerate(participants_list):
        if cpf == participants["cpf"]:
            print(f'\nInformações do participante: \n')
            print(f' CPF: {participants["cpf"]}')
            print(f' Nome: {participants["nome"]}')
            print(f' Email: {participants["email"]}')
            print(f' Prefereências Temáticas: {participants["preferencias_tematicas"]}')