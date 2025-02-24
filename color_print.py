from colorama import Fore, Style, init

# 初始化 Colorama
init(autoreset=True)


class TestClass:
    def __str__(self):
        return "TestClass instance as string"

    def __repr__(self):
        return "TestClass instance as repr"


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
def yellow_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.YELLOW + response, **kwargs)


@valid_str
def red_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.RED + response, **kwargs)


@valid_str
def green_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.GREEN + response, **kwargs)


@valid_str
def blue_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.BLUE + response, **kwargs)


@valid_str
def magenta_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.MAGENTA + response, **kwargs)


@valid_str
def cyan_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.CYAN + response, **kwargs)


@valid_str
def white_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.WHITE + response, **kwargs)


@valid_str
def black_print(response, **kwargs):
    print(Style.RESET_ALL + Fore.BLACK + response, **kwargs)


@valid_str
def bright_red_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.RED + response, **kwargs)


@valid_str
def bright_green_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + response, **kwargs)


@valid_str
def bright_blue_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.BLUE + response, **kwargs)


@valid_str
def bright_yellow_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW + response, **kwargs)


@valid_str
def bright_magenta_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.MAGENTA + response, **kwargs)


@valid_str
def bright_cyan_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + response, **kwargs)


@valid_str
def bright_white_print(response, **kwargs):
    print(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + response, **kwargs)


@valid_str
def dim_red_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.RED + response, **kwargs)


@valid_str
def dim_green_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.GREEN + response, **kwargs)


@valid_str
def dim_blue_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.BLUE + response, **kwargs)


@valid_str
def dim_yellow_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.YELLOW + response, **kwargs)


@valid_str
def dim_magenta_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.MAGENTA + response, **kwargs)


@valid_str
def dim_cyan_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.CYAN + response, **kwargs)


@valid_str
def dim_white_print(response, **kwargs):
    print(Style.RESET_ALL + Style.DIM + Fore.WHITE + response, **kwargs)


if __name__ == "__main__":
    # test
    a = TestClass()

    yellow_print(1.4, a, sep="--", flush=True, end="***")
    bright_blue_print(1.4, a, sep="\n", flush=True, end="\n")
    dim_cyan_print(1.4, a, sep="--", flush=True, end="***\n")
    bright_red_print(1.4, a, sep="--", flush=True, end="***\n")
    red_print(1.4, a, sep="--", flush=True, end="***\n")
    dim_red_print(1.4, a, sep="--", flush=True, end="***\n")

