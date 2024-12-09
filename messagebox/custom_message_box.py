from qfluentwidgets import MessageBox


def popCustomMessageBox(title, content, src):
    mb = MessageBox(title, content, src)
    mb.yesButton.setText("确认")
    mb.cancelButton.hide()
    mb.buttonLayout.insertStretch(1)
    mb.exec()
