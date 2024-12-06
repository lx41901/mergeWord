## mergeWord-合并word文档工具

---
需要额外安装 win32com、docx、docxcompose，输入以下代码安装：
```
pip install pywin32
pip install python-docx
pip install docxcompose
pip install pyqt6
pip install pyqt6-tools
```
---
添加Qt Designer：
Settings—> Tools —> External Tools 中点击 + 号，添加外部工具。</br>
配置以下信息：
```
Name: "QT Designer"，这个名字可以随意填
Group: "PyQt6"
Program: "D:\xxx\Python\Python39\Scripts\pyqt6-tools.exe" (自己安装的python路径)
Arguments: "designer"
Working directory: $FileDir$ 
```

