import pytest

from app.calculadora import interpretar_entero, sumar


def test_suma():
    assert sumar(2, 3) == 5


def test_entero():
    assert interpretar_entero("12") == 12


def test_rechaza_expresiones():
    with pytest.raises(ValueError):
        interpretar_entero("2 + 3")
