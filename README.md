## mergeWord-合并word文档工具

---
需要安装 PySide6、docxcompose、PySide6-Fluent-Widgets，输入以下代码安装依赖：
```
pip install docxcompose -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install PySide6-Fluent-Widgets -i https://pypi.org/simple/
```
可能需要额外安装以下依赖：
```
pip install PySideSix-Frameless-Window
```
---
添加QtDesigner（仅打开QtDesigner）：
Settings—> Tools —> External Tools 中点击 + 号，添加外部工具。</br>
配置以下信息：
```
Name: QTDesigner
Group: PySide6
Program: D:\python\anaconda\envs\py311\Lib\site-packages\PySide6\designer.exe （自己安装的python路径）
Arguments: 空
Working directory: $ProjectFileDir$ 
```
添加QtDesignerEdit（打开QtDesigner，并直接编辑当前ui文件）：
Settings—> Tools —> External Tools 中点击 + 号，添加外部工具。</br>
配置以下信息：
```
Name: QtDesignerEdit
Group: PySide6
Program: D:\python\anaconda\envs\py311\Lib\site-packages\PySide6\designer.exe （自己安装的python路径）
Arguments: $FileName$
Working directory: $FileDir$ 
```
添加PyUIC（将ui文件转换为py文件）：
Settings—> Tools —> External Tools 中点击 + 号，添加外部工具。</br>
配置以下信息：
```
Name: PyUIC
Group: PySide6
Program: D:\python\anaconda\envs\py311\Scripts\pyside6-uic.exe （自己安装的python路径）
Arguments: $FileName$ -o $FileNameWithoutExtension$.py
Working directory: $FileDir$ 
```
