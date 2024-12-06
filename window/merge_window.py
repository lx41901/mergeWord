from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import MessageBox

from merge.do_merge import MergeThread
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
        print("执行doMerge了")
        input_dir = self.input_dir_edit.text()
        logger.info("待合并路径:" + input_dir)
        if len(input_dir) == 0:
            mb = MessageBox("错误", "未选择待合并文件所在的文件夹", self)
            mb.yesButton.setText("确认")
            mb.cancelButton.hide()
            mb.buttonLayout.insertStretch(1)
            mb.exec()
            return

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
        mb = MessageBox("结果", resultMsg, self)
        mb.yesButton.setText("确认")
        mb.cancelButton.hide()
        mb.buttonLayout.insertStretch(1)
        mb.exec()
