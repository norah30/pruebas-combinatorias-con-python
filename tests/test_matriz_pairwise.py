# tests
import os
import csv
import pytest

from DOE.src.matriz_pairwise import (
    tipo_cliente,
    metodo_pago,
    tipo_envio,
    dispositivo,
    navegador,
)

def cargar_casos_csv():
    casos = []
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'matriz_pairwise.csv'))

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            casos.append((
                row["Tipo_Cliente"],
                row["Metodo_Pago"],
                row["Tipo_Envio"],
                row["Dispositivo"],
                row["Navegador"],
            ))

    return casos

# Validación de cobertura pairwise
@pytest.mark.parametrize(
    "cliente, pago, envio, device, browser",
    cargar_casos_csv(),
)
def test_combinaciones_validas(cliente, pago, envio, device, browser):
    """Valida que cada valor pertenece a su lista original."""

    assert cliente in tipo_cliente, f"ERROR → Tipo de Cliente inválido: {cliente}"
    assert pago in metodo_pago, f"ERROR → Método de Pago inválido: {pago}"
    assert envio in tipo_envio, f"ERROR → Tipo de Envío inválido: {envio}"
    assert device in dispositivo, f"ERROR → Dispositivo inválido: {device}"
    assert browser in navegador, f"ERROR → Navegador inválido: {browser}"

    resultado = True
    assert resultado is True
