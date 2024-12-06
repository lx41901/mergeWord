# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge_win_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from qfluentwidgets import (LineEdit, PushButton, ToolButton)

class Ui_MergeWindow(object):
    def setupUi(self, MergeWindow):
        if not MergeWindow.objectName():
            MergeWindow.setObjectName(u"MergeWindow")
        MergeWindow.setWindowModality(Qt.NonModal)
        MergeWindow.resize(600, 230)
        MergeWindow.setMinimumSize(QSize(600, 230))
        MergeWindow.setMaximumSize(QSize(600, 230))
        self.centralwidget = QWidget(MergeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.content_layout = QVBoxLayout()
        self.content_layout.setObjectName(u"content_layout")
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(60, 30))
        self.input_label.setMaximumSize(QSize(600, 30))
        font = QFont()
        font.setPointSize(12)
        self.input_label.setFont(font)
        self.input_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.content_layout.addWidget(self.input_label)

        self.input_layout = QHBoxLayout()
        self.input_layout.setObjectName(u"input_layout")
        self.input_dir_edit = LineEdit(self.centralwidget)
        self.input_dir_edit.setObjectName(u"input_dir_edit")
        self.input_dir_edit.setMinimumSize(QSize(300, 30))
        self.input_dir_edit.setReadOnly(True)

        self.input_layout.addWidget(self.input_dir_edit)

        self.select_input_dir_button = ToolButton(self.centralwidget)
        self.select_input_dir_button.setObjectName(u"select_input_dir_button")
        self.select_input_dir_button.setMinimumSize(QSize(60, 30))

        self.input_layout.addWidget(self.select_input_dir_button)


        self.content_layout.addLayout(self.input_layout)

        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setMinimumSize(QSize(60, 30))
        self.output_label.setMaximumSize(QSize(600, 30))
        self.output_label.setFont(font)
        self.output_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.output_label.setMargin(0)

        self.content_layout.addWidget(self.output_label)

        self.output_layout = QHBoxLayout()
        self.output_layout.setObjectName(u"output_layout")
        self.output_dir_edit = LineEdit(self.centralwidget)
        self.output_dir_edit.setObjectName(u"output_dir_edit")
        self.output_dir_edit.setMinimumSize(QSize(60, 30))
        self.output_dir_edit.setReadOnly(True)

        self.output_layout.addWidget(self.output_dir_edit)


        self.content_layout.addLayout(self.output_layout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.content_layout.addItem(self.verticalSpacer)

        self.merge_button = PushButton(self.centralwidget)
        self.merge_button.setObjectName(u"merge_button")
        self.merge_button.setMinimumSize(QSize(100, 30))
        self.merge_button.setFont(font)

        self.content_layout.addWidget(self.merge_button)


        self.gridLayout.addLayout(self.content_layout, 0, 0, 1, 1)

        MergeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MergeWindow)
        self.select_input_dir_button.clicked.connect(MergeWindow.selectDir)
        self.merge_button.clicked.connect(MergeWindow.doMerge)

        QMetaObject.connectSlotsByName(MergeWindow)
    # setupUi

    def retranslateUi(self, MergeWindow):
        MergeWindow.setWindowTitle(QCoreApplication.translate("MergeWindow", u"word\u6587\u6863\u5408\u5e76", None))
        self.input_label.setText(QCoreApplication.translate("MergeWindow", u"\u5f85\u5408\u5e76word\u6587\u6863\u6240\u5728\u76ee\u5f55:", None))
        self.select_input_dir_button.setText(QCoreApplication.translate("MergeWindow", u"...", None))
        self.output_label.setText(QCoreApplication.translate("MergeWindow", u"\u5408\u5e76\u540eword\u6587\u6863\u8f93\u51fa\u76ee\u5f55:", None))
        self.merge_button.setText(QCoreApplication.translate("MergeWindow", u"\u5408\u5e76", None))
    # retranslateUi

