import logging
from datetime import datetime
import os


def setup_loger(logger_name, log_level, base_log_dir):
    """
    创建并配置一个日志记录器，将日志输出到文件和控制台。

    参数:
        - logger_name (str): 日志记录器的名称。
        - file_path (str): 日志文件路径。
        - log_level (int): 日志级别，默认为 logging.INFO。

    返回:
        - logging.Logger: 配置好的日志记录器。
    """
    # 创建日志记录器
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(base_log_dir, exist_ok=True)
    # log_file_path = os.path.join(base_log_dir, f"{timestamp}.log")
    log_file_path = os.path.join(base_log_dir, ".log")

    # 定义日志格式器，用于统一控制日志输出格式
    # 日志记录时间，格式如 '2025-06-17 00:01:35,123'
    # 日志级别名（INFO、DEBUG 等），右对齐，占8字符宽度
    # 触发日志的源文件名，右对齐，占15字符宽度
    # 日志调用位置的源代码行号，占4字符宽度
    # 日志主体内容，由用户传入
    formatter = logging.Formatter(
        "[{asctime}][{name}][{filename:^15}][line:{lineno:^4}][{levelname:^8}] {message}",
        datefmt="%Y/%m/%d %H:%M:%S",
        style='{'
    )

    # formatter = logging.Formatter(
    #     "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #     datefmt="%Y/%m/%d %H:%M:%S",
    # )

    # 创建文件处理器
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


if __name__ == '__main__':
    print(getattr(logging, "INFO"))  # 20
    print(logging.INFO)  # 20
    logger = setup_loger(
        "h-tq",
        logging.INFO,
        "../test/log"
    )
    logger.info("This is a info test.")
    logger.info("This is a info test1.")
    logger.info("This is a info test3.")
    logger.debug("This is a debug test.")
    logger.warning("This is a warning test.")
