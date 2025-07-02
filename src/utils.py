from datetime import datetime

def validar_data(data_string):
    try:
        datetime.strptime(data_string, "%d/%m/%Y")
        return True
    except ValueError:
        return False
