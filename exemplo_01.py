from loguru import logger

logger.add("meu_log.log", level="CRITICAL")

def soma(x, y):
    try:
        soma= x + y
        logger.info(f"Você digitou valores corretos, parabéns! {soma}")
        return soma
    except:
        logger.critical("Você digitou valores incorretos, tente novamente!")
        

soma(2, 3)
soma(2,7)
soma("2", 3)