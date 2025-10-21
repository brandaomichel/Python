import pytest
from nome_abreviado import abreviatura

@pytest.mark.parametrize("nomecompleto,resultado",[("Fernando Amaral", "F A"), 
                                                   ("Jose Carlos Teixeira", "F A J C T"), 
                                                   ("Ana Soares", "F A J C T A S"), 
                                                   ("Ana Rosa", "F A J C T A S A R"),
                                                   ("Maria Da slva", "")])
def test_nome_abreviado(nomecompleto, resultado):
    assert abreviatura(nomecompleto) == resultado