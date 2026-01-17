import re
import sys
from typing import Optional
from invoke.context import Context
import invoke
from invoke.tasks import task

# Specifying encoding because Windows crashes otherwise when running Invoke
# tasks below:
# UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd'
# in position 16: character maps to <undefined>
# People say, it might also be possible to export PYTHONIOENCODING=utf8 but this
# seems to work.
# FIXME: If you are a Windows user and expert, please advise on how to do this
# properly.
sys.stdout = open(  # pylint: disable=consider-using-with
    1, "w", encoding="utf-8", closefd=False, buffering=1
)


def run_invoke(
    context: Context,
    cmd: str,
    environment: Optional[dict[str, str]] = None,
    warn: bool = False,
    pty: bool = False,
) -> Optional[invoke.runners.Result]:
    def one_line_command(string: str) -> str:
        return re.sub("\\s+", " ", string).strip()

    return context.run(
        one_line_command(cmd),
        env=environment,
        hide=False,
        warn=warn,
        pty=pty,
        echo=True,
    )


@task(default=True)
def list_tasks(context: Context) -> None:
    clean_command = """
        invoke --list
    """
    run_invoke(context, clean_command)


@task
def bootstrap(context: Context) -> None:
    run_invoke(context, "pip install -r requirements.development.txt")


@task
def format_readme(context: Context) -> None:
    run_invoke(
        context,
        """
    prettier
        --write --print-width 80 --prose-wrap always --parser=markdown
        README.md
    """,
    )


@task
def lint_ruff_format(context: Context) -> None:
    result: Optional[invoke.runners.Result] = run_invoke(
        context,
        """
            ruff
                format
                gitkey tasks.py
                --line-length 80
        """,
    )
    assert result is not None
    # Ruff always exits with 0, so we handle the output.
    if "reformatted" in result.stdout:
        print("invoke: ruff format found issues")  # noqa: T201
        result.exited = 1
        raise invoke.exceptions.UnexpectedExit(result)


@task(aliases=["lr"])
def lint_ruff(context: Context) -> None:
    run_invoke(
        context,
        """
            ruff check gitkey tasks.py --fix --cache-dir build/ruff
        """,
    )


@task(aliases=["lm"])
def lint_mypy(context: Context) -> None:
    # These checks do not seem to be useful:
    # - import
    # - misc
    run_invoke(
        context,
        """
            mypy gitkey
                --show-error-codes
                --disable-error-code=import
                --disable-error-code=misc
                --cache-dir=build/mypy
                --strict
                --python-version=3.9
        """,
    )


@task(aliases=["l"])
def lint(context: Context) -> None:
    lint_ruff_format(context)
    lint_ruff(context)
    lint_mypy(context)


@task(aliases=["ti"])
def test_integration(context: Context, focus: Optional[str] = None) -> None:
    filter_arg = f"--filter {focus}" if focus else ""
    run_invoke(context, f"lit -v tests/integration {filter_arg}")


@task(aliases=["c"])
def check(context: Context) -> None:
    lint(context)
    test_integration(context)
