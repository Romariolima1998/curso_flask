from datetime import datetime

def format_date(value: datetime):
    return value.strftime('%d-%m-%Y %H:%M:%S')