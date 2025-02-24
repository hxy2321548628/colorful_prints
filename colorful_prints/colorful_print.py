from rich import print

__all__ = [
    "yellow_print",
    "red_print",
    "green_print",
    "blue_print",
    "magenta_print",
    "cyan_print",
    "white_print",
    "black_print",
    "bright_red_print",
    "bright_green_print",
    "bright_blue_print",
    "bright_yellow_print",
    "bright_magenta_print",
    "bright_cyan_print",
    "bright_white_print",
    "dim_red_print",
    "dim_green_print",
    "dim_blue_print",
    "dim_yellow_print",
    "dim_magenta_print",
    "dim_cyan_print",
    "dim_white_print",
    "danger",
    "success",
    "info",
    "warning"
]
# # 初始化 可以自定义 theme
# custom_theme = Theme(
#    /e =  {
#         "info": "blue",
#         "warning": "yellow",
#         "danger": "bold red",
#         "success": "green",
#         "yellow": "yellow",
#         "red": "red",
#         "green": "green",
#         "blue": "blue",
#         "magenta": "magenta",
#         "cyan": "cyan",
#         "white": "white",
#         "black": "black",
#         "bright_red": "bold red",
#         "bright_green": "bold green",
#         "bright_blue": "bold blue",
#         "bright_yellow": "bold yellow",
#         "bright_magenta": "bold magenta",
#         "bright_cyan": "bold cyan",
#         "bright_white": "bold white",
#         "dim_red": "dim red",
#         "dim_green": "dim green",
#         "dim_blue": "dim blue",
#         "dim_yellow": "dim yellow",
#         "dim_magenta": "dim magenta",
#         "dim_cyan": "dim cyan",
#         "dim_white": "dim white",
#     }
# )


def valid_str(func):
    def wrapper(*args, **kwargs):
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
        response = format_str(*converted_args, sep=sep)
        return func(response, **kwargs)  # 传递转换后的参数

    return wrapper


def format_str(*args, sep=" "):
    return sep.join(args)


@valid_str
def danger(response, **kwargs):
    print(f"[bold red]{response}[/bold red]", **kwargs)


@valid_str
def success(response, **kwargs):
    print(f"[green]{response}[/green]", **kwargs)


@valid_str
def warning(response, **kwargs):
    print(f"[yellow]{response}[/yellow]", **kwargs)


@valid_str
def info(response, **kwargs):
    print(f"[blue]{response}[/blue]", **kwargs)


@valid_str
def yellow_print(response, **kwargs):
    print(f"[yellow]{response}[/yellow]", **kwargs)


@valid_str
def red_print(response, **kwargs):
    print(f"[red]{response}[/red]", **kwargs)


@valid_str
def green_print(response, **kwargs):
    print(f"[green]{response}[/green]", **kwargs)


@valid_str
def blue_print(response, **kwargs):
    print(f"[blue]{response}[/blue]", **kwargs)


@valid_str
def magenta_print(response, **kwargs):
    print(f"[magenta]{response}[/magenta]", **kwargs)


@valid_str
def cyan_print(response, **kwargs):
    print(f"[cyan]{response}[/cyan]", **kwargs)


@valid_str
def white_print(response, **kwargs):
    print(f"[white]{response}[/white]", **kwargs)


@valid_str
def black_print(response, **kwargs):
    print(f"[black]{response}[/black]", **kwargs)


@valid_str
def bright_red_print(response, **kwargs):
    print(f"[bright_red]{response}[/bright_red]", **kwargs)


@valid_str
def bright_green_print(response, **kwargs):
    print(f"[bright_green]{response}[/bright_green]", **kwargs)


@valid_str
def bright_blue_print(response, **kwargs):
    print(f"[bright_blue]{response}[/bright_blue]", **kwargs)


@valid_str
def bright_yellow_print(response, **kwargs):
    print(f"[bright_yellow]{response}[/bright_yellow]", **kwargs)


@valid_str
def bright_magenta_print(response, **kwargs):
    print(f"[bright_magenta]{response}[/bright_magenta]", **kwargs)


@valid_str
def bright_cyan_print(response, **kwargs):
    print(f"[bright_cyan]{response}[/bright_cyan]", **kwargs)


@valid_str
def bright_white_print(response, **kwargs):
    print(f"[bright_white]{response}[/bright_white]", **kwargs)


@valid_str
def dim_red_print(response, **kwargs):
    print(f"[dim_red]{response}[/dim_red]", **kwargs)


@valid_str
def dim_green_print(response, **kwargs):
    print(f"[dim_green]{response}[/dim_green]", **kwargs)


@valid_str
def dim_blue_print(response, **kwargs):
    print(f"[dim_blue]{response}[/dim_blue]", **kwargs)


@valid_str
def dim_yellow_print(response, **kwargs):
    print(f"[dim_yellow]{response}[/dim_yellow]", **kwargs)


@valid_str
def dim_magenta_print(response, **kwargs):
    print(f"[dim_magenta]{response}[/dim_magenta]", **kwargs)


@valid_str
def dim_cyan_print(response, **kwargs):
    print(f"[dim_cyan]{response}[/dim_cyan]", **kwargs)


@valid_str
def dim_white_print(response, **kwargs):
    print(f"[dim_white]{response}[/dim_white]", **kwargs)


if __name__ == "__main__":
    # test
    from test_print import TestClass

    a = TestClass()

    danger("danger", sep="--",)
    warning("warning", sep="--")
    success("success", sep="--")
    info("info", sep="--")
    yellow_print("yellow")
    print("[yellow]hello world[/yellow]")
    # bright_blue_print(1.4, a, sep="\n", end="\n")
    # dim_cyan_print(1.4, a, sep="--", end="***\n")
    # bright_red_print(1.4, a, sep="--", end="***\n")
    # red_print(1.4, a, sep="--", end="***\n")
    # dim_red_print(1.4, a, sep="--", end="***\n")
