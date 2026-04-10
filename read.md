mi-proyecto-serverless/
├── pyproject.toml              # Gestión de dependencias de Python (Poetry)
├── src/                        # TU CÓDIGO (Ya lo tenemos)
│   ├── handlers/               # Funciones Lambda (Validadora, Escritora)
│   ├── models/                 # Modelos Pydantic
│   └── services/               # UserRepository (Lógica de base de datos)
├── tests/                      # TUS TESTS (Pytest + Moto, ¡Ya pasan!)
├── iac/                        # INFRAESTRUCTURA COMO CÓDIGO (¡NUEVO!)
│   ├── template.yaml           # Definición de AWS SAM o CDK (elegiremos uno)
│   └── state_machine.json      # Definición ASL de tu Step Function
├── deployment/                 # SCRIPTS DE DESPLIEGUE (¡NUEVO!)
│   └── deploy.sh               # Un script para automatizar el comando de despliegue
└── README.md                   # Documentación clara