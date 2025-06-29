from InquirerPy import inquirer
import events
import participants

def menu_principal():
    """
    Exibe o menu principal do sistema e executa a funcionalidade selecionada.

    Utiliza InquirerPy para interação com funções diretamente nos valores.
    """
    
    escolhas = [
                {'name': '1. Listar todos os eventos', 'value': events.show_event_list},
                {'name': '2. Ver participantes de um evento', 'value': events.show_participants_by_event},
                {'name': '3. Buscar participante por CPF', 'value': participants.search_participant_for_cpf},
                {'name': '4. Estatísticas e relatórios', 'value': lambda: print("[Função em construção]")},
                {'name': '5. Gerenciar eventos', 'value': lambda: print("[Função em construção]")},
                {'name': '6. Gerenciar participantes', 'value': lambda: print("[Função em construção]")},
                {'name': '7. Buscar eventos por filtros', 'value': events.show_events_by_theme},
                {'name': '8. Encerrar sistema', 'value': False},
            ]

    while True:
        print()
        option = inquirer.select(
            message='----- MENU PRINCIPAL -----\n',
            choices=escolhas
        ).execute()
        
        if not option:
            print('Saindo ...')
            break
        
        option()

def menu_dinamico_func(*opcoes):
    """
    Exibe um menu interativo com InquirerPy a partir de uma lista de tuplas (nome, função).
    
    Exemplo de uso:
        mostrar_menu_e_executar(
            ('Cadastrar evento', cadastrar_evento),
            ('Remover evento', remover_evento)
        )
    """
    
    choice_list = [{'name': name, 'value': func} for name, func in opcoes]

    print()
    escolha = inquirer.select(
        message='O que deseja fazer agora?\n',
        choices=choice_list
    ).execute()
    
    escolha()