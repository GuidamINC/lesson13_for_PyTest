from functions import hello_who,salary

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max', 'CriticalERROR: MAX'
    assert hello_who('Igor') == 'Hello, Igor', 'CriticalERROR: IGOR'
    assert hello_who('Sasha') == 'Hello, Sasha', 'CriticalERROR: SASHA'
    assert hello_who('Max1') == 'Hello, Max1', 'CriticalERROR: MAX1'
    assert hello_who('Max2') == 'Hello, Max2', 'CriticalERROR: MAX2'

def test_salary_max():
    assert salary(2,5)==10,'CriticalERROR: bolshai zarplat'