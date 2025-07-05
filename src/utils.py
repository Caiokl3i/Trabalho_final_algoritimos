from datetime import datetime
from InquirerPy import inquirer
import os

def validar_data(data_string):
    '''
    Validates whether a string is in the correct date format (dd/mm/yyyy) using datetime.
        - Returns True if valid, False otherwise.
    '''
    
    try:
        datetime.strptime(data_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def cpf_validate():
    '''
    Prompts the user to enter a valid CPF (Brazilian individual taxpayer ID).
    Ensures input is numeric and exactly 11 digits long.
    Returns the validated CPF as a string.
    '''
    
    print()
    while True:
        cpf = inquirer.text(
            message='CPF do participante (apenas números): '
        ).execute()
        
        if not cpf.isdigit():
            print('\n - CPF inválido! Digite apenas números\n')
            continue
        elif len(cpf) != 11:
            print('\n - CPF inválido! Deve ter 11 digitos\n')
            continue
        break
    
    return cpf

def email_validate():
    '''
    Prompts the user to enter a valid email address.
    Performs basic structure validation (non-empty, contains '@' and '.', does not start or end with '@').
    Returns the validated email as a string.
    '''
    
    print()
    while True:
        email = inquirer.text(
            message='Email: ',
            validate=lambda result: len(result) > 0 or '\nÉ obrigatório preencher esse campo!\n'
        ).execute()
        email = email.replace(" ", "")
        
        if not email:
            print('\nEmail não pode ser vazio')
            continue
        elif email[0] == '@' or email[len(email)-1] == '@':
            print('\nDigite um email válido\n')
            continue
        elif not '@' in email:
            print('\nDigite um email válido\n')
            continue
        elif not '.' in email:
            print('\nDigite um email válido\n')
            continue
        break
        
    return email

def name_validate():
    '''
    Clears the terminal screen.
    Compatible with Windows and Unix-based systems.
    '''
    
    print()
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
    
    return name

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
Predefined list of technology-related themes used for classifying events.
Each item represents a specific event theme.
'''

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