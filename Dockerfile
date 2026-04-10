# 1. Usamos la imagen base de AWS para Python 3.11
FROM public.ecr.aws/lambda/python:3.11

# 2. Instalamos Poetry
RUN pip install poetry

# 3. Copiamos los archivos de configuración de dependencias
# LAMBDA_TASK_ROOT es /var/task por defecto en estas imágenes
COPY pyproject.toml poetry.lock ${LAMBDA_TASK_ROOT}/

# 4. Instalamos dependencias (sin crear entorno virtual, ya estamos en un contenedor)
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

# 5. Copiamos el código fuente
COPY src/ ${LAMBDA_TASK_ROOT}/src/

# 6. El CMD se sobreescribirá en el template.yaml para cada función
CMD [ "src.handlers.validator.handler" ]