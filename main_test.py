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

