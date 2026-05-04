# Pruebas Combinatorias con Python

Proyecto de calidad de software que implementa dos estrategias de generación de casos de prueba combinatorios en Python: **Diseño de Experimentos (DOE)** con matriz factorial completa y **Pairwise** con la técnica de todos los pares.

---

## Descripción general

Este proyecto aplica técnicas de pruebas combinatorias sobre un sistema de comercio electrónico con 5 factores de entrada:

| Factor | Valores posibles |
|---|---|
| Tipo de Cliente | Nuevo, Premium, Vip, Corporativo |
| Método de Pago | Débito, Crédito, PayPal, Transferencia, Contra entrega |
| Tipo de Envío | Recogida en Tienda, A Domicilio, Internacional |
| Dispositivo | Windows/Mac, Laptop, Android, iPhone, Tablet |
| Navegador | Chrome, Firefox, Edge, Safari, Opera |

---

## Técnicas implementadas

### 1. Matriz DOE (Diseño de Experimentos)

Genera la matriz factorial **completa** con todas las combinaciones posibles usando `pyDOE3`.

- Total de combinaciones: **4 × 5 × 3 × 5 × 5 = 1500 casos**
- Resultado guardado en: `matriz_completa_DOE.csv`

### 2. Pairwise (Todos los Pares)

Genera casos de prueba optimizados con `allpairspy`, garantizando que cada par de valores aparezca al menos una vez.

- Casos generados: **significativamente menor a 1500**
- Reducción aproximada: **>95%**
- Resultado guardado en: `matriz_pairwise.csv`

---

## Estructura del proyecto

```
pruebas-combinatorias-con-python/
├── DOE/                      # Scripts de generación DOE
├── tests/                    # Pruebas automatizadas con pytest
├── analisis_estatico/        # Análisis estático del código
├── cobertura/                # Reportes de cobertura
├── matriz_completa_DOE.csv   # Resultado DOE (1500 filas)
├── matriz_pairwise.csv       # Resultado Pairwise
├── requirements.txt          # Dependencias
└── pytest.ini                # Configuración de pytest
```

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/norah30/pruebas-combinatorias-con-python.git
cd pruebas-combinatorias-con-python

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias principales

```
pyDOE3
allpairspy
pytest
pandas
pytest-cov
pylint
```

---

## Uso

```bash
# Ejecutar pruebas
pytest

# Ejecutar con reporte de cobertura
pytest --cov
```

---

## Resultados

| Técnica | Casos generados | Cobertura de pares |
|---|---|---|
| DOE Factorial Completo | 1500 | 100% |
| Pairwise | ~25 | 100% de todos los pares |

El enfoque Pairwise logra una **reducción de más del 95%** en el número de casos de prueba manteniendo una cobertura efectiva de todas las combinaciones de pares posibles.

---

## Tecnologías

- Python 3
- pyDOE3
- allpairspy
- pytest / pytest-cov
- pandas
- pylint

<!-- actualizado -->
