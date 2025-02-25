from typing import Callable, TypeVar, ParamSpec
from functools import wraps
from rich.console import Console

# 使用 ParamSpec 和 TypeVar 来更精确地定义装饰器的类型
P = ParamSpec("P")
R = TypeVar("R")


def valid_str(func: Callable[P, R]) -> Callable[P, R]:
    """
    装饰器，用于确保所有参数都可以转换为字符串。
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        converted_args = []
        for arg in args:
            try:
                arg = str(arg)  # 尝试转换为字符串
            except (TypeError, ValueError) as e:
                raise ValueError(
                    f"无法转换为字符串: {type(arg).__name__}, 原始值: {arg}"
                ) from e
            converted_args.append(arg)
        sep = kwargs.pop("sep", " ")  # 使用 get 避免修改 kwargs
        kwargs["_console"] = (
            kwargs.pop("_console")
            if bool(kwargs.get("_console"))
            else Console(file=kwargs.pop("file", None), force_jupyter=False)
        )
        response = format_str(*converted_args, sep=sep)
        return func(response, **kwargs)  # 传递转换后的参数

    return wrapper


def format_str(*args: str, sep: str = " ") -> str:
    """
    使用指定分隔符连接字符串。
    """
    return sep.join(args)
