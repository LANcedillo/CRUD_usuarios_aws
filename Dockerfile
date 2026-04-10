# 1. Imagen base oficial de AWS para Lambda
FROM public.ecr.aws/lambda/python:3.11

# 2. Variables de entorno para Poetry
ENV POETRY_VERSION=2.0.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/tmp/poetry_cache'

# 3. Instalamos Poetry
RUN pip install "poetry==$POETRY_VERSION"

# 4. Establecemos el directorio de trabajo (estándar de Lambda)
WORKDIR ${LAMBDA_TASK_ROOT}

# 5. Copiamos los archivos de dependencias primero 
COPY pyproject.toml ./

# 6. Instalamos dependencias
# Usamos --no-root porque aún no copiamos el código
RUN poetry install --only main --no-interaction --no-ansi --no-root -vvv

# 7. Ahora copiamos el código fuente
COPY src/ ./src/

# 8. Comando por defecto (puedes cambiarlo al handler que quieras probar)
CMD [ "src.handlers.validator.handler" ]