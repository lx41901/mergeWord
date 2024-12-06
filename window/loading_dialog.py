# coding:utf-8
import logging
from PySide6.QtCore import Qt
from qfluentwidgets import MessageBoxBase, SubtitleLabel, IndeterminateProgressRing

logger = logging.getLogger()


class LoadingDialog(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.spinner = IndeterminateProgressRing(self)
        self.titleLabel = SubtitleLabel('合并中...', self)

        self.viewLayout.addWidget(self.spinner, 0, Qt.AlignmentFlag.AlignHCenter)
        self.viewLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget.setMinimumWidth(200)

        self.hideYesButton()
        self.hideCancelButton()

        self.buttonGroup.setFixedHeight(0)


