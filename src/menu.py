from InquirerPy import inquirer
import events
import participants
import report
import time

def main_menu():
    """
    Exibe o menu principal do sistema e executa a funcionalidade selecionada.

    Utiliza InquirerPy para interação com funções diretamente nos valores.
    """
    
    while True:
        time.sleep(0.3)
        
        choices = [
                {'name': '1. Gerenciar eventos', 'value': manage_events_menu},
                {'name': '2. Gerenciar participantes', 'value': manage_participants_menu},
                {'name': '3. Estatísticas e relatórios', 'value': menu_relatorios_estatisticas},
                {'name': '4. Encerrar sistema', 'value': False},
            ]
        
        print()
        option = inquirer.select(
            message='----- MENU PRINCIPAL -----\n',
            choices=choices
        ).execute()
        print()
        
        if not option:
            print('Saindo ...')
            break
        
        option()

def manage_events_menu():
    '''
    Exibe o menu de gerenciamento das funcionalidades relacionadas aos eventos.
    '''
    
    while True:
        time.sleep(0.3)
        
        choices = [
                {'name': '1. Listar todos os eventos', 'value': events.display_event_list},
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

def manage_participants_menu():
    '''
    Exibe o menu de gerenciamento das funcionalidades relacionadas aos participantes.
    '''
    
    while True:
        time.sleep(0.3)
        
        choices = [
                {'name': '1. Cadastrar um novo participante', 'value': participants.register_new_partic},
                {'name': '1. Cadastrar um novo participante', 'value': participants.register_new_partic},
                {'name': '1. Inscrever participante em um evento', 'value': participants.add_participant_in_event},
                {'name': '2. Buscar participante por CPF', 'value': participants.info_participant_for_cpf},
                {'name': '3. Consultar informações de um participante', 'value': participants.info_participant_for_cpf},
                {'name': '4. Editar dados de um participante', 'value': participants.edit_participant_data},
                {'name': '5. Mostrar eventos de cada participante', 'value': participants.events_each_partic},
                {'name': '5. Mostrar eventos de um participante específico', 'value': participants.show_events_by_participant},
                {'name': '5. Remover um particpante', 'value': participants.participant_delete},
                {'name': '6. Voltar', 'value': False}
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

def menu_relatorios_estatisticas():
    '''
    Exibe o menu de funcionalidades relacionadas aos relatorios e estatisticas.
    '''
    
    while True:
        time.sleep(0.3)
        
        choices = [
                {'name': '1. Temas mais frequentes', 'value': report.themes_frequency_report},
                {'name': '2. Participantes mais ativos', 'value': report.more_actives_partic},
                {'name': '3. Taxa média de participação por tema', 'value': report.average_theme},
                {'name': '4. Eventos com poucos inscritos', 'value': report.less_than_2_partic},
                {'name': '5. Voltar', 'value': False}
            ]
        
        option = inquirer.select(
            message='\n----- ESTATÍSTICAS E RELATÓRIOS -----\n',
            choices=choices
        ).execute()
        
        if not option:
            break
        
        option()