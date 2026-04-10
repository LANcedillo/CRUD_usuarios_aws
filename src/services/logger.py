import logging
import json
import sys

# Configuramos el logger para que imprima en una sola línea (ideal para CloudWatch)
logger = logging.getLogger("user-microservice")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_event(message, extra=None):
    # Los logs en la nube deben ser JSON para que herramientas como CloudWatch Insights puedan leerlos
    log_data = {"message": message}
    if extra:
        log_data.update(extra)
    logger.info(json.dumps(log_data))

def log_structured(level, message, extra=None):
    payload = {
        "level": level,
        "message": message,
        "service": "user-service"
    }
    if extra:
        payload.update(extra)
    
    if level == "INFO":
        logger.info(json.dumps(payload))
    elif level == "ERROR":
        logger.error(json.dumps(payload))