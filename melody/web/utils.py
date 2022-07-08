__all__ = ("check_back", "identifier")

IDENTIFIER = r"[A-Za-z0-9_\.\-]+"
BACK = ".."

ARGUMENT = "{{{}:{}}}"


def identifier(name: str) -> str:
    return ARGUMENT.format(name, IDENTIFIER)


def check_back(string: str) -> bool:
    return BACK in string
