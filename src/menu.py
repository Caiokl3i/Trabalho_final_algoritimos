from InquirerPy import inquirer
import events
import participants

'''
Funcionalidade ainda em desenvolvimento.
Cria um menu interativo com InquirerPy.
Cria um dicionário de escolhas para substituir um match-case ou um if-else
Falta ajustar layout, criar funções e coloca-las para rodar conforme escolha e controlar loop infinito
'''

while True:
    option = inquirer.select(
        message='=== MENU PRINCIPAL ===',
        choices=[
            {'name': '1. Listar todos os eventos', 'value': 'listar'},
            {'name': '2. Ver participantes de um evento', 'value': 'ver_participantes'},
            {'name': '3. Buscar participante por CPF', 'value': 'buscar_participante'},
            {'name': '4. Estatísticas e relatórios', 'value': 'relatorios'},
            {'name': '5. Gerenciar eventos', 'value': 'gerenciar_eventos'},
            {'name': '6. Gerenciar participantes', 'value': 'gerenciar_participantes'},
            {'name': '7. Buscar eventos por filtros', 'value': 'buscar_eventos'},
            {'name': '8. Encerrar sistema', 'value': 'sair'},
        ]    
    ).execute()
    
    if option == 'sair':
        break
    
    escolhas = {
        'listar': events.show_event_list,
        'ver_participantes': events.show_participants_by_event,
        'buscar_participante': participants.search_participant_for_cpf,
        'relatorios': 'Função',
        'gerenciar_eventos': 'Função',
        'gerenciar_participantes': 'Função',
        'buscar_eventos': events.show_events_by_theme,
        'sair': 'sair',
    }
    
    escolhas[option]()