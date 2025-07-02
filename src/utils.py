from datetime import datetime

def validar_data(data_string):
    '''
    Valida formato de strings para datas com datetime
    '''
    
    try:
        datetime.strptime(data_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False
