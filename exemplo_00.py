from loguru import logger

logger.add("meu_app.log")

def soma(x, y):
    logger.info(f"x: {x}")
    logger.info(f"y: {y}")
    resultado = x + y
    logger.info(f"Resultado da soma: {resultado}")
    return resultado

soma(2, 3)
