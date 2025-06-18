def custom_logger(level, message):
    import logging
    logger = logging.getLogger(__name__)
    if not len(logger.handlers):
        logging.basicConfig(level=logging.INFO)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler("file.log")
        formatt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        c_handler.setFormatter(formatt)
        f_handler.setFormatter(formatt)
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
    
    if level == 'debug':
        logger.debug(message)
    
    elif level == 'info':
        logger.info(message)
    
    elif level == 'warning':
        logger.warning(message)
    
    elif level == 'error':
        logger.error(message)
    
    elif level == 'critical':
        logger.critical(message)

custom_logger('error', 'Atencao, parametro errado')