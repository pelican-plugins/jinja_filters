import os
from pathlib import Path
from shutil import which

from invoke import task

PKG_NAME = "jinja_filters"
PKG_PATH = Path(f"pelican/plugins/{PKG_NAME}")
BIN_DIR = "bin" if os.name != "nt" else "Scripts"
ACTIVE_VENV = os.environ.get("VIRTUAL_ENV", None)
VENV_HOME = Path(os.environ.get("WORKON_HOME", "~/virtualenvs")).expanduser()
VENV_PATH = Path(ACTIVE_VENV) if ACTIVE_VENV else (VENV_HOME / PKG_NAME)
VENV = str(VENV_PATH.expanduser())
VENV_BIN = Path(VENV) / Path(BIN_DIR)

TOOLS = ["poetry", "pre-commit"]
POETRY = which("poetry") if which("poetry") else (VENV_BIN / "poetry")
PRECOMMIT = which("pre-commit") if which("pre-commit") else (VENV_BIN / "pre-commit")
SYSTEM_PYTHON = which("python") if which("python") else None


@task
def tests(c):
    """Run the test suite"""
    c.run(f"{VENV_BIN}/pytest", pty=True)


@task
def black(c, check=False, diff=False):
    """Run Black auto-formatter, optionally with --check or --diff"""
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "--check"
    if diff:
        diff_flag = "--diff"
    c.run(f"{VENV_BIN}/black {check_flag} {diff_flag} {PKG_PATH} tasks.py")


@task
def isort(c, check=False, diff=False):
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "-c"
    if diff:
        diff_flag = "--diff"
    c.run(f"{VENV_BIN}/isort {check_flag} {diff_flag} .")


@task
def flake8(c):
    c.run(f"{VENV_BIN}/flake8 {PKG_PATH} tasks.py")


@task
def lint(c):
    isort(c, check=True)
    black(c, check=True)
    flake8(c)


@task
def tools(c):
    """Install tools in the virtual environment if not already on PATH"""
    for tool in TOOLS:
        if not which(tool):
            c.run(f"{VENV_BIN}/pip install {tool}")


@task
def precommit(c):
    """Install pre-commit hooks to .git/hooks/pre-commit"""
    c.run(f"{PRECOMMIT} install")


@task
def setup(c):
    if ACTIVE_VENV is None and not VENV_PATH.exists():
        if SYSTEM_PYTHON:
            print("Creating virutal environment at {VENV}")
            c.run(f"{SYSTEM_PYTHON} -m venv {VENV}")
        else:
            print(
                "Could not determine system Python path. Create and activate a "
                "virtual environment and run again."
            )
    c.run(f"{VENV_BIN}/python -m pip install -U pip")
    tools(c)
    c.run(f"{POETRY} install")
    precommit(c)
