# 🚀 User Management Cloud-Native Microservice

Este proyecto es un microservicio **Serverless** diseñado para la gestión de usuarios en entornos de nube (AWS). Utiliza una arquitectura desacoplada, validación de datos estricta y contenedores para garantizar la consistencia entre entornos de desarrollo y producción.

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.11+
- **Validación:** Pydantic V2 (Esquemas de datos estrictos)
- **Base de Datos:** Amazon DynamoDB (NoSQL Serverless)
- **Orquestación:** AWS Step Functions & AWS SAM
- **Infraestructura:** Docker (Lambda Container Image)
- **Testing:** Pytest & Moto (Mocking de AWS en memoria)

## 🏗️ Arquitectura y Buenas Prácticas

El microservicio sigue los principios de **Clean Architecture** y **SOLID**:

1. **Capa de Dominio (`src/models/`)**: Definición de contratos de datos mediante Pydantic.
2. **Capa de Aplicación (`src/handlers/`)**: Orquestadores de entrada (AWS Lambda) que gestionan el flujo del evento.
3. **Capa de Infraestructura (`src/services/`)**: Implementación del **Repository Pattern** para desacoplar el negocio del SDK de AWS (`boto3`).

---

## 🧪 Calidad y Testing

El proyecto cuenta con una cobertura de pruebas completa que simula el entorno de AWS sin incurrir en costes, utilizando **Moto**.

Bash

```
# Ejecutar pruebas unitarias e integración
poetry run pytest
```

---

## 📦 Ejecución Local con Docker

Para garantizar que el microservicio funcione en cualquier entorno, hemos empaquetado la lógica en una imagen compatible con **AWS Lambda RIE (Runtime Interface Emulator)**.

### 1. Construir la imagen

Bash

```
docker build -t user-microservice:local .
```

### 2. Ejecutar el contenedor

Bash

```
docker run -p 8080:8080 -e USE_AWS_MOCK=true user-microservice:local
```

### 3. Probar el endpoint (Validator)

Usa el siguiente comando en tu terminal para simular una invocación de AWS:

**PowerShell**

`Prueba de un registro valido`
```
curl.exe -X POST "http://localhost:8080/2015-03-31/functions/function/invocations" `
-d '{\"username\": \"user_test\", \"email\": \"test@example.com\", \"edad\": 25}'
```

`Prueba de un registro con minoria de edad`

```
curl.exe -X POST "http://localhost:8080/2015-03-31/functions/function/invocations" `
-d '{\"username\": \"junior\", \"email\": \"niño@test.com\", \"edad\": 15}'
```

`Prueba de un registro con formato de correo erroneo`

```
curl.exe -X POST "http://localhost:8080/2015-03-31/functions/function/invocations" `
-d '{\"username\": \"user1\", \"email\": \"not-an-email\", \"edad\": 20}'
```

---

## ☁️ Despliegue en AWS (CI/CD)

El despliegue está automatizado mediante **AWS SAM**. El flujo de trabajo recomendado es:

1. `sam build`: Construye las imágenes de Docker.
2. `sam deploy`: Crea la tabla de DynamoDB, registra las imágenes en ECR y configura la **State Machine** de Step Functions.

---

## 📝 Decisiones de Diseño

- **¿Por qué Step Functions?** Para delegar la lógica de reintentos y manejo de errores a la infraestructura de AWS, reduciendo la complejidad del código Python y ahorrando costes de computación.
- **¿Por qué Docker?** Para eliminar el problema de "en mi máquina funciona", asegurando que las dependencias de Python sean idénticas en local y en la nube.
- **¿Por qué Pydantic?** Para actuar como un "Guardrail" legal y técnico, impidiendo que datos corruptos o menores de edad lleguen a la base de datos.

---

## 👨‍💻 Autor

**LACN** - Cloud & Backend Developer