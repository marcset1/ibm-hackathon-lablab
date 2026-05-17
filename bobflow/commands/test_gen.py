import click
import os
from bobflow.bob_runner import run_bob

@click.command()
@click.argument("filepath")
def test(filepath):
    """Generate unit tests for a file using IBM Bob.

    Example: bobflow test src/utils.py
    """
    abs_path = os.path.abspath(filepath)
    cwd = os.path.dirname(abs_path)

    if not os.path.exists(abs_path):
        click.echo(f"❌ File not found: {abs_path}", err=True)
        return

    click.echo(f"\n🧪 BobFlow — Generating tests for '{filepath}'\n")
    click.echo("🤖 IBM Bob is writing tests...\n")

    prompt = f"""Read the file '{os.path.basename(filepath)}' and generate comprehensive unit tests.

Requirements:
- Cover all functions and edge cases
- Use appropriate test framework (pytest for Python, jest for JS)
- Save tests in a test file named 'test_{os.path.basename(filepath)}'
- Include setup/teardown if needed
- Add docstrings to each test"""

    result = run_bob(prompt, cwd=cwd, mode="code")

    if result["success"]:
        click.echo(result["output"])
        click.echo(f"\n✅ Tests generated for {filepath}")
    else:
        click.echo(f"❌ {result['error']}", err=True)
