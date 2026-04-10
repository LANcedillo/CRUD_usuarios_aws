#!/bin/bash

# Salir inmediatamente si un comando falla
set -e

echo "--- 1. Construyendo el proyecto con SAM ---"
# SAM instalará dependencias, compilará y preparará los artefactos
sam build

echo "--- 2. Ejecutando Tests Unitarios e Integración con Pytest ---"
# ¡CRÍTICO! No desplegamos si los tests fallan.
# Asumimos que tienes configurado el entorno virtual de Poetry
poetry run pytest

echo "--- 3. Desplegando a AWS con SAM ---"
# Usamos la configuración de samconfig.toml.
# El flag --no-confirm-changeset es útil para pipelines totalmente automatizados,
# pero para empezar, lo dejaremos para que confirmes manualmente.
sam deploy

echo "--- ¡Despliegue completado con éxito! ---"