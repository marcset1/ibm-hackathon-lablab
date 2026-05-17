import click
import os
from bobflow.bob_runner import run_bob

@click.command()
@click.argument("path", default=".")
def review(path):
    """Review code quality and suggest improvements using IBM Bob.

    Example: bobflow review ./src
    """
    abs_path = os.path.abspath(path)
    click.echo(f"\n🔎 BobFlow — Code review for '{abs_path}'\n")
    click.echo("🤖 IBM Bob is reviewing...\n")

    prompt = """Review all code files in the current directory.

Provide:
1. Code quality score (1-10) with justification
2. Critical issues to fix immediately
3. Security vulnerabilities if any
4. Performance improvements
5. Best practices violations
6. Suggested refactoring

Format as a structured report."""

    result = run_bob(prompt, cwd=abs_path, mode="ask")

    if result["success"]:
        click.echo(result["output"])
    else:
        click.echo(f"❌ {result['error']}", err=True)
