from src.calculadora import soma, subtracao, multiplicacao, divisao

import pytest

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-2, -3) == -5

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(-1, 1) == -2
    assert subtracao(0, 0) == 0
    assert subtracao(-2, -3) == 1

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(0, 5) == 0
    assert multiplicacao(-2, -3) == 6

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(-6, 2) == -3
    assert divisao(0, 1) == 0
    
    # testando a divisao por 0
    with pytest.raises(ValueError):
        divisao(1, 0)
