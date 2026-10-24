import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Sheet 1: Matriz de Evidencias
ws1 = wb.active
ws1.title = "Matriz de Evidencias"
ws1.views.sheetView[0].showGridLines = True

# Paleta de colores
NAVY_HEADER = "1E293B"      # Slate 800
WHITE = "FFFFFF"
LIGHT_GRAY = "F8FAFC"       # Slate 50
BORDER_COLOR = "CBD5E1"     # Slate 300
ACCENT_BLUE = "0284C7"      # Sky 600

# Fills
header_fill = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
zebra_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
white_fill = PatternFill(start_color=WHITE, end_color=WHITE, fill_type="solid")

success_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Emerald 100
success_font = Font(name="Segoe UI", size=10, bold=True, color="166534") # Emerald 800

skipped_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid") # Rose 100
skipped_font = Font(name="Segoe UI", size=10, bold=True, color="991B1B") # Rose 800

thin_border = Border(
    left=Side(style='thin', color=BORDER_COLOR),
    right=Side(style='thin', color=BORDER_COLOR),
    top=Side(style='thin', color=BORDER_COLOR),
    bottom=Side(style='thin', color=BORDER_COLOR)
)

# Título y metadatos
ws1.merge_cells("A1:K1")
title_cell = ws1["A1"]
title_cell.value = "LABORATORIO 2: PIPELINE SEGURO PASO A PASO (CLOUD FORGE CI)"
title_cell.font = Font(name="Segoe UI", size=15, bold=True, color="0F172A")
title_cell.alignment = Alignment(vertical="center", indent=1)
ws1.row_dimensions[1].height = 35

ws1.merge_cells("A2:K2")
meta_cell = ws1["A2"]
meta_cell.value = "Repositorio: https://github.com/lianlee007/cloud-forge-ci | Entorno: GitHub Actions | Controles: Ruff, Pytest, Bandit, Trivy Secret, Trivy SCA"
meta_cell.font = Font(name="Segoe UI", size=9.5, italic=True, color="64748B")
meta_cell.alignment = Alignment(vertical="center", indent=1)
ws1.row_dimensions[2].height = 22

headers = [
    "Experimento",
    "Commit Fallo",
    "Control Esperado",
    "Control Observado",
    "Regla / Aviso",
    "Archivo / Paquete Afectado",
    "Estado Package",
    "Corrección Aplicada",
    "Commit Corregido",
    "Enlace a Ejecución",
    "Reportes Generados"
]

ws1.append([]) # Fila 3 vacía
ws1.row_dimensions[3].height = 10

ws1.append(headers) # Fila 4 encabezados
ws1.row_dimensions[4].height = 28

for col_num in range(1, len(headers) + 1):
    c = ws1.cell(row=4, column=col_num)
    c.fill = header_fill
    c.font = Font(name="Segoe UI", size=10.5, bold=True, color=WHITE)
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border

rows_data = [
    [
        "Línea base",
        "N/A",
        "todos",
        "todos_aprobados",
        "Ninguna (línea base limpia)",
        "app/ y tests/",
        "aprobado (success)",
        "N/A",
        "6bafbb7",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40048784380",
        "reporte-lint; reporte-tests; reporte-sast; reporte-secrets; reporte-sca; codigo-aprobado"
    ],
    [
        "1. Lint (Ruff)",
        "9238787",
        "lint",
        "control-lint",
        "F401 `os` imported but unused",
        "app/calculadora.py:1",
        "omitido (skipped)",
        "Eliminar import os no utilizado",
        "d386f19",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40053585502",
        "reporte-lint"
    ],
    [
        "2. Pruebas (Pytest)",
        "8c1dda4",
        "tests",
        "control-tests",
        "AssertionError: assert -1 == 5 en test_suma",
        "tests/test_calculadora.py / app/calculadora.py:2",
        "omitido (skipped)",
        "Restaurar return a + b en función sumar",
        "7f57250",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40055017418",
        "reporte-tests"
    ],
    [
        "3. SAST (Bandit)",
        "b55ffaf",
        "sast",
        "control-sast",
        "B307: Use of possibly insecure function (eval)",
        "app/calculadora.py:10",
        "omitido (skipped)",
        "Eliminar función ejemplo_inseguro con llamada a eval",
        "40264c5",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40055175920",
        "reporte-sast"
    ],
    [
        "4. Secretos (Trivy)",
        "3945b5d",
        "secrets",
        "control-secrets",
        "cloud-forge-demo (Token sintético de laboratorio - HIGH)",
        "app/demo.env:1",
        "omitido (skipped)",
        "Eliminar archivo app/demo.env con token sintético",
        "4d36a79",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40055338070",
        "reporte-secrets"
    ],
    [
        "5. SCA (Trivy)",
        "fc3c436",
        "sca",
        "control-sca",
        "CVE-2018-18074 / CVE-2023-32681 (CRITICAL/HIGH)",
        "requirements.txt (requests==2.19.1)",
        "omitido (skipped)",
        "Eliminar dependencia obsoleta e innecesaria del manifiesto",
        "74a008e",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40055438098",
        "reporte-sca"
    ],
    [
        "Verificación Final",
        "N/A",
        "todos",
        "todos_aprobados",
        "Ninguna (árbol limpio y validado)",
        "app/ y tests/",
        "aprobado (success)",
        "N/A",
        "74a008e",
        "https://github.com/lianlee007/cloud-forge-ci/actions/runs/40055564679",
        "reporte-lint; reporte-tests; reporte-sast; reporte-secrets; reporte-sca; codigo-aprobado"
    ]
]

start_row = 5
for i, row in enumerate(rows_data):
    current_row = start_row + i
    ws1.append(row)
    ws1.row_dimensions[current_row].height = 26
    
    is_even = (i % 2 == 1)
    base_fill = zebra_fill if is_even else white_fill
    
    for col_idx in range(1, len(row) + 1):
        cell = ws1.cell(row=current_row, column=col_idx)
        cell.font = Font(name="Segoe UI", size=9.5, color="334155")
        cell.border = thin_border
        cell.fill = base_fill
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        
        # Centrar columnas clave
        if col_idx in [1, 2, 3, 4, 7, 9]:
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            
        # Badges para estado de Package
        if col_idx == 7:
            if "success" in str(cell.value):
                cell.fill = success_fill
                cell.font = success_font
            else:
                cell.fill = skipped_fill
                cell.font = skipped_font
                
        # Hipervínculo para enlace de ejecución
        if col_idx == 10 and str(cell.value).startswith("http"):
            cell.hyperlink = cell.value
            cell.font = Font(name="Segoe UI", size=9.5, color="0284C7", underline="single")
            cell.value = f"Ver Run en GitHub"

# Sheet 2: Preguntas y Rúbrica
ws2 = wb.create_sheet(title="Preguntas y Respuestas")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:C1")
q_title = ws2["A1"]
q_title.value = "SECCIÓN 16: PREGUNTAS DE REFLEXIÓN Y RÚBRICA"
q_title.font = Font(name="Segoe UI", size=14, bold=True, color="0F172A")
q_title.alignment = Alignment(vertical="center", indent=1)
ws2.row_dimensions[1].height = 32

q_headers = ["#", "Pregunta de Evaluación", "Respuesta Técnica y Justificación del Pipeline"]
ws2.append([]) # row 2
ws2.row_dimensions[2].height = 8

ws2.append(q_headers) # row 3
ws2.row_dimensions[3].height = 26
for c_idx in range(1, 4):
    cell = ws2.cell(row=3, column=c_idx)
    cell.fill = header_fill
    cell.font = Font(name="Segoe UI", size=10.5, bold=True, color=WHITE)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border

qa_data = [
    (
        "1",
        "¿Por qué una prueba puede aprobar y SAST fallar?",
        "Porque las pruebas unitarias ejecutan dinámicamente únicamente el código invocado por los casos de prueba existentes. Si se añade una función vulnerable (como ejemplo_inseguro() con eval) pero ningún test la llama, la suite de pruebas continuará en verde. En cambio, SAST (Bandit) analiza el Árbol de Sintaxis Abstracta (AST) de todos los archivos del proyecto de forma estática, detectando la llamada peligrosa sin importar si fue ejecutada o testeada."
    ),
    (
        "2",
        "¿Qué implica package omitido (skipped)?",
        "El trabajo 'package' tiene una dependencia obligatoria mediante 'needs: checks'. Gracias a 'fail-fast: false', la matriz ejecuta todos los controles para generar reportes completos de diagnóstico, pero si al menos un control de seguridad o calidad falla (código distinto de 0), la condición de éxito previa no se cumple y GitHub Actions cancela/omite el empaquetado. Esto evita que código no conforme sea distribuido o desplegado."
    ),
    (
        "3",
        "¿Qué diferencia un secreto borrado de uno revocado?",
        "Un secreto borrado simplemente se retira del archivo o commit actual; sin embargo, permanece accesible en el historial de Git (commits pasados), logs de runners y copias locales, por lo que sigue siendo vulnerable y activo si el atacante consulta el historial. Un secreto revocado, por el contrario, se invalida y rota directamente en el proveedor del servicio (ej. AWS, GitHub, BD), de modo que incluso si la cadena filtrada se descubre, carece por completo de permisos."
    ),
    (
        "4",
        "¿Qué cobertura falta al escanear solo dependencias directas?",
        "Se ignora todo el grafo de dependencias transitivas (aquellas librerías requeridas indirectamente por los paquetes principales). La inmensa mayoría de las vulnerabilidades en software moderno residen en componentes secundarios o terciarios. Para cubrirlas adecuadamente, se requiere escanear un inventario cerrado con versiones exactas (como un lockfile tipo poetry.lock o requirements.lock)."
    ),
    (
        "5",
        "¿Por qué HIGH/CRITICAL no expresa por sí solo explotabilidad?",
        "La severidad CVSS evalúa el impacto teórico y la facilidad técnica intrínseca de una falla bajo un escenario estándar. No obstante, la explotabilidad real depende del contexto de la aplicación: si la función vulnerable está expuesta a entradas del usuario externo, si la librería está aislada en la red interna, o si existen controles defensivos que mitigan el vector de ataque antes de alcanzar el componente."
    ),
    (
        "6",
        "¿Qué revisar antes de aceptar código generado por IA?",
        "Se debe verificar minuciosamente: 1) Corrección funcional y cobertura de pruebas unitarias/casos borde. 2) Calidad y estándares de código (linter/tipado). 3) Patrones de seguridad (evitar eval, inyecciones SQL/OS, deserialización no confiable). 4) Alucinación de paquetes: confirmar que las librerías sugeridas existan legítimamente en el repositorio oficial y no sean malware (typosquatting). 5) Ausencia de credenciales ficticias o sensibles en el código."
    )
]

for idx, (num, q, a) in enumerate(qa_data):
    r_idx = 4 + idx
    ws2.append([num, q, a])
    ws2.row_dimensions[r_idx].height = 55
    b_fill = zebra_fill if (idx % 2 == 1) else white_fill
    
    c1 = ws2.cell(row=r_idx, column=1)
    c1.alignment = Alignment(horizontal="center", vertical="center")
    c1.font = Font(name="Segoe UI", size=10, bold=True, color="475569")
    c1.border = thin_border
    c1.fill = b_fill
    
    c2 = ws2.cell(row=r_idx, column=2)
    c2.alignment = Alignment(vertical="center", wrap_text=True)
    c2.font = Font(name="Segoe UI", size=9.5, bold=True, color="1E293B")
    c2.border = thin_border
    c2.fill = b_fill
    
    c3 = ws2.cell(row=r_idx, column=3)
    c3.alignment = Alignment(vertical="center", wrap_text=True)
    c3.font = Font(name="Segoe UI", size=9.5, color="334155")
    c3.border = thin_border
    c3.fill = b_fill

# Ajustar anchos en ws1
col_widths_ws1 = {
    "A": 20, # Experimento
    "B": 15, # Commit Fallo
    "C": 18, # Control Esperado
    "D": 18, # Control Observado
    "E": 36, # Regla / Aviso
    "F": 32, # Archivo / Paquete
    "G": 20, # Estado Package
    "H": 34, # Corrección
    "I": 16, # Commit Corregido
    "J": 22, # Enlace
    "K": 35  # Reportes
}
for col_letter, width in col_widths_ws1.items():
    ws1.column_dimensions[col_letter].width = width

# Ajustar anchos en ws2
ws2.column_dimensions["A"].width = 6
ws2.column_dimensions["B"].width = 38
ws2.column_dimensions["C"].width = 85

output_file = "c:/Users/Leonardo/Desktop/cloud-forge-ci/Laboratorio_2_Evidencias.xlsx"
wb.save(output_file)
print("Archivo Excel creado con exito en:", output_file)
