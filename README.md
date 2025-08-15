# 便笺工具

一个类似微软便笺的简单工具，具有窗口置顶功能，可以让你的便笺始终显示在屏幕最前方。

## 功能特点

- 类似微软便笺的简洁界面
- 窗口置顶功能，始终保持在所有程序的最前端
- 基本的文本编辑功能（新建、打开、保存）
- 自动保存功能
- 右键菜单功能（复制、剪切、粘贴）
- 应用图标

## 使用方法

直接运行 [main.py](file:///C:/Users/admin/PycharmProjects/bianqian/main.py) 文件即可启动应用：

```bash
python main.py
```

或者运行打包后的可执行文件：

```bash
# 在bianqian-software目录中运行
便笺工具.exe
```

## 操作说明

- **文件菜单**：
  - 新建：创建新的便笺
  - 打开：打开已保存的便笺文件
  - 保存：保存当前便笺
  - 另存为：将便笺保存到指定位置

- **视图菜单**：
  - 窗口置顶：勾选后窗口将始终保持在最前端

- **右键菜单**：
  - 在文本区域点击右键可打开菜单
  - 当有选中文本时，可使用复制或剪切功能
  - 任何时候都可以使用粘贴功能

- **快捷键**：
  - Ctrl+N：新建便笺
  - Ctrl+O：打开便笺
  - Ctrl+S：保存便笺

## 系统要求

- Python 3.x
- Tkinter（通常随Python一起安装）

## 打包和分发

使用PyInstaller打包应用：

```bash
pyinstaller --noconfirm --onefile --windowed --icon=icons/notes_icon.ico main.py
```

## 注意事项

- 应用会自动将内容保存到 `default_note.txt` 文件中
- 关闭应用前会提示保存未保存的内容