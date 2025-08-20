from loguru import logger

logger.debug("Um aviso para o desenvolvedor: este é um exemplo de log de depuração.")
logger.info("Este é um log informativo, útil para entender o fluxo do programa.")
logger.warning("Cuidado! Algo pode não estar certo, mas o programa ainda está funcionando.")
logger.error("Ocorreu um erro, mas o programa pode continuar rodando.")
logger.critical("Um erro crítico ocorreu! O programa pode não funcionar corretamente a partir daqui.")

