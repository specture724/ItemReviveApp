# ItemReviveApp

ItemReviveApp 是一个使用 `tkinter` 构建的简单图形界面应用，允许用户添加、删除、查看和查找闲置物品信息。该程序旨在帮助用户管理和复用不再使用的物品资源。

## 功能

1. **添加物品**：用户可以输入物品名称、描述和联系人信息，将物品信息添加到列表中。
2. **删除物品**：用户可以从列表中删除指定物品。
3. **显示所有物品**：列出所有已添加的物品信息。
4. **查找物品**：按名称查找物品，列出匹配的物品信息。
5. **双击查看详情**：在列表中双击某个物品，可以弹出一个新窗口，显示该物品的详细信息（名称、描述、联系人信息）。

## 文件结构

- `ItemReviveApp.py`：主应用程序文件，包含物品管理的所有逻辑代码。
- `items.json`：数据文件，用于存储物品信息，包括名称、描述和联系人信息。

## 安装和运行

### 1. 安装Python

确保系统中已安装 Python 3.6以上版本。

### 2. 下载项目文件

将 `ItemReviveApp.py` 和 `items.json` 文件下载到同一目录。

### 3. 安装依赖库

该程序使用Python标准库中的 `tkinter` 和 `json`，无需额外安装其他依赖库。

### 4. 运行程序

在命令行中运行以下命令启动程序：

```bash
python ItemReviveApp.py
```