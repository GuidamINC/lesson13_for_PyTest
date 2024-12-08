def hello_who(name):
    return f'Hello, {name}'

def salary(hours, salary_by_hour):
    '''Расчет ЗП сотрудника
    :param hours: количество часов
    :param solary_by_hour: зарплата за час
    :return: итоговая сумма'''
    k = 2
    return hours * salary_by_hour*k