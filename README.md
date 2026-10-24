# Cloud Forge: laboratorio de CI seguro

1. Subir todo este proyecto a un repositorio de practica, incluida la carpeta .github.
2. Consultar Guia_Laboratorio.pdf para los pasos y salidas esperadas.
3. Actions ejecuta cinco controles y condiciona el empaquetado a su aprobacion.
4. No usar secretos reales ni instalar la dependencia vulnerable del experimento.

Entorno: Python 3.11, runner ubuntu-latest, Docker disponible en runner.
Versiones de herramientas fijadas para docencia, no necesariamente actuales.
Revisar y actualizar antes de uso productivo. Fijar acciones por SHA y contenedores
por digest verificado en produccion. El SCA excluye herramientas dev en este
laboratorio: ampliar cobertura e inventario para una implementacion real.
No se ha ejecutado este workflow en GitHub desde el entorno de generacion.
