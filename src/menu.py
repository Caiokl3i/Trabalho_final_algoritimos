from InquirerPy import inquirer
import events
import participants

def menu_principal():
    """
    Exibe o menu principal do sistema e executa a funcionalidade selecionada.

    Utiliza InquirerPy para interação com funções diretamente nos valores.
    """
    
    escolhas = [
                {'name': '5. Gerenciar eventos', 'value': menu_gerenciar_eventos},
                {'name': '6. Gerenciar participantes', 'value': menu_gerenciar_participantes},
                {'name': '4. Estatísticas e relatórios', 'value': lambda: print("[Função em construção]")},
                {'name': '8. Encerrar sistema', 'value': False},
            ]

    while True:
        
        print()
        option = inquirer.select(
            message='----- MENU PRINCIPAL -----\n',
            choices=escolhas
        ).execute()
        print()
        
        if not option:
            print('Saindo ...')
            break
        
        option()

def menu_gerenciar_eventos():
    while True:
        choices = [
                {'name': '1. Listar todos os eventos', 'value': events.show_event_list},
                {'name': '2. Buscar eventos por tema', 'value': events.show_events_by_theme},
                {'name': '3. Ver quantidade de eventos por tema', 'value': events.number_events_by_theme},
                {'name': '4. Ver participantes de um evento específico', 'value': events.show_participants_by_event},
                {'name': '5. Adicionar novo evento', 'value': events.new_event_register},
                {'name': '6. Excluir evento', 'value': events.event_remove},
                {'name': '7. Voltar', 'value': False}
            ]
        
        print()
        option = inquirer.select(
            message='----- GERENCIAR EVENTOS -----\n',
            choices=choices
        ).execute()
        print()
        
        if not option:
            break
        
        option()

def menu_gerenciar_participantes():
    while True:
        choices = [
                {'name': '1. Buscar participante por CPF', 'value': participants.search_participant_for_cpf},
                {'name': '2. Consultar informações de um participante', 'value': participants.info_participant_for_cpf},
                {'name': '3. Editar dados de um participante', 'value': participants.edit_participant_data},
                {'name': '4. Mostrar eventos de um participante', 'value': lambda: print('Em andamento')},
                # listar todos os eventos em que um participante espec´ıfico est´a inscrito
                {'name': '5. Voltar', 'value': False}
            ]
        
        print()
        option = inquirer.select(
            message='----- GERENCIAR PARTICIPANTES -----\n',
            choices=choices
        ).execute()
        print()
        
        if not option:
            break
        
        option()

def report_statistics():
    while True:
        choices = [
                {'name': '1. Temas mais frequentes', 'value': lambda: print('Funcionalidade em construção')},
                {'name': '2. Participantes mais ativos', 'value': lambda: print('Funcionalidade em construção')},
                {'name': '3. Taxa média de participação por tema', 'value': lambda: print('Funcionalidade em construção')},
                {'name': '4. Eventos com poucos inscritos', 'value': lambda: print('Funcionalidade em construção')},
                # identificar eventos com menos de dois participantes (para poss´ıvel cancelamento)
                {'name': '5. Voltar', 'value': False}
            ]
        
        option = inquirer.select(
            message='----- ESTATÍSTICAS E RELATÓRIOS -----\n',
            choices=choices
        ).execute()
        
        if not option:
            break
        
        option()