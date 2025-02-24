from rich import print
from typing import Any, IO, Sequence
from .utils import valid_str

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
    "bright_black_print",
    "bright_white_print",
    "dim_red_print",
    "dim_green_print",
    "dim_blue_print",
    "dim_yellow_print",
    "dim_magenta_print",
    "dim_cyan_print",
    "dim_white_print",
    "dim_black_print",
    "danger",
    "success",
    "info",
    "warning",
]


@valid_str
def danger(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bold red` formatting, often used to indicate danger or errors.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[bold red]{response}[/bold red]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def success(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `green` formatting, often used to indicate success.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[green]{response}[/green]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def warning(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `yellow` formatting, often used to indicate warnings.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[yellow]{response}[/yellow]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def info(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `blue` formatting, often used to provide informational messages.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[blue]{response}[/blue]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def yellow_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `yellow` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[yellow]{response}[/yellow]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def red_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `red` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[red]{response}[/red]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def green_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `green` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[green]{response}[/green]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def blue_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `blue` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[blue]{response}[/blue]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def magenta_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `magenta` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[magenta]{response}[/magenta]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def cyan_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `cyan` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[cyan]{response}[/cyan]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def white_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `white` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[white]{response}[/white]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def black_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `black` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[black]{response}[/black]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def bright_black_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright black` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold black]{response}[/bold black]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def bright_red_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright red` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[bold red]{response}[/bold red]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def bright_green_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright green` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold green]{response}[/bold green]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def bright_blue_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright blue` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold blue]{response}[/bold blue]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def bright_yellow_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright yellow` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold yellow]{response}[/bold yellow]",
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )


@valid_str
def bright_magenta_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright magenta` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold magenta]{response}[/bold magenta]",
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )


@valid_str
def bright_cyan_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright cyan` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold cyan]{response}[/bold cyan]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def bright_white_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `bright white` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[bold white]{response}[/bold white]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def dim_black_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim black` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[dim black]{response}[/dim black]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def dim_red_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim red` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[dim red]{response}[/dim red]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def dim_green_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim green` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[dim green]{response}[/dim green]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def dim_blue_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim blue` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[dim blue]{response}[/dim blue]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def dim_yellow_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim yellow` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[dim yellow]{response}[/dim yellow]", sep=sep, end=end, file=file, flush=flush
    )


@valid_str
def dim_magenta_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim magenta` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[dim magenta]{response}[/dim magenta]",
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )


@valid_str
def dim_cyan_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim cyan` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(f"[dim cyan]{response}[/dim cyan]", sep=sep, end=end, file=file, flush=flush)


@valid_str
def dim_white_print(
    response: Any | Sequence[Any],
    sep: str = " ",
    end: str = "\n",
    file: IO[str] | None = None,
    flush: bool = False,
) -> None:
    """Prints the given `response` to the console with `dim white` formatting.

    Args:
        response: The object(s) to be printed. Can be a single object or a sequence of objects.
        sep:  String inserted between values, default ' '.
        end:  String appended after the last value, default '\\n'.
        file: A file-like object (stream); defaults to the current sys.stdout.
        flush: Whether to forcibly flush the stream.
    """
    print(
        f"[dim white]{response}[/dim white]", sep=sep, end=end, file=file, flush=flush
    )



