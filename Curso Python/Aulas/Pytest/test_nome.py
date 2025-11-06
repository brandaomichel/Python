import pytest
from nome import quebra_nome

@pytest.mark.parametrize("nomecompleto,resultado",[("Fernando Amaral", "Fernando Amaral"), 
                                                   ("Jose Carlos Teixeira", "Jose Teixeira"), 
                                                   ("Ana Soares", "Ana Soares"), 
                                                   ("Ana Rosa", "Ana Rosa"),
                                                   ("Maria Da slva", "")])
def test_quebra_nome(nomecompleto, resultado):
    assert quebra_nome(nomecompleto) == resultado