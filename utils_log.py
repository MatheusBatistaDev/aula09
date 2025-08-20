from loguru import logger
from sys import stderr
from functools import wraps

# Remove o handler padrão (console)
logger.remove()

logger = logger.bind(username="Matheus")

# Handler para logs gerais (INFO e acima) em arquivo
logger.add(
    "meu_arquivo_de_logs.log",
    format="{time} | {level} | {message} | {file} | {extra[username]}",
    level="INFO",
    rotation="10 MB",  # opcional: cria novo arquivo após 10MB
    retention="7 days",  # opcional: mantém logs por 7 dias
    compression="zip"  # opcional: comprime logs antigos
)

# Handler para logs críticos/erros em arquivo separado
logger.add(
    "meu_arquivo_de_logs_critical.log",
    format="{time} | {level} | {message} | {file} | {extra[username]}",
    level="ERROR",
    rotation="5 MB",
    retention="7 days",
    compression="zip"
)

# Handler para console
logger.add(
    stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
    level="INFO"
)

# Decorador de logs
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args={args} e kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception:
            logger.exception(f"Exceção capturada em '{func.__name__}'")
            raise
    return wrapper

# --- TESTE ---
@log_decorator
def soma(a, b):
    return a + b

@log_decorator
def erro():
    raise ValueError("Ops! Algo deu errado.")

if __name__ == "__main__":
    soma(10, 20)
    # erro()  # descomente para testar exceção
