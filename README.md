
# Colorful Prints - 终端彩色输出工具

![PyPI Version](https://img.shields.io/pypi/v/colorful_prints?style=flat-square) ![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)

一个基于 [rich](https://github.com/Textualize/rich) 的终端彩色打印工具集，提供多达 40 种预设颜色样式，支持语义化日志输出（危险/成功/警告/信息）。

## 主要特性

- 🌈 **20+ 预设颜色样式**：支持基础色、亮色、暗色等多种组合
- 🛡 **类型安全校验**：自动验证输入参数合法性
- 📦 **语义化日志**：danger/success/warning/info 四种语义级别
- 🖨 **完全兼容原生print**：支持 sep/end/file/flush 等标准参数

## 安装

```bash
pip install colorful-prints
```

**要求：** Python 3.8+，需要安装 [rich](https://pypi.org/project/rich/) 库

## 快速开始


```python
from colorful_prints import (
    danger, success, info, warning,
    bright_cyan_print, dim_green_print
)

# 语义化打印
danger("系统发生严重错误!")
success("数据保存成功!")
info("建议使用最新版本")
warning("内存占用超过阈值")

# 基础颜色打印
bright_cyan_print("这是亮青色文本")
dim_green_print("这是暗绿色文本")
```
![](./image/quick_start.png)
## 颜色样式参考

### 基础颜色

| 方法              | 示例         |
| ----------------- | ------------ |
| `red_print()`     | 🔴 红色文本   |
| `green_print()`   | 🟢 绿色文本   |
| `blue_print()`    | 🔵 蓝色文本   |
| `yellow_print()`  | 🟡 黄色文本   |
| `magenta_print()` | 🟣 品红色文本 |
| `cyan_print()`    | 🌊 青色文本   |

### 亮色系列


```python
bright_red_print("高亮红")    # 🔥 明亮红色
bright_green_print("高亮绿")  # 🌿 鲜明绿色
bright_blue_print("高亮蓝")   # 💧 明亮蓝色
```
![](./image/bright.png)
### 暗色系列


```python
dim_red_print("暗红")     # 🩸 深红色
dim_green_print("暗绿")   # 🫒 橄榄绿
dim_blue_print("暗蓝")    # 🌌 深夜蓝
```
![](./image/dim.png)
## 高级用法

### 类型安全验证

自动将参数转换为字符串，支持任何实现 `__str__` 方法的对象：


```python
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"用户: {self.name}"

user = User("Alice")
success(user)  # ✅ 自动调用 str(user)
```
![](./image/type_safe.png)
### 原生参数支持

完美兼容标准 print 函数参数：


```python
bright_yellow_print(
    "姓名", "张三",
    sep=": ",       # 使用冒号分隔
    end="!\n",      # 自定义结束符
    file=open('log.txt', 'a')  # 写入文件
)
```
![](./image/print.png)
## 项目结构

```
colorful_prints/
├── setup.py                  # 打包配置
└── colorful_prints/
    ├── __init__.py           # 模块初始化
    ├── colorful_prints.py    # 核心打印方法实现
    ├── utils.py              # 装饰器和校验逻辑
    └── test_print.py         # 示例测试类
```


## 许可协议

[MIT License](LICENSE)

---

⭐ **提示：**
- 使用前请确保终端支持 ANSI 颜色转义
- 内置类型校验装饰器会自动转换非字符串参数
- 通过 `file` 参数可将彩色文本保存到文件
- 亮色使用 `bold` 样式实现，暗色使用 `dim` 样式实现
