import subprocess
from pathlib import Path
from sys import exit
from typing import Sequence

import click
from aiohttp.web import Application, run_app

from melody.web.constants import (
    DEFAULT_HOST,
    DEFAULT_INPUT,
    DEFAULT_NAME,
    DEFAULT_OUTPUT,
    DEFAULT_PORT,
    ROOT,
)
from melody.web.core import setup_app

EXECUTE = "npx"
TAILWIND = "tailwindcss"
INPUT = "-i"
OUTPUT = "-o"
MINIFY = "--minify"
WATCH = "--watch"


def build_command(input: Path, output: Path, watch: bool) -> Sequence[str]:
    arguments = [EXECUTE, TAILWIND, INPUT, input.as_posix(), OUTPUT, output.as_posix(), MINIFY]

    if watch:
        arguments.append(WATCH)

    return arguments


@click.group(name=DEFAULT_NAME)
def web() -> None:
    pass


@click.option("--host", "-h", type=str, default=DEFAULT_HOST)
@click.option("--port", "-p", type=int, default=DEFAULT_PORT)
@web.command()
def run(host: str, port: int) -> None:
    try:
        create_and_run_app(host, port)

    except KeyboardInterrupt:
        pass


def create_and_run_app(host: str, port: int) -> None:
    app = Application()

    setup_app(app)

    run_app(app, host=host, port=port)


@click.option("--input", "-i", type=Path, default=DEFAULT_INPUT)
@click.option("--output", "-o", type=Path, default=DEFAULT_OUTPUT)
@click.option("--watch", "-w", is_flag=True, default=False)
@web.command()
def build(input: Path, output: Path, watch: bool) -> None:
    exit(
        subprocess.call(build_command(input, output, watch=watch), cwd=ROOT.as_posix(), shell=True)
    )
