from PySide6.QtWidgets import QFileDialog, QMainWindow

from merge.do_merge import MergeThread
from messagebox.custom_message_box import popCustomMessageBox
from ui.merge_win_ui import *
import logging
import os

from window.loading_dialog import LoadingDialog

logger = logging.getLogger()


class MergeWindow(QMainWindow, Ui_MergeWindow):

    def __init__(self, parent=None):
        super(MergeWindow, self).__init__(parent)
        self.setupUi(self)
        # 获取当前工作目录路径
        current_path = os.getcwd()
        self.output_dir_edit.setText(current_path)

    def selectDir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择目录", "C:/", QFileDialog.Option.ShowDirsOnly)
        if dir_path:
            self.input_dir_edit.setText(dir_path)

    def doMerge(self):
        input_dir = self.input_dir_edit.text()
        if len(input_dir) == 0:
            logger.warning("提示: 未选择待合并文件所在的文件夹")
            popCustomMessageBox("提示", "未选择待合并文件所在的文件夹", self)
            return

        logger.info("待合并路径:" + input_dir)

        self.loading = LoadingDialog(self)
        self.loading.show()
        self.merge_button.setText("合并中...")
        self.merge_button.setEnabled(False)
        self.select_input_dir_button.setEnabled(False)
        self.merge_thread = MergeThread(input_dir)
        self.merge_thread.mergeSignal.connect(self.mergeFinish)
        self.merge_thread.start()

    def mergeFinish(self, resultMsg):
        self.loading.close()
        self.merge_button.setText("合并")
        self.merge_button.setEnabled(True)
        self.select_input_dir_button.setEnabled(True)
        popCustomMessageBox("结果", resultMsg, self)
