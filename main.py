import sys
import logging.config
from PySide6.QtWidgets import QApplication, QMessageBox
# from qt_material import apply_stylesheet
from window.merge_window import MergeWindow


def handle_exception(exc_type, exc_value, exc_traceback):
    """异常处理函数"""
    message = f"发生了一个{exc_type.__name__}类型的错误.\n{exc_value}"
    QMessageBox.critical(None, "错误", message)


# 程序入口
if __name__ == '__main__':
    # 加载日志配置
    logging.config.fileConfig('log/logging_config.ini')
    # 处理异常
    sys.excepthook = handle_exception
    app = QApplication(sys.argv)
    # apply_stylesheet(app, theme='my_theme.xml')
    win = MergeWindow()
    win.show()
    sys.exit(app.exec())
