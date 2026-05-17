import click
import os
from bobflow.bob_runner import run_bob

@click.command()
@click.argument("path", default=".")
def docs(path):
    """Generate or update documentation using IBM Bob.

    Example: bobflow docs ./my-project
    """
    abs_path = os.path.abspath(path)
    click.echo(f"\n📝 BobFlow — Generating docs for '{abs_path}'\n")
    click.echo("🤖 IBM Bob is documenting...\n")

    prompt = """Analyze all code files in the current directory.
Generate or update documentation:
1. Update README.md with full project documentation
2. Add docstrings to all functions missing them
3. Create a CONTRIBUTING.md
4. Document all API endpoints if any

Save all documentation files."""

    result = run_bob(prompt, cwd=abs_path, mode="code")

    if result["success"]:
        click.echo(result["output"])
        click.echo("\n✅ Documentation generated")
    else:
        click.echo(f"❌ {result['error']}", err=True)
