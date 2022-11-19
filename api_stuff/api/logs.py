import logging
import hosts_holder


def init_logger():
    hosts_holder.logger = logging.getLogger()
    l_format = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(message)s')
    l_handler = logging.FileHandler('logger.log')
    l_handler.setFormatter(l_format)
    l_handler.setLevel(logging.INFO)
    hosts_holder.logger.addHandler(l_handler)


def save_log_info(msg):
    hosts_holder.logger.warning(msg=str(msg))


def save_log_error(msg):
    hosts_holder.logger.error(msg=str(msg))


def save_log_critical(msg):
    hosts_holder.logger.critical(msg=str(msg))
