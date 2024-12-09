import sys
import logging.config

from PySide6.QtWidgets import QApplication

from log.logging_config import LOGGING_CONFIG
from messagebox.custom_message_box import popCustomMessageBox
from window.merge_window import MergeWindow

logger = logging.getLogger()

main_win = None


def handle_exception(exc_type, exc_value, exc_traceback):
    """异常处理函数"""
    message = f"错误类型: {exc_type.__name__}\n错误描述: {exc_value}\n错误堆栈: {exc_traceback}\n"
    logger.exception(message[0:50])
    popCustomMessageBox("错误", message, main_win)


# 程序入口
if __name__ == '__main__':
    # 处理异常
    sys.excepthook = handle_exception
    # 加载日志配置
    logging.config.dictConfig(LOGGING_CONFIG)
    app = QApplication(sys.argv)
    win = MergeWindow()
    main_win = win
    win.show()
    sys.exit(app.exec())
