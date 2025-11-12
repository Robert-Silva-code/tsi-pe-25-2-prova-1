import mock
import builtins
import main

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q_exemplo(capfd, monkeypatch):
    entrada_saida = {
        '1': '',
        '2': '2\n',
        '10': '2\n4\n6\n8\n10\n'
    }
    for entrada, saida_esperada in entrada_saida.items():
        with mock.patch.object(builtins, 'input', lambda _: entrada):
            main.q_exemplo()
            sua_saida, err = capfd.readouterr()
            assert sua_saida == saida_esperada

def test_q1(capfd, monkeypatch):
    entrada_saida = {
        '555,777,666': '555\n666\n777\n',
        '3,2,1': '1\n2\n3\n',
        '2,3,2': '2\n2\n3\n',
    }
    for entrada, saida_esperada in entrada_saida.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(entrada.split(',')))
        main.q1()
        out, _ = capfd.readouterr()
        assert out == saida_esperada

def test_q2(capfd, monkeypatch):
    entrada_saida = {
        '80,1': '90.00\n',
        '301,3': '282.00\n',
        '300,3': '270.00\n',
        '1320,10': '4740.00\n',
    }
    for entrada, saida_esperada in entrada_saida.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(entrada.split(',')))
        main.q2()
        sua_saida, _ = capfd.readouterr()
        assert sua_saida == saida_esperada

def test_q3(capfd, monkeypatch):
    entrada_saida = {
        '1': '1 \n',
        '2': '1 \n1 2 \n',
        '5': '1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n',
        '10': '1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5 \n1 2 3 4 5 6 \n1 2 3 4 5 6 7 \n1 2 3 4 5 6 7 8 \n1 2 3 4 5 6 7 8 9 \n1 2 3 4 5 6 7 8 9 10 \n'
    }
    for entrada, saida_esperada in entrada_saida.items():
        with mock.patch.object(builtins, 'input', lambda _: entrada):
            main.q3()
            sua_saida, err = capfd.readouterr()
            assert sua_saida == saida_esperada


def test_q4(capfd, monkeypatch):
    entrada_saida = {
    '-1, 0': '0.00\n',
    '-1, 10': '10.00\n',
    '-1, 5, 5': '5.00\n',
    '-1, 10, 8, 6': '8.00\n',
    '-1, 5, 7, 10': '7.33\n',
    '-1, 7.5, 8.25, 9.75': '8.50\n',
    '-1, 6.4, 6.6': '6.50\n',
    '-1, 9.99, 9.99, 9.99': '9.99\n',
    '-1, 0, 0, 0': '0.00\n',
    '-1, 10, 10, 10': '10.00\n',
    '-1, 0, 10': '5.00\n',
    '-1, 10, 0, 10, 0': '5.00\n',
    '-1': '0.00\n',
    '-1, 7.666, 7.666, 7.666': '7.67\n',
    '-1, 7.333, 7.333, 7.333': '7.33\n',
    }

    for entrada, saida_esperada in entrada_saida.items():
        with mock.patch.object(builtins, 'input', make_multiple_inputs(entrada.split(','))):
            main.q4()
            sua_saida, err = capfd.readouterr()
            assert sua_saida == saida_esperada

def test_q5(capfd):
    input_output = {
        'romulo junior':'Romulo Junior\n', 
        'zé da manga': 'Zé da Manga\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q5()
            out, err = capfd.readouterr()
            assert out == v

def test_q6(capfd):
    input_output = {
        '222':'equilátero\n',
        '322': 'isósceles\n',
        '345': 'escaleno\n'
    }
    for k,v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q6()
            out, err = capfd.readouterr()
            assert out == v


def test_q7(capfd):
    input_output = {
        '7': 'O número não possui divisores multiplos de 3\n',
        '3': 'Quantidade de divisores divisiveis por 3: 1\n',
        '555':'Quantidade de divisores divisiveis por 3: 4\n',
        '3144':'Quantidade de divisores divisiveis por 3: 8\n',
        '17640':'Quantidade de divisores divisiveis por 3: 48\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q7()
            out, err = capfd.readouterr()
            assert out == v