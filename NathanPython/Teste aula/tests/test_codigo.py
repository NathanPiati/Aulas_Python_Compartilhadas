from minhas_funcoes import somar, subtrair
import pytest

def test_soma_positiva():
    assert somar(5, 3) == 8


def test_soma_negativa():
    assert somar(-10, -2) == 8


def test_subtracao():
    assert subtrair(10, 5) == 5        


def test_soma_com_tipo_invalido():
    with pytest.raises(TypeError):
        somar(5, "texto")